from django.shortcuts import render
# Create your views here.
import boto3
from dateutil.tz import tzutc
import datetime


session = boto3.Session(profile_name='default')

# session = boto3.Session(region_name='us-west-2',
#                             aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
#                             aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
#

def get_ec2_info():
    ec2 = session.client('ec2')
    ec2_resource = boto3.resource('ec2')
    instances = ec2.describe_instances()
    Items = instances['Reservations']
    ec2_assets = []
    for item in Items:
        data = []
        instance_id = item['Instances'][0]['InstanceId']
        data.append(instance_id)
        try:
            pub_ip = item['Instances'][0]['PublicIpAddress']
            data.append(pub_ip)
        except:
            pub_ip = 'none'
            data.append(pub_ip)
        try:
            sgId = item['Instances'][0]['SecurityGroups'][0]['GroupId']
            data.append(sgId)
            security_group = ec2_resource.SecurityGroup(sgId)
            Item = security_group.ip_permissions
            group_acl = []
            for sg_items in Item:
                acl = []
                try:
                    acl.append(sg_items['FromPort'])
                except:
                    acl.append('All')
                try:
                    acl.append(sg_items['IpProtocol'])
                except:
                    acl.append('All')
                for ace in sg_items['IpRanges']:
                    range = []
                    range.append(ace['CidrIp'])
                    acl.append(range)
                group_acl.append(acl)
            data.append(group_acl)
        except:
            sgId = 'none'
            data.append(sgId)
        try:
            name = item['Instances'][0]['PublicDnsName']
            data.append(name)
        except:
            name = item['Instances'][0]['PrivateDnsName']
            data.append(name)
        ec2_assets.append(data)
    return (ec2_assets)

def get_elb_info():
    elbv2 = session.client('elbv2')
    instances = elbv2.describe_load_balancers()
    elbv2_resource = boto3.client('elbv2')
    Items = instances['LoadBalancers']
    elb_assets = []
    for item in Items:
        data = []
        instance_id = item['LoadBalancerArn']
        data.append(instance_id)
        try:
            pub_ip = item['Scheme']
            data.append(pub_ip)
        except:
            pub_ip = 'none'
            data.append(pub_ip)
        try:
            sgId = item['SecurityGroups']
            data.append(sgId)
        except:
            sgId = 'none'
            data.append(sgId)
            security_group = elbv2_resource.SecurityGroup(sgId)
            Item = security_group.ip_permissions
            group_acl = []
            for sg_items in Item:
                acl = []
                try:
                    acl.append(sg_items['FromPort'])
                except:
                    acl.append('All')
                try:
                    acl.append(sg_items['IpProtocol'])
                except:
                    acl.append('All')
                range = []
                for ace in sg_items['IpRanges']:
                    range.append(ace['CidrIp'])
                acl.append(range)
                group_acl.append(acl)
            data.append(group_acl)
        try:
            name = item['DNSName']
            data.append(name)
        except:
            name = "None"
            data.append(name)
        elb_assets.append(data)
    return (elb_assets)

def get_rds_info():
    rds = session.client('rds')
    instances = rds.describe_db_instances()
    rds_resource = boto3.client('rds')
    Items = instances['DBInstances']
    rds_assets = []
    for item in Items:
        data = []
        instance_id = item['DBInstanceIdentifier']
        data.append(instance_id)
        try:
            pub_ip = item['Endpoint']['Address']
            data.append(pub_ip)
        except:
            pub_ip = 'none'
            data.append(pub_ip)
        try:
            sgId = item['VpcSecurityGroups'][0]['VpcSecurityGroupId']
            data.append(sgId)
        except:
            sgId = 'none'
            data.append(sgId)
            Item = rds.describe_db_security_groups()
            # Item = security_group.ip_permissions
            group_acl = []
            for sg_items in Item:
                acl = []
                try:
                    acl.append(sg_items['FromPort'])
                except:
                    acl.append('All')
                try:
                    acl.append(sg_items['IpProtocol'])
                except:
                    acl.append('All')
                range = []
                for ace in sg_items['IpRanges']:
                    range.append(ace['CidrIp'])
                acl.append(range)
                group_acl.append(acl)
            data.append(group_acl)
        try:
            name = item['DBInstanceIdentifier']
            data.append(name)
        except:
            name = "None"
            data.append(name)
        rds_assets.append(data)
    return (rds_assets)


def index(request):
    current_user = request.user.id
    elb_data = get_elb_info()
    ec2_data = get_ec2_info()
    rds_data = get_rds_info()
    context = {
        'ec2_data': ec2_data,
        'rds_data': rds_data,
        'elb_data': elb_data,
    }
    return render(request, 'aws/index.html', context)

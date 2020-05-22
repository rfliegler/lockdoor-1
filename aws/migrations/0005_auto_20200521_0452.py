# Generated by Django 2.2.4 on 2020-05-21 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0004_auto_20200521_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_hash',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_priv_ip',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_pub_ip',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_zone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aws.Zone'),
        ),
    ]
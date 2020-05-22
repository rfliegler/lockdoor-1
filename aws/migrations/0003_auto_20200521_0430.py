# Generated by Django 2.2.4 on 2020-05-21 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0002_asset_asset_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='asset_egress_applied',
            new_name='asset_instance_id',
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='asset_region',
            new_name='asset_name',
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_sgId',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_zone',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='aws.Zone'),
            preserve_default=False,
        ),
    ]

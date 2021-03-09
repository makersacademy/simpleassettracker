# Generated by Django 3.0.7 on 2021-03-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='colour',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='imei',
            field=models.CharField(default=None, max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='storage',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='device_model',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='asset',
            name='device_type',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='asset',
            name='hard_drive',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='ram',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='screen_size',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='year',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]

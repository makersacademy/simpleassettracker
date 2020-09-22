# Generated by Django 3.0.6 on 2020-09-22 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20200914_1300'),
        ('assets', '0005_auto_20200921_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='Company',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='companies.Company'),
            preserve_default=False,
        ),
    ]

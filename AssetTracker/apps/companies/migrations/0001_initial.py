<<<<<<< HEAD
# Generated by Django 3.0.6 on 2020-10-07 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
=======
# Generated by Django 3.0.6 on 2020-09-01 11:20

from django.db import migrations, models
>>>>>>> master


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('owned_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 2.0.1 on 2018-02-05 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signupapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertable',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userinfo', to=settings.AUTH_USER_MODEL),
        ),
    ]

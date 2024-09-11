# Generated by Django 5.0.3 on 2024-09-02 01:17

import base.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OnetimePassword',
            fields=[
                ('id', base.fields.RandomStringIDField(editable=False, max_length=32, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(max_length=6)),
                ('expired_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
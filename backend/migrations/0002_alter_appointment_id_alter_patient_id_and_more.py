# Generated by Django 5.1.6 on 2025-02-27 17:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b36851a0-f66f-4d21-ad87-f50e41ebb6e1'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.UUIDField(default=uuid.UUID('87575297-d3c6-4a7c-b033-ec49ce9035ce'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='professional',
            name='id',
            field=models.UUIDField(default=uuid.UUID('64cb30fd-d315-4e33-abe7-b133cf9f21eb'), editable=False, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-17 00:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='post_id',
            field=models.UUIDField(default=uuid.UUID('f1daca77-926b-463f-bd2e-ec0d87254cd3'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]

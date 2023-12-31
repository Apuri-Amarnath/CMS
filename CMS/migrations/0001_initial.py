# Generated by Django 4.2.6 on 2023-10-17 00:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_post',
            fields=[
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images')),
                ('body', models.TextField()),
                ('post_id', models.UUIDField(default=uuid.UUID('47ce0ca0-eb75-44c9-93a8-9358e8fab895'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]

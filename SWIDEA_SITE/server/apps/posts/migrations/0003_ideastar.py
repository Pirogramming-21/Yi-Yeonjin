# Generated by Django 5.0.7 on 2024-07-17 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_photo_post_image_rename_like_post_interest_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]
# Generated by Django 5.0.7 on 2024-07-17 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('develTools', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='develtool',
            old_name='explan',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='develtool',
            old_name='type',
            new_name='kind',
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-15 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_post_control_rename_content_control_field'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Control',
        ),
    ]

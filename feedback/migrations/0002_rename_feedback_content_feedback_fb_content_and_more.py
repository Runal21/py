# Generated by Django 5.0.3 on 2024-03-29 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='feedback_content',
            new_name='fb_content',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='timestamp',
            new_name='fb_timestamp',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='feedback_type',
            new_name='fb_type',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='username',
            new_name='fb_uname',
        ),
    ]

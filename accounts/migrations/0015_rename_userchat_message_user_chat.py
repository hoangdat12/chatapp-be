# Generated by Django 4.1.1 on 2022-09-19 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_remove_conversation_profile_conversation_userchat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='userchat',
            new_name='user_chat',
        ),
    ]

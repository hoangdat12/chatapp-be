# Generated by Django 4.1.1 on 2022-09-19 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_rename_userchat_message_user_chat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='userchat',
            new_name='user_chat',
        ),
    ]

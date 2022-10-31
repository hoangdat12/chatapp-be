# Generated by Django 4.1.1 on 2022-09-19 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_rename_userchat_conversation_user_chat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='nick_name',
            new_name='nickname',
        ),
        migrations.RenameField(
            model_name='conversation',
            old_name='nick_name',
            new_name='nickname',
        ),
        migrations.RenameField(
            model_name='conversation',
            old_name='user_chat',
            new_name='userchat',
        ),
        migrations.RenameField(
            model_name='friend',
            old_name='nick_name',
            new_name='nickname',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='my_content',
            new_name='mycontent',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='user_chat',
            new_name='userchat',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='is_active',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='nick_name',
            new_name='nickname',
        ),
    ]

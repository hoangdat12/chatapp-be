# Generated by Django 4.1.1 on 2022-09-17 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_conversation_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
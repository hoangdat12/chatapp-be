# Generated by Django 4.1.1 on 2022-09-14 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_friend_delete_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-02-13 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_board_main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='email',
        ),
    ]

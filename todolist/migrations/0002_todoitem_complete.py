# Generated by Django 2.2.6 on 2019-10-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
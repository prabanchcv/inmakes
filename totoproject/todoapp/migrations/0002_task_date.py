# Generated by Django 4.0.4 on 2022-07-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-04-03'),
            preserve_default=False,
        ),
    ]

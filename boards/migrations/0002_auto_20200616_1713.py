# Generated by Django 3.0.7 on 2020-06-16 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='views',
            new_name='numViews',
        ),
    ]

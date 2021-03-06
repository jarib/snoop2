# Generated by Django 2.0.4 on 2018-04-26 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0023_auto_20180426_1305'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='directory',
            unique_together={('parent_directory', 'name_bytes')},
        ),
        migrations.AlterUniqueTogether(
            name='file',
            unique_together={('parent_directory', 'name_bytes')},
        ),
        migrations.RemoveField(
            model_name='directory',
            name='name',
        ),
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
    ]

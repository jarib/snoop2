# Generated by Django 2.0 on 2018-01-06 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20180106_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directory',
            name='parent_directory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='child_directory_set', to='data.Directory'),
        ),
    ]

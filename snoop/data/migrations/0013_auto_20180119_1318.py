# Generated by Django 2.0 on 2018-01-19 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_task_blob_arg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='blob',
            new_name='original',
        ),
        migrations.AlterField(
            model_name='file',
            name='original',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='data.Blob'),
        ),
    ]

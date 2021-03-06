# Generated by Django 2.0 on 2018-03-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0018_auto_20180204_1631'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='digest',
            index=models.Index(fields=['date_modified'], name='data_digest_date_mo_60356c_idx'),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['status'], name='data_task_status_ab742f_idx'),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['func', 'status'], name='data_task_func_7a9361_idx'),
        ),
    ]

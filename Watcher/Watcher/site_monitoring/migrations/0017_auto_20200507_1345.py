# Generated by Django 3.0.6 on 2020-05-07 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_monitoring', '0016_auto_20200507_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='mx_records',
            new_name='MX_records',
        ),
    ]

# Generated by Django 3.1 on 2020-08-10 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200807_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='cid',
            new_name='eid',
        ),
    ]

# Generated by Django 2.1.3 on 2018-12-21 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20181221_0947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='publication_date',
            new_name='date',
        ),
    ]
# Generated by Django 2.1.3 on 2018-12-21 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20181218_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='CAR_TYPES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carnum', models.CharField(max_length=50)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('car_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.CAR_TYPES')),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]

# Generated by Django 3.2.25 on 2025-04-20 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20240801_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msd_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(default='', max_length=50)),
                ('des', models.CharField(default='', max_length=300)),
            ],
        ),
    ]

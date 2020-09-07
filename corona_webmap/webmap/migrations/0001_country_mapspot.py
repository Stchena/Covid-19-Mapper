# Generated by Django 3.0.3 on 2020-09-07 11:03

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('webmap', 'enable_postgis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('population', models.IntegerField()),
                ('area', models.FloatField()),
                ('lat_long', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='MapSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]

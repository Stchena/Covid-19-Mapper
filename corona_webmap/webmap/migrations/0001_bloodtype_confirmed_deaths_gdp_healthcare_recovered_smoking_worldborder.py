# Generated by Django 3.0.3 on 2020-09-11 19:27


import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('webmap', 'enable_postgis'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorldBorder',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('area', models.IntegerField()),
                ('pop2005', models.IntegerField(default='', verbose_name='Population 2005')),
                ('fips', models.CharField(max_length=2, null=True, verbose_name='FIPS Code')),
                ('iso2', models.CharField(default='', max_length=2, verbose_name='2 Digit ISO')),
                ('iso3', models.CharField(default='', max_length=3, verbose_name='3 Digit ISO')),
                ('un', models.IntegerField(default='', verbose_name='United Nations Code')),
                ('region', models.IntegerField(default='', verbose_name='Region Code')),
                ('subregion', models.IntegerField(default='', verbose_name='Sub-Region Code')),
                ('lon', models.FloatField(default='')),
                ('lat', models.FloatField(default='')),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(default='', srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Smoking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('male', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('female', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('total', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('country', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='webmap.WorldBorder')),
            ],
        ),
        migrations.CreateModel(
            name='Recovered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=15)),
                ('total', models.IntegerField()),
                ('country', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='webmap.WorldBorder')),
            ],
        ),
        migrations.CreateModel(
            name='Healthcare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('score', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('country', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='webmap.WorldBorder')),
            ],
        ),
        migrations.CreateModel(
            name='GDP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('gdpPerCapita', models.FloatField()),
                ('country', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='webmap.WorldBorder')),
            ],
        ),
        migrations.CreateModel(
            name='Deaths',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=15)),
                ('total', models.IntegerField()),
                ('country', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='webmap.WorldBorder')),
            ],
        ),
        migrations.CreateModel(
            name='Confirmed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=15)),
                ('total', models.IntegerField()),
                ('country', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='webmap.WorldBorder')),
            ],
        ),
        migrations.CreateModel(
            name='Bloodtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ominus', models.CharField(max_length=10)),
                ('Oplus', models.CharField(max_length=10)),
                ('Aminus', models.CharField(max_length=10)),
                ('Aplus', models.CharField(max_length=10)),
                ('Bminus', models.CharField(max_length=10)),
                ('Bplus', models.CharField(max_length=10)),
                ('ABminus', models.CharField(max_length=10)),
                ('ABplus', models.CharField(max_length=10)),
                ('country', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='webmap.WorldBorder')),
            ],
        ),
    ]
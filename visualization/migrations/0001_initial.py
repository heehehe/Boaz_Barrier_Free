# Generated by Django 2.2.1 on 2019-11-19 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('대분류', models.CharField(blank=True, max_length=100)),
                ('소분류', models.CharField(blank=True, max_length=100)),
                ('시설명', models.CharField(blank=True, max_length=1000)),
                ('주소', models.CharField(blank=True, max_length=2000)),
                ('위도', models.FloatField(blank=True)),
                ('경도', models.FloatField(blank=True)),
                ('전화번호', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]

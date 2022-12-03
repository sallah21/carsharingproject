# Generated by Django 4.1.3 on 2022-12-03 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('idcar', models.IntegerField(db_column='idCar', primary_key=True, serialize=False)),
                ('model', models.CharField(blank=True, db_column='Model', max_length=45, null=True)),
                ('enginetype', models.CharField(blank=True, db_column='EngineType', max_length=45, null=True)),
                ('enginecapacity', models.CharField(blank=True, db_column='EngineCapacity', max_length=45, null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=45, null=True)),
                ('seatsnumber', models.IntegerField(blank=True, db_column='SeatsNumber', null=True)),
                ('value', models.IntegerField(blank=True, db_column='Value', null=True)),
            ],
            options={
                'db_table': 'Cars',
                'managed': True,
            },
        ),
    ]

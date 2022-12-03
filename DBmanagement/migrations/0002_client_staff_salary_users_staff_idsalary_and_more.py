# Generated by Django 4.1.3 on 2022-12-03 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DBmanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('idclient', models.IntegerField(db_column='idClient', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=45, null=True)),
                ('surname', models.CharField(blank=True, db_column='Surname', max_length=45, null=True)),
                ('pesel', models.CharField(blank=True, db_column='PESEL', max_length=45, null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=45, null=True)),
            ],
            options={
                'db_table': 'Client',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('idstaff', models.IntegerField(db_column='idStaff', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=45, null=True)),
                ('surname', models.CharField(blank=True, db_column='Surname', max_length=45, null=True)),
                ('pesel', models.CharField(blank=True, db_column='PESEL', max_length=11, null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=12, null=True)),
                ('position', models.CharField(blank=True, db_column='Position', max_length=45, null=True)),
            ],
            options={
                'db_table': 'Staff',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('idsalary', models.OneToOneField(db_column='idStaff', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='DBmanagement.staff')),
                ('amount', models.IntegerField(blank=True, db_column='Amount', null=True)),
                ('bonus', models.IntegerField(blank=True, db_column='Bonus', null=True)),
            ],
            options={
                'db_table': 'Salary',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('iduser', models.OneToOneField(db_column='idUser', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='DBmanagement.staff')),
                ('login', models.CharField(blank=True, db_column='Login', max_length=45, null=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=45, null=True)),
                ('position', models.CharField(blank=True, db_column='Position', max_length=45, null=True)),
                ('idclient', models.OneToOneField(blank=True, db_column='idClient', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='DBmanagement.client')),
            ],
            options={
                'db_table': 'Users',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='staff',
            name='idsalary',
            field=models.OneToOneField(db_column='idSalary', on_delete=django.db.models.deletion.DO_NOTHING, to='DBmanagement.salary'),
        ),
        migrations.AddField(
            model_name='staff',
            name='iduser',
            field=models.OneToOneField(db_column='idUser', on_delete=django.db.models.deletion.DO_NOTHING, to='DBmanagement.users'),
        ),
        migrations.AddField(
            model_name='client',
            name='iduser',
            field=models.ForeignKey(db_column='idUser', on_delete=django.db.models.deletion.DO_NOTHING, to='DBmanagement.users'),
        ),
    ]

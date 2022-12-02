from django.db import models


class Cars(models.Model):
    idcar = models.IntegerField(db_column='idCar', primary_key=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=45, blank=True, null=True)  # Field name made lowercase.
    enginetype = models.CharField(db_column='EngineType', max_length=45, blank=True, null=True)
    enginecapacity = models.CharField(db_column='EngineCapacity', max_length=45, blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    seatsnumber = models.IntegerField(db_column='SeatsNumber', blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cars'


# Clients Users  Details Orders Insurance  Listofcars  ORders Detail
class Client(models.Model):
    idclient = models.OneToOneField('Users',  models.DO_NOTHING, db_column='idClient', primary_key=True)
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pesel = models.CharField(db_column='PESEL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Client'


class Orders(models.Model):
    idorder = models.OneToOneField('Details', models.DO_NOTHING,  db_column='idOrder', primary_key=True)
    dateoforder = models.DateField(db_column='DateOfOrder', blank=True, null=True)  # Field name made lowercase.
    datestart = models.DateField(db_column='DateStart', blank=True, null=True)  # Field name made lowercase.
    dateend = models.DateField(db_column='DateEnd', blank=True, null=True)  # Field name made lowercase.
    idclient = models.ForeignKey(Client, models.DO_NOTHING, db_column='idClient', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Orders'


class Details(models.Model):
    iddetails = models.OneToOneField(Orders, models.DO_NOTHING, db_column='idOrder', primary_key=True)
    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=45, blank=True, null=True)  # Field name made lowercase.
    buildingnumber = models.CharField(db_column='BuildingNumber', max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Details'


class Feedback(models.Model):
    idorder = models.AutoField(db_column='idOrder', primary_key=True)
    amountofstar = models.IntegerField(db_column='AmountOfStar', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Feedback'


class Listofcars(models.Model):
    idlistofcars = models.OneToOneField('Insurance',  models.DO_NOTHING, db_column='idInsurance', primary_key=True)
    idcar = models.ForeignKey(Cars, models.DO_NOTHING, db_column='idCar', blank=True, null=True)
    idorder = models.ForeignKey('Orders', models.DO_NOTHING, db_column='idOrder', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ListOfCars'


class Insurance(models.Model):
    idinsurance = models.OneToOneField(Listofcars, models.DO_NOTHING,  db_column='idInsurance', primary_key=True)
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    cost = models.IntegerField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Insurance'


class Listofservices(models.Model):
    idlistofservice = models.IntegerField(db_column='idListOfService', primary_key=True)  # Field name made lowercase.
    idservice = models.ForeignKey('Service', models.DO_NOTHING, db_column='idService', blank=True, null=True)
    idservicetype = models.ForeignKey('Servicetype', models.DO_NOTHING, db_column='idServiceType', blank=True,
                                      null=True)
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ListOfServices'


class Listofstaff(models.Model):
    idlistofstaff = models.IntegerField(db_column='idListOfStaff', primary_key=True)  # Field name made lowercase.
    idstaff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='idStaff', blank=True, null=True)
    idservice = models.ForeignKey('Service', models.DO_NOTHING, db_column='idService', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ListOfStaff'


class Payment(models.Model):
    idpayment = models.IntegerField(db_column='idPayment', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    amounttopay = models.IntegerField(db_column='AmountToPay', blank=True, null=True)  # Field name made lowercase.
    dateofpayment = models.DateField(db_column='DateOfPayment', blank=True, null=True)  # Field name made lowercase.
    amountpayed = models.IntegerField(db_column='AmountPayed', blank=True, null=True)  # Field name made lowercase.
    idorder = models.ForeignKey(Orders, models.DO_NOTHING, db_column='idOrder', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Payment'


class Salary(models.Model):
    idsalary = models.OneToOneField('Staff', models.DO_NOTHING,db_column='idStaff', primary_key=True)
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    bonus = models.IntegerField(db_column='Bonus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Salary'


class Staff(models.Model):
    idstaff = models.OneToOneField(Salary, models.DO_NOTHING, db_column='idStaff', primary_key=True)
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pesel = models.CharField(db_column='PESEL', max_length=11, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=12, blank=True, null=True)
    position = models.CharField(db_column='Position', max_length=45, blank=True, null=True)
    iduser = models.OneToOneField('Users', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Staff'


class Service(models.Model):
    idservice = models.IntegerField(db_column='idService', primary_key=True)  # Field name made lowercase.
    dateofstart = models.DateField(db_column='DateOfStart', blank=True, null=True)  # Field name made lowercase.
    dateofend = models.DateField(db_column='DateOfEnd', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    idcar = models.ForeignKey(Cars, models.DO_NOTHING, db_column='idCar', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Service'


class Servicetype(models.Model):
    idservicetype = models.IntegerField(db_column='idServiceType', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cost = models.IntegerField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServiceType'


class Users(models.Model):
    iduser = models.OneToOneField(Staff, models.DO_NOTHING, db_column='idUser', primary_key=True)
    login = models.CharField(db_column='Login', max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45, blank=True, null=True)  # Field name made lowercase
    position = models.CharField(db_column='Position', max_length=45, blank=True, null=True)  # Field name made lowercase
    idclient = models.OneToOneField(Client, models.DO_NOTHING, db_column='idClient', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'

from django.db import models
class Car(models.Model):
    idcar = models.AutoField(db_column='idCar', primary_key=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=45, blank=True, null=True)  # Field name made lowercase.
    enginetype = models.CharField(db_column='EngineType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    enginecapacity = models.CharField(db_column='EngineCapacity', max_length=45, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numberofseats = models.IntegerField(db_column='NumberOfSeats', blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Car'


class Client(models.Model):
    idclient = models.AutoField(db_column='idClient', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pesel = models.CharField(db_column='PESEL', max_length=11, blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Client'


class Insurance(models.Model):
    idinsurance = models.AutoField(db_column='idInsurance',primary_key=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type',max_length=45, blank=True, null=True)  # Field name made lowercase.
    cost = models.IntegerField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    idlistofcars = models.ForeignKey('Listofcars', models.DO_NOTHING, db_column='idListOfCars', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Insurance'


class Listofcars(models.Model):
    idlistofcars = models.AutoField(db_column='idListOfCars', primary_key=True)  # Field name made lowercase.
    idorder = models.ForeignKey('Order', models.DO_NOTHING, db_column='idOrder', blank=True, null=True)  # Field name made lowercase.
    idcar = models.ForeignKey(Car, models.DO_NOTHING, db_column='idCar', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ListOfCars'


class Listofservice(models.Model):
    idlistservices = models.AutoField(db_column='idListServices', primary_key=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    idservice = models.ForeignKey('Service', models.DO_NOTHING, db_column='idService', blank=True, null=True)  # Field name made lowercase.
    idservicetype = models.ForeignKey('Servicetype', models.DO_NOTHING, db_column='idServiceType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ListOfService'


class Listofstaff(models.Model):
    idliststaff = models.AutoField(db_column='idListStaff', primary_key=True)  # Field name made lowercase.
    idstaff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='idStaff', blank=True, null=True)  # Field name made lowercase.
    idservice = models.ForeignKey('Service', models.DO_NOTHING, db_column='idService', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ListOfStaff'


class Order(models.Model):
    idorder = models.AutoField(db_column='idOrder', primary_key=True)  # Field name made lowercase.
    dateoforder = models.DateField(db_column='DateOfOrder', blank=True, null=True)  # Field name made lowercase.
    datestart = models.DateField(db_column='DateStart', blank=True, null=True)  # Field name made lowercase.
    dateend = models.DateField(db_column='DateEnd', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=45, blank=True, null=True)  # Field name made lowercase.
    buldingnumber = models.CharField(db_column='BuldingNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    feedback = models.TextField(db_column='Feedback', blank=True, null=True)  # Field name made lowercase.
    idclient = models.ForeignKey(Client, models.DO_NOTHING, db_column='idClient', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Order'


class Payment(models.Model):
    idpayment = models.AutoField(db_column='idPayment', primary_key=True)  # Field name made lowercase.
    amounttopay = models.IntegerField(db_column='AmountToPay', blank=True, null=True)  # Field name made lowercase.
    amountpayed = models.IntegerField(db_column='AmountPayed', blank=True, null=True)  # Field name made lowercase.
    dateofpayment = models.DateField(db_column='DateOfPayment', blank=True, null=True)  # Field name made lowercase.
    idorder = models.ForeignKey(Order, models.DO_NOTHING, db_column='idOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Payment'


class Service(models.Model):
    idservice = models.AutoField(db_column='idService', primary_key=True)  # Field name made lowercase.
    dateservicestart = models.DateField(db_column='DateServiceStart', blank=True, null=True)  # Field name made lowercase.
    dateserviceend = models.DateField(db_column='DateServiceEnd', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    idcar = models.ForeignKey(Car, models.DO_NOTHING, db_column='idCar', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Service'


class Servicetype(models.Model):
    idservicetype = models.AutoField(db_column='idServiceType', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name',max_length=45 ,blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    cost = models.IntegerField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ServiceType'


class Staff(models.Model):
    idstaff = models.AutoField(db_column='idStaff', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pesel = models.CharField(db_column='PESEL', max_length=11, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=12, blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=45, blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45, blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Staff'

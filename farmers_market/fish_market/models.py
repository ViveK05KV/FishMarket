from django.db import models

# Create your models here.
class FishDB(models.Model):
    name = models.CharField(max_length=140)
    category = models.CharField(max_length=20)
    description = models.TextField()
    picURL = models.CharField(max_length=255)

class registration(models.Model):
    uid = models.AutoField(primary_key = True)
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    mobileno = models.IntegerField()
    email = models.CharField(max_length = 100)
    address1 = models.CharField(max_length = 1000)
    address2 = models.CharField(max_length = 1000)

class login(models.Model):
    uid = models.ForeignKey(registration,on_delete=models.CASCADE)
    username = models.CharField(max_length=100,unique = True)
    password = models.CharField(max_length=100,unique = True)

class fishmain(models.Model):
    fid = models.AutoField(primary_key = True)
    fishname = models.CharField(max_length = 100,unique = True)
    fishdesc = models.CharField(max_length = 5000)
    fishurl = models.URLField()
    fishtype = models.CharField(max_length = 2)

class fishcurrent(models.Model):
    id = models.AutoField(primary_key = True)
    fid = models.ForeignKey(fishmain,on_delete = models.CASCADE)
    currentfish = models.IntegerField()
    currentrate = models.IntegerField()
    wrate = models.IntegerField(default = '0')
    clrate = models.IntegerField(default = '0')
    ccrate = models.IntegerField(default = '0')

class fishorder(models.Model):
    id = models.AutoField(primary_key = True)
    uid = models.ForeignKey(registration,on_delete = models.CASCADE)
    fid = models.ForeignKey(fishmain,on_delete = models.CASCADE)
    weight = models.IntegerField()

class issue(models.Model):
    id = models.AutoField(primary_key = True)
    uid = models.ForeignKey(registration,on_delete = models.CASCADE)
    userissue = models.CharField(max_length = 5000)

from django.db import models

# Create your models here.

class Player(models.Model):
  #id=models.AutoField()              // a field automatically generated by django in its DB. We dont need to write it explicitely in our model
  name=models.CharField(max_length=100)
  age=models.IntegerField()
  address=models.TextField()
  email=models.EmailField(null=True, blank=True)

class User(models.Model):
  pass

class Car(models.Model):
  name=models.CharField(max_length=50)
  topSpeed=models.IntegerField()

  def __str__(self):
      return self.name
  
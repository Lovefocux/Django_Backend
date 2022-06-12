<<<<<<< HEAD
from ast import Return
from email.headerregistry import Address
from django.db import models

# Create your models here.
class Schools(models.Model):
   name = models.CharField(max_length=23)
   Address = models.CharField(max_length=23)

   def __str__(self) -> str:
      return self.name

class Country(models.Model):
   name = models.CharField(max_length=23)
   def __str__(self) -> str:
=======
from ast import Return
from email.headerregistry import Address
from django.db import models

# Create your models here.
class Schools(models.Model):
   name = models.CharField(max_length=23)
   Address = models.CharField(max_length=23)

   def __str__(self) -> str:
      return self.name

class Country(models.Model):
   name = models.CharField(max_length=23)
   def __str__(self) -> str:
>>>>>>> 73e61ff79d44c22cda4c549eccd06f4f316fa5d0
      return self.name
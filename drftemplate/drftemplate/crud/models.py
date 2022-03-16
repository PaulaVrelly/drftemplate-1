import email
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=120, verbose_name='Nombre')
    last_name = models.CharField(max_length=120, verbose_name='Apellido')
    age = models.IntegerField(default=0, verbose_name='Edad')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Creacion')
    status = models.BooleanField(default=True, verbose_name='status')

    class Meta:
        db_table = 'persons'
        
class Rol(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nombre')
    applicant = models.BooleanField(default=True, verbose_name='Solicitante')
    employer = models.BooleanField(default=False,verbose_name='Empleador')
    
    class Meta:
        db_table = 'roles'
    
class User(models.Model):
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email')
    password = models.CharField(max_length=120,verbose_name='Contraseña')
    rol = models.ForeignKey(Rol, related_name='rol', on_delete=models.CASCADE, null=True, verbose_name='Rol')  
    
    class Meta:
        db_table = 'users'
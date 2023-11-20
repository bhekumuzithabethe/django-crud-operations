from django.db import models

# Create your models here.


class Position(models.Model):

    position = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Position")
        verbose_name_plural = ("Positions")

    def __str__(self):
        return f'{self.position}'

class Employee(models.Model):
    position = models.ForeignKey(Position, verbose_name=("Employee Position"), on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    cellphone = models.CharField(max_length=13,default="+27")
    salary = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return f'Employee: {self.first_name} {self.last_name}'

from django.db import models

# Create your models here.
class  Type_of_Router(models.Model):
    sap_id=models.CharField(primary_key=True,unique=True,max_length=50)
    router_type=models.TextField(max_length=50)
    def __str__(self):
        return self.router_type

class Router_Details(models.Model):
    router_id=models.CharField(primary_key=True,unique=True,max_length=50)
    loopback=models.CharField(max_length=50,default=False)
    hostname=models.CharField(max_length=50,unique=True)
    sap_id=models.ForeignKey(Type_of_Router,on_delete=models.CASCADE)



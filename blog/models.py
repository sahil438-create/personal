from django.db import models
from datetime import datetime 
class Project1(models.Model):
    name=models.CharField(max_length=250)
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to='images/')
    url=models.URLField(max_length=200 ,blank=True)
    date = models.DateTimeField(default=datetime.now(), blank=True)  


    def __str__(self):
        return self.description
    


# Create your models here.

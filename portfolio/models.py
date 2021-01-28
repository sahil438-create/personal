from django.db import models 
from datetime import datetime 

class Project(models.Model):
    titleman=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='portfolio/images')
    url=models.URLField(blank=True)
    date = models.DateTimeField(default=datetime.now(), blank=True)



    def __str__(self):
        return self.description
        
    
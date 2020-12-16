from django.db import models

# Create your models here.
class student(models.Model):
    cname=models.CharField(max_length=20, null= False)
    cphone=models.CharField(max_length=50, null= False)
    caddr=models.CharField(max_length=255, null= False)
    def __str__(self):
        return self.cname
        
        
class memberform(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name=models.CharField(max_length=50, null= False)
    tel=models.CharField(max_length=50, null= False)
    addr=models.CharField(max_length=50, null= False)
    def __str__(self):
        return self.name       

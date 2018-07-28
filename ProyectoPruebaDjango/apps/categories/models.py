from django.db import models

# Create your models here.

class Category(models.Model):
    #id = models.AutoField(primary_key=True) #Added by default, not required explicitly
    name = models.CharField(max_length=30)
    description = models.TextField()
    #objects = models.Manager() #Added by default, not required explicitly

    def __str__(self):
        return "Name: %s - Category: %s" % (self.name, self.description)




      

from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30) 

    def __str__(self):
        return self.username

class ModelFile(models.Model):
  content_image = models.ImageField(upload_to='documents/')
  result_image = models.ImageField(upload_to='documents/output.jpg')

  

from django.db import models
from django.contrib.auth.models import User

class cameraimage(models.Model):
    tphoto = models.FileField(upload_to='tumorcamra',blank=True,max_length=None)
    username =  models.ForeignKey(User,null = True, on_delete = models.CASCADE)
    description = models.CharField(max_length=1000,blank=True)
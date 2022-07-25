from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Tag(models.Model):
    def __str__(self):
        return self.tagname
    tagname=models.CharField(max_length=200)
class Advert(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=200)
    tags=models.ManyToManyField(Tag)
    image=models.ImageField(upload_to='image/')
    ad_url=models.CharField(max_length=500)
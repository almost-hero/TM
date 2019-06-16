import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User,Group
from django.utils.text import slugify
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 150,unique = True)
    slug = models.SlugField(max_length=150,unique = True,blank=True)
    user = models.ManyToManyField(User,blank=True)
    role = models.ForeignKey(Group,on_delete=models.CASCADE,blank=True,null=True)
    
    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)


    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length=150,unique = True,blank=True)
    description = models.TextField(blank = True)
    pr = models.ForeignKey('Project',on_delete=models.CASCADE,blank=True,null=True)
    developer = models.ForeignKey(User,on_delete = models.SET_NULL,blank=True,null=True)
    due_date = models.DateField(default=datetime.datetime.now() + datetime.timedelta(days=7))

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title

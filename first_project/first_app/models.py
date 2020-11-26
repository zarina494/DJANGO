from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now=True)

    image = models.ImageField()
    blog = models.ForeignKey(Blog,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title


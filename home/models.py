from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class About(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    about_me = models.TextField()
    tag_line = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=14, default=000000)
    github_link = models.CharField(max_length=200, default='www.example.com')
    linkedin_link = models.CharField(max_length=200, default='www.example.com')
    twitter_link = models.CharField(max_length=200, default='www.example.com')

    class Meta:
        verbose_name_plural = 'About'
        ordering = ['user']

    def __str__(self):
        return str(self.user)


class Skill(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

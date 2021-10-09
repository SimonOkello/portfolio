from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.


class About(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    about_me = models.TextField()
    tag_line = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=14, default=000000)
    github_url = models.CharField(max_length=200, default='www.example.com')
    linkedin_url = models.CharField(max_length=200, default='www.example.com')
    twitter_url = models.CharField(max_length=200, default='www.example.com')

    class Meta:
        verbose_name_plural = 'About'
        ordering = ['user']

    def __str__(self):
        return str(self.user)


class Skill(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    skill_image = models.ImageField(upload_to='media/skills', default='default.png')
    skill_tags = TaggableManager()

    def __str__(self):
        return str(self.name)


class Service(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return str(self.name)


class Resume(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    c_vitae = models.FileField(upload_to='media/CVS/%Y/%m/%D')
    cover_letter = models.FileField(upload_to='media/CoverLetters/%Y/%m/%D', null=True, blank=True)

    def __str__(self):
        return str(self.c_vitae)
class Portfolio(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    screenshot = models.ImageField(upload_to='media/portfolio')
    preview_url = models.CharField(max_length=255, null=True, blank=True)
    source_code_url = models.CharField(max_length=255, null=True, blank=True)
    tags = TaggableManager()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

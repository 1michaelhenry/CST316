from django.db import models

# Create your models here.
class posts(models.Model):
        author = models.CharField(max_length = 30)
        title = models.CharField(max_length = 100)
        bodytext = models.TextField()
        timestamp = models.DateTimeField(null=True)

class users(models.Model):
	username = models.CharField(max_length = 30)
	password = models.CharField(max_length = 30)

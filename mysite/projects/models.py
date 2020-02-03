from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    coordinator = models.CharField(max_length=70)
    coordinator_email = models.EmailField()
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    is_approved = models.BooleanField()

    def __str__(self):
        return self.title

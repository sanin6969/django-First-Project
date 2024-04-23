from django.db import models

# Create your models here.

class Movieinfo(models.Model):
    title=models.CharField(max_length=200)
    year=models.IntegerField(null=True)
    rating=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.title

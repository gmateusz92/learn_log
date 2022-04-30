from django.db import models

class Description(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
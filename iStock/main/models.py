from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    date_updated = models.DateField(auto_now_add=True)
    type = models.TextField()
    description = models.TextField()

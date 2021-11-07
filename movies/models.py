from django.db import models

import uuid
# Create your models here.
class Movie(models.Model):
    # django auto creates id field could have saved myself hours 😢 of reading
    # movie_id = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    # categor_id = models.AutoField()
    name = models.CharField(max_length=40)
    discription = models.TextField()

    def __str__(self):
        return self.name

class Cast(models.Model):

    number_of_people = models.IntegerField()
    
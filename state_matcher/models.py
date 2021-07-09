from django.db import models

# Create your models here.

class UserDetails(models.Model):

    name = models.TextField()
    state = models.CharField(max_length=30)


    def __str__(self):
        return self.name + " from " + self.state 
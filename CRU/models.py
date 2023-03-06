from django.db import models


# Create your models here.
class General_provisions(models.Model):
    intro = models.TextField()
    fount = models.TextField()
    addition = models.TextField()

    def is_valid(self):
        pass


class Smth(models.Model):
    add_items = models.TextField()
    concl = models.TextField()

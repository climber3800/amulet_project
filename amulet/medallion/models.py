from django.db import models


class UserAmulet(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    runes = models.TextField()
    style = models.CharField(max_length=30)
    material = models.CharField(max_length=30)

    def __str__(self):
        return self.last_name

from django.db import models

class log(models.Model):
    mac = models.CharField(max_length=50)
    slave = models.CharField(max_length=10)
    message = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mac

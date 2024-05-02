from django.db import models
from django.contrib.auth.models import User

class Unduhan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    judul = models.CharField(max_length=100)
    waktu_diunduh = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
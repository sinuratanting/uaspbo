from django.db import models

class Koordinat(models.Model):
    nama_cafe = models.CharField(max_length=100, null=True)
    alamat = models.CharField(max_length=100)
    koordinat = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_cafe

class Menu(models.Model):
    nama_menu = models.TextField(null=True)
    keterangan = models.CharField(max_length=100, null=True)
    harga = models.CharField(max_length=20)
    img = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nama_menu
    

    
# Create your models here.

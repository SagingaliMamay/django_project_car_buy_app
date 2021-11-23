from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Merk : ', max_length=50)
    task = models.TextField( 'Beschrijving:')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Brandstof:'
        verbose_name_plural = "Brandstofs"
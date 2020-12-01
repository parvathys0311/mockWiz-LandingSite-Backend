from django.db import models

# Create your models here.

class Function(models.Model):
    functionID = models.AutoField(primary_key = True)
    functionName = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.functionName
from django.db import models

# Create your models here.
class contactuser(models.Model):
      name1 = models.CharField(max_length=20)
      phone1 = models.CharField(max_length=10)
      email1 = models.CharField(max_length=20)
      txt = models.CharField(max_length=50)
      message1 = models.CharField(max_length=100)

      def __str__(self):
            return self.name1 
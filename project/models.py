from django.db import models


class feedback(models.Model):
      name = models.CharField(max_length=10)
      phone_number = models.CharField(max_length=10)
      email = models.CharField(max_length=20)
      message = models.TextField(max_length=100)

      def __str__(self):
            return self.name 
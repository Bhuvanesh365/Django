from django.db import models

class Gst_app(models.Model):
  customer_name = models.CharField(max_length=255)
  user_id = models.CharField(max_length=255)
  password = models.CharField(max_length=255)

def __str__(self):
    return f"{self.customer_name}"
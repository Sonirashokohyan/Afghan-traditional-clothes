from django.db import models

class Member(models.Model):
  productName = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  material = models.CharField(max_length=255)
  price = models.IntegerField(null=True)
  pub_date = models.DateField(null=True)

from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    speed = models.CharField(max_length=255)
    data_cap = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, choices=[('residential', 'Residential'), ('business', 'Business'), ('prepaid', 'Prepaid')])

    def __str__(self):
        return self.name

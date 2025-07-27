from django.db import models
import uuid

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    tin = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()
    nic_or_passport = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

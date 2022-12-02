from django.db import models
import uuid
class Content(models.Model):
    itemName = models.CharField(max_length=200)
    description = models.TextField(null= True, blank=True)
    image = models.ImageField(default="Screenshot.png", null=True, blank=True)
    image1 = models.ImageField(default="Screenshot.png", null=True, blank=True)
    image2 = models.ImageField(default="Screenshot.png", null=True, blank=True)
    image3 = models.ImageField(default="Screenshot.png", null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self):
        return self.itemName
class contectTable(models.Model):
    firstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    email = models.EmailField()
    phoneNumber = models.IntegerField()

    def __str__(self):
        return self.email
# Create your models here.

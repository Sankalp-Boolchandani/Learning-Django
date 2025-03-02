from email.mime import image
from django.db import models

# Create your models here.

class Recipe(models.Model):
  recipe_name=models.CharField(max_length=100)
  recipe_desc=models.TextField()
  recipe_image=models.ImageField(upload_to="vege/images")

  def __str__(self):
      return self.name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #foreign key throws an error if null and blank are not specified since django then confuses it with the id.
  recipe_name=models.CharField(max_length=100)
  recipe_desc=models.TextField()
  recipe_image=models.ImageField(upload_to="vege/images")
  recipe_views=models.IntegerField(null=True)
from django.db import models
from django.contrib.auth.models import User
from .utils import *
from django.utils import timezone

# Create your models here.

class Recipe(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #foreign key throws an error if null and blank are not specified since django then confuses it with the id.
  recipe_name=models.CharField(max_length=100)
  recipe_desc=models.TextField()
  recipe_image=models.ImageField(upload_to="vege/images")
  recipe_views=models.IntegerField(null=True)
  slug=models.SlugField(unique=True, default=timezone.now())
  
  # logic to save slug string automatically on the new object creation
  def save(self, *args, **kwargs):
    self.slug=generate_slug(self.recipe_name)
    super(Recipe, self).save(*args, **kwargs)
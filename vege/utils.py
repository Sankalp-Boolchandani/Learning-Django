from django.utils.text import slugify
import uuid

# logic to create a slug string using slugify
def generate_slug(title:str)->str:
  from .models import Recipe
  slug=slugify(title)
  while Recipe.objects.filter(slug=slug).exists():            # checks if the slug string already exists or not
    slug=f'{slugify(title)}-{str(uuid.uuid4())[:4]}'
  return slug
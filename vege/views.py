from django.shortcuts import render, redirect
from vege.models import *
from django.http import HttpResponse

# Create your views here.

def recipe(request):
  page="Recipe page"
  if request.method=="POST":
    data = request.POST
    recipe_image=request.FILES.get("recipe_image")
    recipe_name=data.get("recipe_name")
    recipe_desc=data.get("recipe_desc")

    print(recipe_name)
    print(recipe_desc)
    print(recipe_image)

    Recipe.objects.create(
      recipe_name=recipe_name,
      recipe_desc=recipe_desc,
      recipe_image=recipe_image
    )
    return redirect("/recipe")

  return render(request, 'recipes.html', context={'page':page})

def allRecipes(request):
  page="Your Recipes"
  queryset=Recipe.objects.all()
  context={"recipes":queryset, "page":page}
  return render(request, "viewAllRecipes.html", context) #vege\templates\viewAllRecipes.html

def deleteRecipe(request, id):
  recipe=Recipe.objects.get(id=id)
  recipe.delete()
  return redirect("/allRecipes")

def updateRecipe(request, id):
  page="Update Recipe"
  recipe=Recipe.objects.get(id=id)

  if request.method=="POST":
    data=request.POST
    
    recipe.recipe_name=data.get("recipe_name")
    recipe.recipe_desc=data.get("recipe_desc")
    if request.FILES.get("recipe_image"):
      recipe.recipe_image=request.FILES.get("recipe_image")
    recipe.save()

    return redirect("/allRecipes")
    
  context={
    "page":page,
    "recipe":recipe
    }
  return render(request, "updateRecipe.html", context) #vege\templates\updateRecipe.html
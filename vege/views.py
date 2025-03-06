from django.shortcuts import render, redirect
from vege.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User

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
  recipes=Recipe.objects.all()

  #used to get the string that is being searched in the search bar. Django identifies the result with the associated name which in this case is "search"
  # first .GET is for the get method, second .get is for getting the result with the associated name 
  if request.GET.get('search'): 
    recipes=recipes.filter(recipe_name__icontains = request.GET.get('search'))
  
  context={"recipes":recipes, "page":page}
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

    return redirect("/updateRecipe/"+id+"/")
    
  context={
    "page":page,
    "recipe":recipe
    }
  return render(request, "updateRecipe.html", context) #vege\templates\updateRecipe.html

def login_page(request):
  page="Login"
  context={
    "page":page,
    }
  return render(request, "login.html", context)

def register_page(request):
  page="Register"
  if request.method=="POST":
    user=request.POST
    User.objects.create(
      first_name=user.get("first_name"),
      last_name=user.get("last_name"),
      username=user.get("username"),
      password=user.get("password")
    )
    return redirect("/login")


  context={
    "page":page,
    }
  return render(request, "register.html", context)

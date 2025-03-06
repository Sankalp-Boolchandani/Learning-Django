from django.shortcuts import render, redirect
from vege.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login_page")
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

@login_required(login_url="login_page")
def allRecipes(request):
  page="Your Recipes"
  recipes=Recipe.objects.all()

  #used to get the string that is being searched in the search bar. Django identifies the result with the associated name which in this case is "search"
  # first .GET is for the get method, second .get is for getting the result with the associated name 
  if request.GET.get('search'): 
    recipes=recipes.filter(recipe_name__icontains = request.GET.get('search'))
  
  context={"recipes":recipes, "page":page}
  return render(request, "viewAllRecipes.html", context) #vege\templates\viewAllRecipes.html

@login_required(login_url="login_page")
def deleteRecipe(request, id):
  recipe=Recipe.objects.get(id=id)
  recipe.delete()
  return redirect("/allRecipes")

@login_required(login_url="login_page")
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
  
  if request.method=="POST":
    data=request.POST
    username=data.get("username")
    password=data.get("password")

    if not User.objects.filter(username=username).exists():
      messages.error(request, "User doesn't exists.")
      return redirect("/login")
    else:
      user=User.objects.get(username=username)
      if authenticate(username=username, password=password):
        login(request, user)
        return redirect("/recipe")
      else:
        messages.error(request, "Invalid credentials.")

  return render(request, "login.html", context={"page":page})

def register_page(request):
  page="Register"
  if request.method=="POST":
    data=request.POST
    first_name=data.get("first_name")
    last_name=data.get("last_name")
    username=data.get("username")
    password=data.get("password")

    user=User.objects.filter(username=username)
    if user.exists():
      messages.error(request, "Username already taken.")
      return redirect("/register")
    else:
      user=User.objects.create(
        first_name=first_name,
        last_name=last_name,
        username=username
      )
      user.set_password(password)
      user.save()

      messages.success(request, "User created successfully.")
      return redirect("/register")

  return render(request, "register.html", context={"page":page})

@login_required(login_url="login_page")
def logout_user(request):
  logout(request)
  return redirect("/login_page")
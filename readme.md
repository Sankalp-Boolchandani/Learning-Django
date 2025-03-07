# Self notes:
  - Always add the app as soon as you create it in the setting .py to register it. Why? So that the apps are integrated/mapped correctly in django
  - Urls.py: all the related routing
  - views.py: all the logics are written in views.py
  - templates: htmls that are rendered using views
  - context: **used in views.py**, helps us to send backend data to the templates(html pages), in html pages the data can be rendered using double curly brackets.(-{{data}}-)
  - base-template: a common template for all the html pages with the required data to avoid writing same code multiple times. DRY(dont repeat yourself). Done using block tag 
  - Models: DB structure. Schema of the DB cosisting of all the fields.
  - Unless stated otherwise, by default method of a form is GET. Can be used for getting all the results or searching queries/objects/items.
  - __icontains is used to search related queries if they contain the specified string in the search option
  - autheticate: in built django function that helps us check the credentials for logging in
  - login: in built django function that logs in the user for a session, i.e. using this function helps save login details of a user for a specific time or till one logs out. Basically helps logging in.
  

# Migrations:
  - python manage.py **makemigrations**: helps to create new migrations whenever anything is added or updated in the models
  - python manage.py **migrate**: finally creates the database
  - *Note*: on every makemigrate command a new migrations file is generated and it consists of the imformation and config of the changes that are made, deletion of any of the migrations file can result in the collapse of the database. This is because of the dependencies that are added in the migrations file

# About Project:
  - PP: initial for "personal project" used in commits

# Django ORM:
  - somewhat in relation to sql.
  - order_by('field') - helps in arranging in ascending order. order_by('-field') for descending
    *ex: Recipe.objects.all().order_by()*
  - __lte: helps giving a range less than specified number
    *ex: Recipe.objects.filter(recipe_views__lte=20)*
  - __gte: helps giving a range greater than specified number
    *ex: Recipe.objects.filter(recipe_views__gte=20)*
  - slicing: works similar to sl command LIMIT. Gives the most or least number of specified items
    *ex: Recipe.objects.all().order_by('recipe_views')[0,100]. Gives 100 items with in ascending order of views* 

# To-Do(self, after project):
  - Use CDN(AWS s3) for storing and accessing the images
"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from college.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('admin/', admin.site.urls),
    path('context', context, name='context'),

    # Recipe
    path('recipe', recipe, name='recipe'),
    path('allRecipes', allRecipes, name='viewRecipes'),
    path('deleteRecipe/<slug>/', deleteRecipe, name='deleteRecipe'),
    path('updateRecipe/<slug>/', updateRecipe, name='deleteRecipe'),
    path('login_page', login_page, name='login_page'),
    path('register_page', register_page, name='register_page'),
    path('logout_user', logout_user, name='logout_user'),
    path('success_page', success_page, name='success_page'),

    # College
    path('students', get_students, name='get_students'),
    path('see_marks/<email>', see_marks, name='see_marks'),

]


if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
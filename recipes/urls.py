from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
    #path('sobre/', sobre),
    #path('contato/', contato),
]
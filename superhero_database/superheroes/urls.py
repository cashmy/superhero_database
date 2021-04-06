from django.urls import path
from . import views

app_name = 'superheroes'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>', views.delete, name='delete'),
    path('<int:superhero_id>', views.update, name='update'),
    path('<int:superhero_id>', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero'),

]

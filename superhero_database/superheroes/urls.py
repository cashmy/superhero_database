from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'superheroes'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:superhero_id>', views.delete, name='delete'),
    path('update/<int:superhero_id>', views.update, name='update'),
    path('detail/<int:superhero_id>', views.detail, name='detail'),
    path('create/', views.create, name='create_new_superhero'),

]

urlpatterns += staticfiles_urlpatterns()
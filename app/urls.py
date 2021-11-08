from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('welcome/', views.welcome, name ='home'),
    path('index/', views.index, name = 'index'),
    path('add-todo/', views.add_todo, name = 'add_todo'),
    path('delete-todo/<int:id>', views.delete_todo, name = 'delete_todo'),
    path('logout/', views.logout, name = 'logout'),
    path('change-status/<int:id>/<str:status>', views.change_status)


]
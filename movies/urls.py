from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.create,name='create'),
    path('edit/<id>',views.edit,name='edit'),
    path('delete/<id>',views.delete,name='delete'),
    path('list/',views.list,name='list'),
    path('signup/',views.signup,name='signup'),
    path('',views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('index/',views.index,name='index'),
    path('clear/', views.clear_session, name='clear_session'),
   
]
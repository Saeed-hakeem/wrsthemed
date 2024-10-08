from django.urls import path
from . import views
#from .views import CustomLoginView
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('', views.index, name='index'),
    #path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('add_type', views.add_type, name='add_type'),
    path('list_type', views.list_type, name='list_type'),
    path('add_dep', views.add_dep, name='add_dep'),
    path('list_dep', views.list_dep, name='list_dep'),
    path('list_user', views.list_user, name='list_user'),
    path('add_user', views.add_user, name='add_user'),
    path('add_rank', views.add_rank, name='add_rank'),
    path('list_rank', views.list_rank, name='list_rank'),
    path('update_type/<int:id>/', views.update_type, name='update_type'),
    path('update_dep/<int:id>/', views.update_dep, name='update_dep'),
    path('update_rank/<int:id>/', views.update_rank, name='update_rank'),
    #path('<int:id>/', views.add_type, name='update_type'),
    path('', views.add_user, name='update_department'),
    path('delete_dep/<int:id>/', views.delete_dep, name='delete_dep'),
    path('delete_type/<int:id>/', views.delete_type, name='delete_type'),
    path('delete_rank/<int:id>/', views.delete_rank, name='delete_rank'),
    path('edit_rank/<int:id>/', views.edit_rank, name='edit_rank'),
    path('edit_dep/<int:id>/', views.edit_dep, name='edit_dep'),
    path('edit_type/<int:id>/', views.edit_type, name='edit_type'),
    #path('register/', views.register, name='register'),
    path('teamlead/', views.team_lead, name='teamlead'),
    path('so2/', views.so2, name='so2'),
]
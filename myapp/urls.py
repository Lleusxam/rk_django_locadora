from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('crud/', views.crud, name='crud'),
    path('consulta/', views.consulta, name='consulta'),
    path('listagem/', views.listagem, name='listagem'),
    path('sobre/', views.sobre, name='sobre'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('busca/', views.busca, name='busca')
]

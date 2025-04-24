from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('obrigado/', views.obrigado),
    path('all-data/', views.dados),
    path('update/<int:id>/', views.atualizar, name="update"),
    path('delete/<int:id>/', views.deletar, name="delete"),

    # URLs COOKIES
    path('set/', views.set),
    path('get/', views.get),
    path('delete/', views.delete),
    path('update/', views.update)
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"), 
    path("producto", views.producto, name="producto"),
    path("<int:producto_id>", views.articulo, name="articulo" ),
    path("lista_seguimiento" , views.lista_seguimiento , name="lista_seguimiento")
]

"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#from blogPost.ejemploTrabajo.ejemRequestProject import saludo, adios, dameFecha, calculaEdad
#path('saludo/', saludo),
#path('adios/', adios),
#path('fecha/', dameFecha),
#path('edades/<int:edad>/<int:agnoActual>/<int:agnoFuturo>', calculaEdad),
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from indexTemplate.views import index, login
from users.views import listUser, createUser, updateUser, deleteUser
from post.views import post, createPost, updatePost, deletePost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('listUser/', listUser, name="list_user"),
    path('signUp/', createUser, name= 'signUp'),
    path('signIn/', login, name= 'signIn'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name= 'logout'),
    path('updateUser/<int:id>/', updateUser, name = 'update_user'),
    path('deleteUser/<int:id>/', deleteUser, name = 'delete_user'),
    path('listPost/', post, name = 'post_list'),
    path('createPost/', createPost, name= 'create_post'),
    path('updatePost/<int:id>', updatePost, name = 'update_post'),
    path('deletePost/<int:id>', deletePost, name = 'delete_post'),
]

from django.contrib import admin
from .models import Post

#Registra nuestro objeto Post ene el administrador
#de Django para poder consualtar  o actualizar la la informaciòn del o de los Post

admin.site.register(Post)

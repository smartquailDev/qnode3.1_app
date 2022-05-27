from django.contrib import admin
from .models import Profile, UserRequest


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','admin_user','direccion','telefono','RUC', 'photo']

@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    list_display = ['admin_user','edificio','direccion','email']

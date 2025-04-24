from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import MyUser

User = get_user_model()


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    empty_value_display = '-пусто-'

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserRegistrationForm

User = get_user_model()


@admin.register(User)
class MyUserAdmin(BaseUserAdmin):
    add_form = UserRegistrationForm
    list_display = ('username',)
    fieldsets = (  
        *BaseUserAdmin.fieldsets,
        ('Дополнительная информация',
         {'fields': ('telegram_id', 'is_telegram_bot')}
         ),
    )
    add_fieldsets = (  
        *BaseUserAdmin.add_fieldsets,
        ('Дополнительная информация',
         {'fields': ('telegram_id',)}
         ),
    )
    empty_value_display = '-пусто-'

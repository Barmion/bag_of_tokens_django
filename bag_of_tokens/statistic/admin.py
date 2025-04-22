from django.contrib import admin

from .models import Statistic_1, Statistic_2

@admin.register(Statistic_1)
class Statistic_1Admin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'token',)
    search_fields = ('owner',)
    list_filter = ('owner',)

@admin.register(Statistic_2)
class Statistic_2Admin(admin.ModelAdmin):
    pass

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Bag, Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'char', 'sticker_id', 'ordering', 'icon_tag')
    list_editable = ('ordering',)
    readonly_fields = ('icon_tag',)
    empty_value_display = '-пусто-'

    def icon_tag(self, obj):
        return mark_safe(f'<img src="{obj.image.url}">')


@admin.register(Bag)
class BagAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'token',)
    list_editable = ('owner', 'token',)
    search_fields = ('owner',)
    list_filter = ('owner',)
    empty_value_display = '-пусто-'

from django.contrib import admin
from home.models import TelegramUser


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'username', 'site_user')
    list_filter = ('name', 'username')
    list_editable = ('name', 'username', 'site_user')
    search_fields = ('username',)


admin.site.register(TelegramUser, TelegramUserAdmin)

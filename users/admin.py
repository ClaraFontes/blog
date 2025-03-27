from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome','telefone']
    list_display_links = ['nome']
    search_fields = ['id']
    
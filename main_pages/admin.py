from django.contrib import admin
from .models.main_pages import Pages

@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
  list_display = ('title', 'detail',)
  search_fields = ('title', 'detail',)

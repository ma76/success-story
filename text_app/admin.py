from django.contrib import admin
from .text_model import TextModel,TextCategoryModel

# Extend Models-Admin
class TextAdmin(admin.ModelAdmin):
    list_display = ['id']
    class Meta:
        model = TextModel

class TextCategoryAdmin(admin.ModelAdmin):
    list_display = ['title','is_gold']

    class Meta:
        model = TextCategoryModel


# Register your models here.
admin.site.register(TextModel,TextAdmin)
admin.site.register(TextCategoryModel,TextCategoryAdmin)
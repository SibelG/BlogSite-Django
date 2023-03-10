from django.contrib import admin
from .models import Blog,Category
from django.utils.safestring import mark_safe
# from post.models import Post
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","selected_categories",)
    list_editable = ("is_home","is_active",)
    search_fields = ("title","description")
    list_filter = ("is_active","is_home","categories",)

    def selected_categories(self,obj):
        html = "<ul>"

        for category in obj.categories.all():
            html += "<li>" + category.name + "</li>"

        html +="</ul>"
        return mark_safe(html)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)

from django.contrib import admin
from film_site.models import Category, Page, Film,Review
from film_site.models import UserProfile


# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'film', 'rating', 'reviewtext')

# class FilmAdmin(admin.ModelAdmin):
#   list_display = ('title', 'category', 'url')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(Film)
admin.site.register(Review,ReviewAdmin)
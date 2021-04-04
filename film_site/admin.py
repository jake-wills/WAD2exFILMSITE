from django.contrib import admin
from film_site.models import Category, Film, Review
from film_site.models import UserProfile


# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'film', 'rating', 'reviewtext','review_time')

admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Film)
admin.site.register(Review,ReviewAdmin)
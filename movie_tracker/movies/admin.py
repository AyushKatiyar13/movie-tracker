from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'created_at', 'description']
    search_fields = ['title']
    list_filter = ['release_date']

admin.site.register(Movie, MovieAdmin)

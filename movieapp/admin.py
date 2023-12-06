from django.contrib import admin
from movieapp.models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['movie_name','actor','actress','rating','release_date']
admin.site.register(Movie,MovieAdmin)

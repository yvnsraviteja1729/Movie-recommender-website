from django.contrib import admin
from recommend_all.models import signup,watched,movie_comment,Rating
# Register your models here.
admin.site.register(signup)
admin.site.register(watched)
admin.site.register(Rating)
admin.site.register(movie_comment)
# admin.site.register(check)

from django.contrib import admin
from .models import Post

# Registering our model with the Admin Interface
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_date')     # To display the these fields in the admin interface
    ordering = ('created_date',)                                # Sorting them with date
#    search_fields = ('title', 'created_date')


# admin.site.register(Post)

from django.contrib import admin
from game.models import Reklama, Restaurant1


@admin.register(Restaurant1)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['title', 'categories1', 'user',
                     ]
    search_fields = ['title']
    list_filter = ['user', 'created_at']
    list_per_page = 20
    date_hierarchy = 'created_at'


admin.site.register(Reklama)
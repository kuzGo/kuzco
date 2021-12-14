
from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'watches',
        'created',
        'updated',
        'title',
        'review',
    )


admin.site.register(Review, ReviewAdmin)

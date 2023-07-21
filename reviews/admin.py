"""from django.contrib import admin
from .models import PostReviewType, PostReview, ReviewResponse


@admin.register(PostReviewType)
class PostReviewTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )
    prepopulated_fields = {'name': ('friendly_name',)}


@admin.register(PostReview)
class PostReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug', 
        'postreview_type',
        'create_date',
    )
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ReviewResponse)
class ReviewResponseAdmin(admin.ModelAdmin):
    list_display = (
        'postreview',
        'author',
        'create_date',
        'approved',
    )
"""

from django.contrib import admin
from .models import Review


@admin.register(Review)
class Review(admin.ModelAdmin):
    """
    Displays the fields for the Review model
    """
    list_display = ('user', 'product', 'review', 'created_on')
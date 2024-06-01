from django.contrib import admin
from photogallery.models import Trip, Photo, Post


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 5

class PostInline(admin.TabularInline):
    model = Post
    extra = 1

class TripAdmin(admin.ModelAdmin):
    list_display = ('city', 'country', 'continent', 'date', 'cover')
    list_filter = ('continent',)
    search_fields = ('city', 'country', 'date')

    fieldsets = (
        ('Location', {
            'fields': ('city', 'country', 'continent')
        }),
        ('Details', {
            'fields': ('date', 'cover')
        })
    )
    inlines = [PhotoInline]
    

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('trip', 'title', 'description', 'photo')
    list_filter = ('trip',)
    search_fields = ('trip__city', 'trip__country', 'title', 'description')
    list_editable = ('title',)

    fieldsets = (
        ('Trip', {
            'fields': ('trip',)
        }),
        ('Photo details:', {
            'fields': ('title', 'description','photo')
        })
    )
    inlines = [PostInline]


class PostAdmin(admin.ModelAdmin):
    list_display = ('user','photo', 'comment', 'reaction')
    list_filter = ('user', 'reaction')
    search_fields = ('trip__city', 'trip__country', 'post_photo', 'user', 'reaction')
    
    fieldsets = (
        ('Photo details:', {
            'fields': ( 'photo',)
        }),
        ('User post:', {
            'fields': ( 'user', 'comment', 'reaction' )

        })
    )

admin.site.register(Trip, TripAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Post, PostAdmin)



from django.contrib import admin


class WallpaperAdmin(admin.ModelAdmin):
    list_display = ["thumbnail", "title", "image", "published"]
    list_editable = ["published"]
    list_filter = ["published"]
    list_display_links = ["thumbnail", "title"]

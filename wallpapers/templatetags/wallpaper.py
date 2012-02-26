from random import choice
from django import template

from wallpapers.models import Wallpaper

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_wallpapers(context):
    return Wallpaper.published_objects.all()


@register.assignment_tag(takes_context=True)
def get_wallpaper(context, pk):
    try:
        return Wallpaper.published_objects.get(pk=pk)
    except DoesNotExist:
        return None


@register.assignment_tag(takes_context=True)
def random_wallpaper(context):
    wallpapers = Wallpaper.published_objects.all()
    try:
        return choice(wallpapers)
    except IndexError:
        return None

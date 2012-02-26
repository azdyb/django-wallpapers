from django.db import models
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail import ImageField, default


class PublishedWallpapersManager(models.Manager):
    def get_query_set(self):
        return super(PublishedWallpapersManager, self) \
        .get_query_set().filter(published=True)


class Wallpaper(models.Model):
    title = models.CharField(_("Title"), max_length=30)
    image = ImageField(_("Image"), upload_to="wallpapers")
    published = models.BooleanField(_("Published"), default=True)

    objects = models.Manager()
    published_objects = PublishedWallpapersManager()

    def __unicode__(self):
        return "%(title)s (%(filename)s)" % {"title": self.title,
                                             "filename": self.image}

    def thumbnail(self):
        if self.image:
            thumb = default.backend.get_thumbnail(self.image, "250x200")
            html = "<img title=\"%s\" alt=\"%s\" src=\"%s\" />" % \
            (self.title, self.title, thumb.url, )
        else:
            return "(None)"
        return html
    thumbnail.allow_tags = True

What is django-wallpapers?
==========================

Django-wallpapers is an django application, which helps managing backgrounds for webpages.

It has an `admin interface`_ allowing to add and manage images used as backgrounds.


Usage
=====

After adding some wallpapers via an `admin interface`_, one can use them in their templates with help of one of three templatetags:

* get_wallpapers – returns all wallpapers marked as published
* get_wallpaper – returns wallpaper indicated by it's primary key
* random_wallpaper – returns random wallpaper of the published ones

The sample usage in template may look as follows::

    {% load wallpaper %}

    ...

    {% random_wallpaper as wallpaper %}
    {% if wallpaper %}
    <style type="text/css">
        body {
            background-image: url({% get_media_prefix %}{{ wallpaper.image }});
        }
    </style>
    {% endif %}


.. _admin interface:

What it looks like?
===================

Everybody loves screenshots, right?

Wallpaper changelist:

.. image:: http://img687.imageshack.us/img687/613/selectwallpapertochange.png
  :alt: Select wallpaper to change


Installation
============

Django-wallpapers is installed just like any other Django application:

1. Put *wallpapers* directory in any path, where python can find it
2. Add *wallpapers* to ``INSTALLED_APPS`` in settings.py
3. Run ```manage.py syncdb``` to create database tables for wallpapers
4. Register ModelAdmin classes found in ``wallpapers/admin.py`` file in you admin site


License
=======

Copyright 2012 Aleksander Zdyb

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see http://www.gnu.org/licenses/.

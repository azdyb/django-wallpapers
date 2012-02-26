from distutils.core import setup
setup(name="django-wallpapers",
      version="0.1.0",
      author="Aleksander Zdyb",
      author_email="azdyb@live.com",
      description="An django application, which helps managing backgrounds"
                    "for webpages",
      long_description=open("README.rst").read(),
      license="GPL",
      url="http://github.com/ojo/django-wallpapers",
      packages=["wallpapers", "wallpapers.templatetags"])

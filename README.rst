=========
pika-flix
=========

pika-flix is a Django web app to enable users share videos
about cooking, food & hotel reviews.


Quick start
-----------

1. Add "pikaflix" to your INSTALLED_APPS setting:

   INSTALLED_APPS = [
        ...,
        "pikaflix",
    ]

2. Include the pikaflix URLconf in your project urls.py:

   path("pikaflix/", include("pikaflix.urls")),

3. Run ``python3 manage.py migrate`` to create models.

4. Start the development server and visit the admin to create a video.

5. Visit the ``/home/`` URL to see how it works.

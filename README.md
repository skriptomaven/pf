#### pika-flix

pika-flix is a Django web app to enable users share videos
about cooking, food & hotel reviews.

![image](https://github.com/skriptomaven/pf/assets/123072803/1b96b949-c440-4f27-bd97-63be52e1279f)


#### Quick start

1. Add "pikaflix" to your INSTALLED_APPS setting:

   ``INSTALLED_APPS = [``
        ``...,``
        ``"pf",``
    ``]``

2. Include the pikaflix URLconf in your project urls.py:

   ``path("pikaflix/", include("pikaflix.urls")),``

3. Run ``python3 manage.py migrate`` to create models.

4. Start the development server and visit the admin to create a video.

5. Visit the ``/home/`` URL to see how it works.

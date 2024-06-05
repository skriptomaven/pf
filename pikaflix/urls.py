from django.contrib import admin
from django.urls import path


from pf.views import home_view, login_view, signup_view


urlpatterns = [
    path('', home_view, name='home_view'),
    path('login/', login_view, name='login_view'),
    path('signup/', signup_view, name='signup_view'),
    path('admin/', admin.site.urls),
]

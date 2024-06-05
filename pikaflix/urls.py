from django.contrib import admin
from django.urls import path


from pf.views import home, login, signup


urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path


from pf.views import home, login, signup, logout, video


urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('video/', video, name='video'),
    path('admin/', admin.site.urls),
]

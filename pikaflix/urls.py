from django.contrib import admin
from django.urls import path


from pf.views import home, login, signup, logout, upload_video


urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('upload_video/', upload_video, name='upload_video'),
    path('admin/', admin.site.urls),
]

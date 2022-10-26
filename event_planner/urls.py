"""event_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from planner.views import get_home
from users.views import create_event, register_user, login_user, logout_user, get_events, get_event_detail, create_reservation
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", get_home, name="home" ), 
    path("register/", register_user, name="register" ), 
    path("login/", login_user, name="login" ), 
    path("signin/", login_user, name="signin" ), 
    path("logout/", logout_user, name="logout" ), 
    path("events/", get_events, name="events-list" ), 
    path("events/<int:event_id>/", get_event_detail, name="event-detail" ), 
    path("events/<int:event_id>/reserve/", create_reservation, name="reserve" ), 
    path("events/create", create_event, name="create-event"), 
    # path("reserve/<int:event_id>/", create_reservation, name="quick-reserve" ), 
    

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from lettings.views import letting, index as lettings_index
from profiles.views import profile, index as profiles_index


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting, name='letting'),
    path('profiles/', profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profile, name='profile'),
    path('admin/', admin.site.urls),
    path('sentry-debug/', views.trigger_error, name='error_testing'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path, re_path

from dj_favorite_wrap.admin_favorite.views import get_district

app_name = 'inventory'

urlpatterns = [
    re_path('favorite', get_district, name='get_district'),

]

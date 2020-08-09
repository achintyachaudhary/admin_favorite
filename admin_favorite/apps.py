from django.apps import AppConfig
from django.conf import settings


class AdminFavoriteConfig(AppConfig):
    name = 'admin_favorite'
    verbose_name = settings.ADMIN_FAVORITE if hasattr(settings, 'ADMIN_FAVORITE') else 'Favorite'

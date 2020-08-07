from django.contrib.contenttypes.models import ContentType
from django.db import models


class Favorite(models.Model):
    model = models.ForeignKey(to=ContentType, db_column="fm_entity_id", verbose_name="Entity Type",
                              on_delete=models.CASCADE)
    priority = models.IntegerField(default=1)

from django.db import models


class Africa(models.Model):
    class Meta:
        verbose_name = 'Africa'
        verbose_name_plural = 'Africa'


class Antarctica(models.Model):
    class Meta:
        verbose_name = 'Antarctica'
        verbose_name_plural = 'Antarctica'


class Asia(models.Model):
    class Meta:
        verbose_name = 'Asia'
        verbose_name_plural = 'Asia'


class Australia(models.Model):
    class Meta:
        verbose_name = 'Australia'
        verbose_name_plural = 'Australia'


class Europe(models.Model):
    class Meta:
        verbose_name = 'Europe'
        verbose_name_plural = 'Europe'


class NorthAmerica(models.Model):
    class Meta:
        verbose_name = 'North America'
        verbose_name_plural = 'North America'


class SouthAmerica(models.Model):
    class Meta:
        verbose_name = 'South America'
        verbose_name_plural = 'South America'

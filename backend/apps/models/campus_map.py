from django.db import models
from django.contrib.gis.db import models as gis_models

class University(models.Model):
    name = models.Charfield(max_length=100)
    track = gis_models.PolygonField(srid=3857)

    def __str__(self):
        return self.name


class Pathway(models.Model):
    path = gis_models.LineStringField(srid=4326)

    def __str__(self):
        return f"Pathway {self.id}"


class DeliveryPoint(models.Model):
    name = models.Charfield(max_length=100)
    location = gis_models.PointField(srid=4326)

    def __str__(self):
        return self.name
from django.db import models


class Service(models.Model):
    """A service registry for the services in the cluster."""

    name        = models.CharField(max_length=32)
    service_url = models.URLField(max_length=256, unique=True)
    active      = models.BooleanField(default=True)
    manage_dir  = models.CharField(max_length=256, unique=True)
    virtual_env = models.CharField(max_length=256, null=True, blank=True)


from django.db import models

# Create your models here.

class Zone(models.Model):
    zone_name = models.CharField(max_length=100, blank=True)

class Asset(models.Model):
    instance_id = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    pub_ip = models.CharField(max_length=100, blank=True, null=True)
    priv_ip = models.CharField(max_length=100, blank=True, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    is_public = models.BooleanField(null=True)
    sgId = models.CharField(max_length=100, blank=True)
    hash = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.instance_id

    objects = models.Manager()


class SGT(models.Model):
    sg_id = models.CharField(max_length=100, blank=True, null=True)

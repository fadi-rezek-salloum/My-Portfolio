from django.db import models

class CV(models.Model):
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.link
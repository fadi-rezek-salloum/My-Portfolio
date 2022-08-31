from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    thumbnail = models.ImageField(upload_to='projects/', blank=True)
    slug = models.SlugField(unique=True, max_length=200, blank=True)

    website_url = models.URLField(null=True, blank=True)

    tags = TaggableManager()

    views = models.PositiveIntegerField(default=0)

    created = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse("projects:details", kwargs={"slug": self.slug})

    def get_tags(self):
        return self.tags.all()

    def get_views(self):
        return self.views
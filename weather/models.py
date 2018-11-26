from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class City(models.Model):
    class Meta:
        verbose_name_plural = "cities"
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    rus_name = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('weather:weather_detail', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

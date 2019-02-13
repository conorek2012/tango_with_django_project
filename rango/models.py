from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = models.URLField(help_text="Please enter the URL of the page.")
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
        # For Python 2, use __unicode__ too

# Create your models here.

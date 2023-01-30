from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    #category = models.ForeignKey(Category, null=True, default=1, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True)
    def __str__(self):
        return f"{self.title}"





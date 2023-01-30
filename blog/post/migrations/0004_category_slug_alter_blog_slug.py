# Generated by Django 4.1.5 on 2023-01-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0003_blog_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
    ]

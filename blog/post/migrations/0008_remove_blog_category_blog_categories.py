# Generated by Django 4.1.5 on 2023-01-27 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0007_blog_category"),
    ]

    operations = [
        migrations.RemoveField(model_name="blog", name="category",),
        migrations.AddField(
            model_name="blog",
            name="categories",
            field=models.ManyToManyField(to="post.category"),
        ),
    ]

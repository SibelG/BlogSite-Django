# Generated by Django 4.1.5 on 2023-01-26 13:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0005_remove_blog_slug_remove_category_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
    ]

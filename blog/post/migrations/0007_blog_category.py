# Generated by Django 4.1.5 on 2023-01-26 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0006_alter_blog_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="category",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="post.category",
            ),
        ),
    ]
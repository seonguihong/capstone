# Generated by Django 5.0.6 on 2024-05-14 14:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chatbot", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lostitem",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="lost_items/", verbose_name="Image"
            ),
        ),
    ]
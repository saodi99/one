# Generated by Django 4.1.7 on 2023-04-15 09:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("APP1", "0005_alter_passwrd_uid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avater",
            field=models.ImageField(default="", max_length=255, upload_to="img"),
        ),
        migrations.AlterField(
            model_name="user",
            name="message",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]

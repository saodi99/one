# Generated by Django 4.1.7 on 2023-04-30 10:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("APP1", "0011_alter_goods_transaction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avater",
            field=models.ImageField(
                default="img/my.jpg", max_length=255, upload_to="img"
            ),
        ),
    ]
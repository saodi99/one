# Generated by Django 4.1.7 on 2023-04-13 02:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("APP1", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="user",
            name="sex",
            field=models.CharField(
                choices=[("male", "男"), ("female", "女")], default="未知", max_length=32
            ),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-15 02:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("APP1", "0002_alter_user_email_alter_user_sex"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avater",
            field=models.ImageField(default=1, max_length=256, upload_to="img"),
            preserve_default=False,
        ),
    ]

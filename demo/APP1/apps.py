from django.apps import AppConfig


class App1Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "APP1"
    verbose_name = '数据管理'
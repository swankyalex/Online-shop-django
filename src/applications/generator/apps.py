from django.apps import AppConfig


class GeneratorConfig(AppConfig):
    label = "generator"
    name = f"applications.{label}"

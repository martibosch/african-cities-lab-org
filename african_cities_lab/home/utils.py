from typing import Any

from django.apps import AppConfig
from django.conf import settings
from django.contrib.contenttypes.models import ContentType as RealContentType
from django.db import models
from treebeard.mp_tree import MP_Node
from wagtail.core import models as core_models
from wagtail.core.utils import get_supported_content_language_variant


class WagtailTreeMigrator:
    def __init__(self, apps: AppConfig):
        self.apps = apps

    def model(self, name: str) -> type[models.Model]:
        return self.apps.get_model(name)

    def content_type(self, model: type[models.Model]):
        ct = self.model("contenttypes.ContentType").objects.get_for_model(model)
        inject_base(ct, RealContentType)
        return ct

    def locale(self, language_code: str) -> core_models.Locale:
        return self.model("wagtailcore.Locale").objects.get(
            language_code=get_supported_content_language_variant(language_code)
        )

    def default_locale(self) -> core_models.Locale:
        return self.locale(settings.LANGUAGE_CODE)

    def site(self, is_default_site: bool = True, **kwargs) -> core_models.Site:
        return self.model("wagtailcore.Site").objects.get(
            is_default_site=is_default_site, **kwargs
        )

    def create_page(
        self, parent: core_models.Page, model: str, kwargs: dict[str, Any]
    ) -> core_models.Page:
        cls = self.model(model)
        inject_base(parent, MP_Node)

        defaults = dict(
            content_type=self.content_type(cls),
            locale=self.default_locale(),
        )
        page = cls(**{**defaults, **kwargs})

        parent.add_child(instance=page)

        return page  # noqa


def inject_base(obj, cls):
    if cls not in obj.__class__.__bases__:
        obj.__class__.__bases__ = (cls,) + obj.__class__.__bases__

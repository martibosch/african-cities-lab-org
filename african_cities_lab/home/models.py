from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

from african_cities_lab.home.blocks import OneColumnBlock


class HomePage(Page):
    subpage_types = [
        "home.FlatPage",
    ]
    parent_page_type = [
        "wagtailcore.Page",
    ]
    max_count = 1

    body = StreamField([("one_column_block", OneColumnBlock())], blank=True)

    content_panels = Page.content_panels + [FieldPanel("body")]


class FlatPage(Page):
    """FlatPage page model."""

    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
    parent_page_type = [
        "home.HomePage",
    ]

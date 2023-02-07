from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class HomePage(Page):
    subpage_types = [
        "home.FlatPage",
    ]
    parent_page_type = [
        "wagtailcore.Page",
    ]
    max_count = 1


class FlatPage(Page):
    """FlatPage page model."""

    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
    parent_page_type = [
        "home.HomePage",
    ]

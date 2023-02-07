from django import template
from wagtail.core.models import Locale, Page, Site
from wagtail.core.templatetags.wagtailcore_tags import pageurl

register = template.Library()


@register.simple_tag(takes_context=True)
def redirect_to(context, slug):
    if slug is None or slug == "":
        return ""
    english = Locale.get_default()
    current_lang = Locale.get_active()
    french = Locale.objects.get_for_language("fr")
    if current_lang == english:
        lang = english
        target_lang = french
    else:
        lang = french
        target_lang = english
    current_page = Page.objects.filter(locale=lang, slug=slug).first()
    page = Page.objects.filter(
        locale=target_lang, translation_key=current_page.translation_key
    ).first()
    url = ""
    if page:
        url = page.url
    return url


@register.simple_tag(takes_context=True)
def localized_slugurl(context, slug):
    """
    Localized slugurl.

    Extends `slugurl`so that given the slug in the default language, get the page in the
    current active language.
    """
    page = None

    english = Locale.get_default()
    try:
        site = Site.find_for_request(context["request"])
        current_site = site
    except KeyError:
        # No site object found - allow the fallback below to take place.
        pass
    else:
        if current_site is not None:
            # TODO: use `.filter(locale=english).filter(slug=slug)`?
            page = (
                Page.objects.in_site(current_site)
                .filter(locale=english, slug=slug)
                .first()
            )

    # If no page is found, fall back to searching the whole tree.
    if page is None:
        page = Page.objects.filter(locale=english, slug=slug).first()

    if page:
        # call pageurl() instead of page.relative_url() here so we get the
        # `accepts_kwarg` logic
        return pageurl(context, page.localized)

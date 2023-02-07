from wagtail.tests.utils import WagtailPageTests

from african_cities_lab.home.models import FlatPage, HomePage


class FlatPageTests(WagtailPageTests):
    def test_can_create_a_page(self):
        self.assertCanCreateAt(HomePage, FlatPage)

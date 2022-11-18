from django.test import TestCase
from django.urls import reverse
from products.models import Product


class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse("products:index")
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data["title"], "Store")
        self.assertTemplateUsed(response, "products/index.html")


class ProductsListViewTestCase(TestCase):
    fixtures = ["categories.json", "goods.json"]

    def test_list(self):
        path = reverse("products:products")
        response = self.client.get(path)

        products = Product.objects.all()[:3]
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")
        self.assertEqual(response.context_data["title"], "Store - Каталог")
        self.assertEqual(list(response.context_data["object_list"]), list(products))

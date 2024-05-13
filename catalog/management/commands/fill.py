from django.core.management import BaseCommand

from catalog.function.fixture import open_fixture
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        file = open_fixture('catalog.json')
        list_categories = [item.get("fields") for item in file if item.get("model") == "catalog.category"]
        return list_categories

    @staticmethod
    def json_read_products():
        file = open_fixture('catalog.json')
        list_products = [item.get("fields") for item in file if item.get("model") == "catalog.product"]
        return list_products


    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_for_create = [Category(**item) for item in self.json_read_categories()]
        product_for_create = []

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product.get("name"),
                        price=product.get("price"),
                        preview=product.get("preview"),
                        created_at=product.get("created_at"),
                        updated_at=product.get("updated_at"),
                        description=product.get("description"),
                        category=Category.objects.get(pk=product.get("category") + 3))
            )

            print(product.get("category"))


        Product.objects.bulk_create(product_for_create)
from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_existed(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="Barang 1", amount=999, type="New", description="Ini deskripsi barang 1")
    
    def test_get_object(self):
        get_obj1 = Item.objects.get(name="Barang 1")
        self.assertEqual(get_obj1.description, "Ini deskripsi barang 1")
    
    def test_update_object(self):
        update_obj1 = Item.objects.get(name="Barang 1")
        update_obj1.description = "Ini deskripsi barang 1 updated 2.0"
        update_obj1.save()

        updated_obj = Item.objects.get(name="Barang 1")
        self.assertEqual(updated_obj.description, "Ini deskripsi barang 1 updated 2.0")
    
    def test_delete_object(self):
        del_obj1 = Item.objects.get(name="Barang 1")
        del_obj1.delete()
        with self.assertRaises(Item.DoesNotExist): Item.objects.get(name="Barang 1")
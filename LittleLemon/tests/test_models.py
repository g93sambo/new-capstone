from django.test import TestCase
from Restaurant.models import Menu
from django.urls import reverse
class MenuItemTest(TestCase):
     def test_get_item(self):
         item = Menu.objects.create(Title="IceCream", price=80, inventory=100)
         self.assertEqual(item, "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        self.menu1 = Menu.objects.create(Title="IceCream", price=80, inventory=100)
        self.menu2 = Menu.objects.create(Title="IceCream", price=80, inventory=100)
        self.menu3 = Menu.objects.create(Title="IceCream", price=80, inventory=100)

    def test_getall(self):
        # Retrieve all Menu objects added for the test purpose
        url = reverse('menu-list')  # Replace 'menu-list' with your actual URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200 (OK)

        # Serialize the retrieved data (assuming you're using Django Rest Framework)
        serialized_data = response.data  # Assuming you're using DRF and response.data contains the serialized data
        
        
        expected_data = [
            {
                
              "Title":"IceCream",
                "price":"80", 
                "inventory":"100"
            },
            {
               
                "Title":"IceCream",
                "price":"80", 
                "inventory":"100"
            },
            {
                
                "Title":"IceCream",
                "price":"80", 
                "inventory":"100"
            },
        ]

        self.assertEqual(serialized_data, expected_data)
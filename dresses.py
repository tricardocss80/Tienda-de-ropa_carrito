#Dado el sitio automationpractise.com
#Caso 1:
#-El usuario ingresa en la sección Dresses 0k
#-Selecciona Casual Dresses                0k
#-Selecciona el vestido que aparece.       0k
#-Selecciona 5 vestidos de tamaño L.       0k
#-Presiona Add To cart                     0k
#-Debe verificar:
# --Que hay 5 elementos en el carrito      0k
#--El precio                               0k
#--El precio de envío                      0k
#--El precio total                         0k
#--El nombre del producto                  0k
#Caso 2:
#-El usuario ingresa en la sección Dresses       0k
#-Ordena los vestidos por precio "Lowest First"  0k/ error 403
#-Cambia la vista a List
#-Agrega al carrito el segundo vestido
#-Debe verificar:
#--El precio
#--El precio de envío
#--El precio total
#--El nombre del producto

import unittest
from selenium import webdriver
from automation_practice.pageindex import PageIndex
from automation_practice.pagedresses import PageDresses
from automation_practice.pagecasualdresses import PageCasualDresses
from automation_practice.pageprinteddresses import PagePrintedDresses
from automation_practice.pagecart import PageCart


class DressesCaseSuite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('automation_practice/chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.IndexPage = PageIndex(self.driver)
        self.DressesPage = PageDresses(self.driver)
        self.CasualDressesPage = PageCasualDresses(self.driver)
        self.PrintedDressesPage = PagePrintedDresses(self.driver)
        self.CartPage = PageCart(self.driver)

    def test01_clothing_store_checks(self):
        self.IndexPage.enter_dresses_section()
        self.DressesPage.select_casual_dresses()
        self.CasualDressesPage.select_dress()
        self.IndexPage.wait_loading()
        unit_price = self.PrintedDressesPage.price_product()
        self.PrintedDressesPage.add_dresses(4)
        self.PrintedDressesPage.selects_size('3')
        self.PrintedDressesPage.click_add_to_card()
        self.IndexPage.wait_layer_cart()
        #operations
        quantity_product = self.CartPage.checks_quantity_products()
        total_price_products = unit_price * quantity_product
        price_shipping = self.CartPage.checks_shipping()
        total_cart_price = total_price_products + price_shipping
        #verifications
        self.assertEqual(self.CartPage.checks_product_name(), 'Printed Dress')
        self.assertEqual(self.CartPage.checks_quantity_products(), 5)
        self.assertEqual(self.CartPage.checks_total_price_products(), total_price_products)
        self.assertEqual(self.CartPage.checks_shipping(), 2.0)
        self.assertEqual(self.CartPage.check_total_cart_price(), total_cart_price)

    def test02_clothing_store_checks(self):
        self.IndexPage.enter_dresses_section()
        self.DressesPage.select_by_price(2)
        self.DressesPage.list_view()
        #self.IndexPage.wait_loading()
        #self.PrintedDressesPage.add_dresses(4)
        #self.PrintedDressesPage.selects_size('3')
        #self.PrintedDressesPage.click_add_to_card()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
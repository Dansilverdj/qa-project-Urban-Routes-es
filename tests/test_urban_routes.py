import time
from data import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages import urban_routes_page as urp
from utils import retrive_code
from selenium.webdriver.common.keys import Keys

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs",{"performance": "ALL"})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = urp.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test2_select_comfort(self): #Selecciona la tarifa Comfort y aserta que quede activa
        self.routes_page.click_on_order_taxi_button()
        self.routes_page.select_comfort_fee()
        assert self.routes_page.get_comfort_title().text == "Comfort"

    def test3_phone_number(self): #Ingresa el número de teléfono, valida el formateo
        self.routes_page.click_phone_on()
        self.routes_page.set_phone(data.phone_number)
        #assert (self.routes_page.get_phone()('value') == '+1 123 123 12 12')
        self.routes_page.click_following_button()
        self.routes_page.set_phone_code(retrive_code.retrieve_phone_code(self.driver))
        self.routes_page.click_confirm_button()
        assert not self.routes_page.is_confirm_button_visible(), "El botón 'Agregar' sigue visible tras hacer clic"


    def test4_add_card(self): #Abre el modal de tarjeta, ingresa número y CVV, un TAB para habilitar
        self.routes_page.click_pay_clic()
        self.routes_page.click_add_card()
        self.routes_page.set_number_card()
        assert (self.routes_page.get_number_card().get_property('value') == '1234 5678 9100')
        self.routes_page.set_code_card(self.driver)
        assert (self.routes_page.get_code_card().get_property('value') == '111')
        self.routes_page.get_code_card().send_keys(Keys.TAB)
        self.routes_page.click_confirmation_button()
        self.routes_page.click_close_pay()


    def test5_send_message_to_driver(self): #Escribe y valida el mensaje para el conductor
        self.routes_page.click_massage_send()
        self.routes_page.set_write_message()
        assert (self.routes_page.get_write_message().get_property('value')) == 'Muéstrame el museo'

    def test6_add_blanket(self): #Activa el toggle de manta y pañuelos valida su estado
        self.routes_page.click_switch_blanket()
        assert (self.routes_page.switch_blanket_checked(), 'El switch no paso')

    def test7_two_ice_cream(self): #Pide dos helados y valida que el contador refleje 2
        self.routes_page.click_ice_cream()
        assert (self.routes_page.get_ice_cream().get_property('value')) != 2

    def test8_take_taxi(self): #Solicita el taxi, espera el modal de búsqueda y opcionalmente valida información del conductor
        self.routes_page.click_take_taxi()

        time.sleep(10)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
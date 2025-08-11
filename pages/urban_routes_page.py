from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data import data


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_fee = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')
    phone_on = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')
    phone_clic = (By.XPATH, '//*[@id="phone"]')
    phone_number = (By.ID, 'phone')
    following_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    phone_code = (By.ID, 'code')
    confirm_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    pay_clic = (By.CSS_SELECTOR, '.pp-button')
    add_card = (By.CSS_SELECTOR, '.pp-plus-container')
    number_card = (By.ID, 'number')
    code_card = (By.NAME, 'code')
    confirmation_button = (By.XPATH, "//div[@class='pp-buttons']/button[text()='Agregar']")
    close_pay = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    message_send = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[3]/div/label')
    write_message = (By.ID, 'comment')
    switch_blanket = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    ice_cream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    take_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button/span[1]')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def set_from(self, from_address):
        # self.driver.find_element(*self.from_field).send_keys(from_address)
        self.wait.until(ec.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        # self.driver.find_element(*self.to_field).send_keys(to_address)
        self.wait.until(ec.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_order_taxi_button(self):
        return self.wait.until(ec.element_to_be_clickable(self.order_taxi_button))

    def click_on_order_taxi_button(self):
        self.get_order_taxi_button().click()

    def get_comfort_fee(self):
        return self.wait.until(ec.element_to_be_clickable(self.comfort_fee))

    def get_comfort_title(self):
        return self.driver.find_element(By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')

    def select_comfort_fee(self):
        self.get_comfort_fee().click()

    def get_phone_on(self):
        return self.wait.until(ec.element_to_be_clickable(self.phone_on))

    def click_phone_on(self):
        self.get_phone_on().click()

    def get_phone_clic(self):
        return self.wait.until(ec.element_to_be_clickable(self.phone_clic))

    def get_phone(self):
        return self.wait.until(ec.presence_of_element_located(self.phone_number))

    def set_phone(self, phone_number):
        self.get_phone().send_keys(phone_number)

    def get_following_button(self):
        return self.wait.until(ec.element_to_be_clickable(self.following_button))

    def click_following_button(self):
        self.get_following_button().click()

    def get_phone_code(self):
        return self.wait.until(ec.presence_of_element_located(self.phone_code))

    def set_phone_code(self, phone_code):
        self.get_phone_code().send_keys(phone_code)

    def get_confirm_button(self):
        return self.wait.until(ec.element_to_be_clickable(self.confirm_button))

    def click_confirm_button(self):
        self.get_confirm_button().click()

    def is_confirm_button_visible(self):
        try:
            return self.get_confirm_button().is_displayed()
        except:
            return False  # Si lanza excepción, asumimos que desapareció

    def get_pay_clic(self):
        return self.wait.until(ec.element_to_be_clickable(self.pay_clic))

    def click_pay_clic(self):
        self.get_pay_clic().click()

    def get_add_card(self):
        return self.wait.until(ec.element_to_be_clickable(self.add_card))

    def click_add_card(self):
        self.get_add_card().click()

    def get_number_card(self):
        return self.wait.until(ec.presence_of_element_located(self.number_card))

    def set_number_card(self):
        self.get_number_card().send_keys(data.card_number)

    def get_code_card(self):
        return self.wait.until(ec.presence_of_element_located(self.code_card))

    def set_code_card(self, driver):
        self.get_code_card().send_keys(data.card_code)

    def get_confirmation_button(self):
        return self.wait.until(ec.element_to_be_clickable(self.confirmation_button))

    def click_confirmation_button(self):
        self.get_confirmation_button().click()

    def get_close_pay(self):
        return self.wait.until(ec.element_to_be_clickable(self.close_pay))

    def click_close_pay(self):
        self.get_close_pay().click()

    def get_massage_send(self):
        return self.wait.until(ec.element_to_be_clickable(self.message_send))

    def click_massage_send(self):
        self.get_massage_send().click()

    def get_write_message(self):
        return self.wait.until(ec.presence_of_element_located(self.write_message))

    def set_write_message(self):
        self.get_write_message().send_keys(data.message_for_driver)

    def get_switch_blanket(self):
        return self.wait.until(ec.element_to_be_clickable(self.switch_blanket))

    def click_switch_blanket(self):
        self.get_switch_blanket().click()

    def switch_blanket_checked(self):
        return self.get_switch_blanket().is_selected()

    def get_ice_cream(self):
        return self.wait.until(ec.element_to_be_clickable(self.ice_cream))

    def click_ice_cream(self):
        self.get_ice_cream().click()
        self.get_ice_cream().click()

    def get_take_taxi(self):
        return self.wait.until(ec.element_to_be_clickable(self.take_taxi))

    def click_take_taxi(self):
        self.get_take_taxi().click()

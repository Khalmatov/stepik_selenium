import math
import re

import pyperclip
from selenium.common.exceptions import NoAlertPresentException

from stepik_selenium.pages.base_page import BasePage
from stepik_selenium.pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_btn_add_to_basket(self):
        """Проверяет наличие кнопки добавления продукта в корзину"""
        assert self.is_element_present(
            *ProductPageLocators.BTN_ADD_TO_BASKET), "Кнопка добавления товара в корзину отсутствует"

    def add_to_basket(self):
        """Добавляет продукт в корзину"""
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()

    def should_be_name(self):
        """Проверяет наличие название продукта"""
        assert self.is_element_present(*ProductPageLocators.NAME), 'Отсутствует название продукта'

    def get_product_name(self):
        """Возвращает название продукта"""
        return self.browser.find_element(*ProductPageLocators.NAME).text

    def should_be_price(self):
        """Проверяет наличие цены продукта"""
        assert self.is_element_present(*ProductPageLocators.PRICE), 'Отсутствует цена продукта'

    def get_product_price(self):
        """Возвращает цену товара"""
        msg = self.browser.find_element(*ProductPageLocators.PRICE).text
        return float(re.search(r'\d{2}[.,]\d{2}', msg).group(0).replace(',', '.')) if msg else 0

    def should_be_basket_mini(self):
        """Проверяет наличие суммы цен товаров, добавленных в корзину"""
        return self.is_element_present(
            *ProductPageLocators.BASKET_MINI), 'Отсутствует сумма цен товаров, добавленных в корзину'

    def get_total_price(self):
        """Возвращает сумму цен товаров, добавленных в корзину"""
        msg = self.browser.find_element(*ProductPageLocators.BASKET_MINI).text
        return float(re.search(r'\d{2}[.,]\d{2}', msg).group(0).replace(',', '.')) if msg else None if msg else 0

    def should_be_msg_product_added_to_basket(self):
        """Проверяет наличие сообщения об успешном добавлении товара в корзину"""
        return self.is_element_present(
            *ProductPageLocators.PRODUCT_WAS_ADDED_TO_BASKET), 'Отсутствует сообщение об успешном добавлении товара в корзину'

    def get_name_of_product_was_added_to_basket(self):
        """Возвращает название продукта, который был добавлен в корзину"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_WAS_ADDED_TO_BASKET).text

    def should_product_added_to_basket(self):
        """Проверяет, добавлен ли текущий продукт в корзину"""
        assert self.get_product_name() == self.get_name_of_product_was_added_to_basket(), 'В корзину добавлен не тот продукт'

    def should_not_be_success_message(self):
        """Проверяет отсутствие сообщения об успехе"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Присутствует сообщение об успехе"

    def should_disappear_of_success_message(self):
        """Проверяет, что элемент исчез в искомое время"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение не исчезло"

    def solve_quiz_and_get_code(self):
        """Решает формулу на капче и копирует код в буфер обмена (Ctrl+C)"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            pyperclip.copy(alert_text.split()[-1])
            print(f"Ваш код: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("Alert отсутствует")

    def should_be_increased_price_basket(self):
        """Проверяет, что цена в корзине изменилась после добавления продукта в нее"""
        product_price = self.get_product_price()
        total_price = self.get_total_price()
        assert product_price == total_price, 'Цена в корзине и цена продукта не сходятся. Продукт: {}. Корзина: {}'.format(
            product_price, total_price)

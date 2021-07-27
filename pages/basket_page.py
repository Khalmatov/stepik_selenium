from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_msg_about_basket_is_empty(self):
        """Проверяет присутствии сообщения о пустоте корзины"""
        assert 'пуста' in self.browser.find_element(
            *BasketPageLocators.MSG_ABOUT_BASKET_IS_EMPTY).text, "Отсутствует сообщение о пустоте корзины "

    def should_not_be_items(self):
        """Проверяет отсутствие продуктов в корзине"""
        self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Продукты присутсвуют в корзине"

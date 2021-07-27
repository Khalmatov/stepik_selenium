from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from stepik_selenium.pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser: WebDriver, url: str, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_basket_page(self):
        """Переход в корзину"""
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def go_to_login_page(self):
        """Переход в страницу авторизации"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def is_disappeared(self, how, what, timeout=4):
        """Проверяет, что элемент исчез со временем"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        """Проверяет присутствие элемента на странице"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Проверяет отсутствие элемента на странице"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        """Проверяет, что пользователь авторизован"""
        assert self.is_element_present(*BasePageLocators.USER_ICON), "Отсутствует иконка пользователя," \
                                                                     " возможно, пользователь не авторизован"

    def should_be_login_link(self):
        """Проверяет присутствие ссылки на страницу авторизации"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Отсутствует ссылка для логина"

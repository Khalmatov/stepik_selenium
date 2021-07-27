from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group a.btn-default')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, 'basket-items')
    MSG_ABOUT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, 'div#content_inner p')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_PASSWORD1 = (By.ID, 'id_registration-password1')
    REGISTER_PASSWORD2 = (By.ID, 'id_registration-password2')
    REGISTER_SUBMIT = (By.NAME, 'registration_submit')


class ProductPageLocators:
    BASKET_MINI = (By.CLASS_NAME, 'basket-mini')
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    PRODUCT_WAS_ADDED_TO_BASKET = SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')

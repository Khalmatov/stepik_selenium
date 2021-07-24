from stepik_selenium.pages.login_page import LoginPage


def test_guest_can_login_and_register(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

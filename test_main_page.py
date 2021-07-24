link = "https://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    go_to_login_page(browser)


def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()



def test_is_btn_basket_exist(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    basket = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert basket, 'Кнопка добавления товара в корзину отсутствует'

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
selector = '[class="btn btn-lg btn-primary btn-add-to-basket"]'


def test_the_page_have_a_basket_button(browser, by):
    browser.get(link)
    assert browser.find_element(by.CSS_SELECTOR, selector), f"Не найдена кнопка добавления в корзину.."

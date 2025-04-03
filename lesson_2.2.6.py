# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
# browser.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math as m


# ссылки для проверки сайтов
# link = 'http://suninjuly.github.io/selects1.html'
link = 'http://suninjuly.github.io/execute_script.html'

# данные для ввода в поля формы
test_inputs = ['Ivan',
               'Petrov',
               'ivanpetrov@testmail.com',
               ]

# тексты плейсхолдеров в форме
placeholders = ['Input your first name',
                'Input your last name',
                'Input your email',
                ]

# собираем список из готовых к поиску локаторов
locators = []
for item in placeholders:
    locators.append('input[required][placeholder="' + item + '"]')


def calc(x):
    return str(m.log(abs(12*m.sin(int(x)))))


def locator_finding_func(page, locators):
    """Функция поиска необходимых локаторов на странице.
    Возвращает готовый список элементов страницы, которыми
    можно дальше управлять при необходимости.

    Аргументы
    -------
    page : object, required
        объект класса Chrome(), наша страница с элементами
    locators : list, required
        список локаторов для поиска необходимых элементов страницы

    Если искомый элемент по какой-то причине будет отсутствовать
    на странице, то в консоли увидим следующее сообщение:
    NoSuchElementException: Message: no such element: Unable to locate element:...

    """
    result_list = []
    for i in range(len(locators)):
        found_element = page.find_element(By.CSS_SELECTOR, locators[i])
        result_list.append(found_element)
    return result_list


def registration_form_test(link: str, locators: list, inputs: list):
    """Для удобства проверки нескольких сайтов
    реализована данная функция, которая принимает на вход
    некоторые параметры

    Аргументы
    -------
    link : str, required
        ссылка на проверяемый ресурс
    locators : list, required
        список локаторов для поиска необходимых элементов страницы
    inputs: list, required
        список тестовых данных для заполнения формы регистрации

    Проверка утверждений
    -------
    assert "Congratulations! ...
        Если страница после нажатия кнопки отправки данных формы
        не содержит искомый текст, значит тест считается проваленным,
        в консоли будет отображаться соответствующий AssertionError

    """

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Ищем необходимые поля для заполнения
        # required_inputs = locator_finding_func(browser, locators)
        x = browser.find_element(By.ID, 'input_value').text
        y = calc(x)

        answer = browser.find_element(By.ID, 'answer')
        answer.send_keys(y)

        checkbox = browser.find_element(By.ID, 'robotCheckbox')
        browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
        checkbox.click()

        radio_1 = browser.find_element(By.ID, 'peopleRule')
        browser.execute_script("return arguments[0].scrollIntoView(true);", radio_1)

        radio = browser.find_element(By.ID, 'robotsRule')
        browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
        radio.click()


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()


        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        try:
            browser.quit()
        except Exception:
            pass


registration_form_test(link, locators, test_inputs)

# не забываем оставить пустую строку в конце файла
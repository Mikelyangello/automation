from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# ссылки для проверки сайтов
test_links = ['https://suninjuly.github.io/file_input.html',
              ]

# данные для ввода в поля формы
test_inputs = ['Ivan',
               'Petrov',
               'ivanpetrov@testmail.com',
               ]

# тексты плейсхолдеров в форме
placeholders = ['Enter first name',
                'Enter last name',
                'Enter email',
                ]

# собираем список из готовых к поиску локаторов
locators = []
for item in placeholders:
    locators.append('input[required][placeholder="' + item + '"]')


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
        required_inputs = locator_finding_func(browser, locators)

        # Ваш код, который заполняет обязательные поля
        [element.send_keys(inputs[required_inputs.index(element)]) for element in required_inputs]

        # insert file
        add_file = browser.find_element(By.ID, 'file')
        import os
        current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, 'File_1.txt')
        add_file.send_keys(file_path)


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        try:
            browser.quit()
        except Exception:
            pass


for link in test_links:
    registration_form_test(link, locators, test_inputs)

# не забываем оставить пустую строку в конце файла
class TestLoginAndAnswer:
    import pytest

    @pytest.mark.parametrize('link', [
            "https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1",
        ])
    def test_of_success_authorisation(self, browser, link, mc, by, wd, ec):
        browser.get(link)
        # ждем кнопку "Войти" для открытия формы авторизации и прожимаем ее
        login_btn = wd(browser, 12).until(ec.visibility_of_element_located((by.CSS_SELECTOR, mc.sel_login_window_btn)))
        login_btn.click()
        # ждем форму авторизации и заполняем ее поля, прожимая кнопку входа
        wd(browser, 12).until(ec.visibility_of_element_located((by.CSS_SELECTOR, mc.sel_login_form)))
        browser.find_element(by.CSS_SELECTOR, mc.sel_login).send_keys(mc.login)
        browser.find_element(by.CSS_SELECTOR, mc.sel_password).send_keys(mc.password)
        browser.find_element(by.CSS_SELECTOR, mc.sel_submit_btn).click()
        # ждем исчесзновения формы авторизации и появления значка пользователя и формы для вставки ответа + клик
        wd(browser, 12).until(ec.invisibility_of_element_located((by.CSS_SELECTOR, mc.sel_login_form)))
        wd(browser, 12).until(ec.visibility_of_element_located((by.CSS_SELECTOR, mc.sel_auth_profile)))
        answer = wd(browser, 12).until(ec.visibility_of_element_located((by.CSS_SELECTOR, mc.sel_for_answer)))
        answer.click()
        try:
            # т.к. сервера Stepik нестабильны, то через эту конструкцию (try) обходим исключения и падения тестов
            # генерируем правильный ответ, отправляем в поле и прожимаем кнопку
            answer.send_keys(mc.answer())
            btn = wd(browser, 12).until(ec.element_to_be_clickable((by.CSS_SELECTOR, mc.sel_btn_for_answer)))
            btn.click()
        except Exception:
            # Не рекомендую так делать, но ради прохождения задания себе позволил
            pass
        # Ждем, находим ответ в поле подсказки и забираем его себе
        hint = wd(browser, 12).until(ec.visibility_of_element_located((by.CSS_SELECTOR, mc.sel_for_hint))).text
        # Формируем сообщение об ошибки для ассерта, параллельно добавляя ответ в наш класс с данными
        assertion_msg = mc.assertion_msg(hint) if hint != mc.expecting_hint else None
        # Принтуем накопительный ответ из класса перед ассертом (потом в логах можно его просто забрать)
        print(f"{'!' * 30}THE REAL ANSWER IS{'!' * 30}\n{mc.real_answer}")
        # Ну и финальная проверка для прохождения или падения теста
        assert hint == mc.expecting_hint, assertion_msg

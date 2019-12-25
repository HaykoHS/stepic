from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение обязательных полей регистрации
    input1 = browser.find_element_by_css_selector (".first_block .form-control.first")
    input1.send_keys('MY NAME')
    input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
    input2.send_keys('MY SURNAME')
    input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
    input3.send_keys('EMAIL')
    # Заполнение необязательных полей регистрации
    input4 = browser.find_element_by_css_selector (".second_block .form-control.first")
    input4.send_keys('+791191919191')
    input5 = browser.find_element_by_css_selector (".second_block .form-control.second")
    input5.send_keys("MY HOME ADDRESS")

    # Отправка формы
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    # Поиск элемента, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # Проверка совпадения фактического и ожидаемого текста
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Финальное ожидание и закрытие браузера
    time.sleep(10)
    browser.quit()
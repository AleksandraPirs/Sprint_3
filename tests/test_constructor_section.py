from locators import MainPageLocators
from urls import URLS

class TestConstructorPage:
    def test_transition_to_bun_success(self, driver):
        #Проверка перехода к разделу 'Булки'
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()
        driver.find_element(*MainPageLocators.bun_btn).click()
        bun_class = driver.find_element(*MainPageLocators.ban_class)
        assert bun_class.text == 'Булки'

    def test_transition_to_sauces_success(self, driver):
        #Проверка перехода к разделу 'Соусы'
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()
        souces_class = driver.find_element(*MainPageLocators.souces_class)
        assert souces_class.text == 'Соусы'

    def test_transition_to_topping_success(self, driver):
        #Проверка перехода к разделу 'Начинки'
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.toppings_btn).click()
        topping_class = driver.find_element(*MainPageLocators.topping_class)
        assert topping_class.text == 'Начинки'
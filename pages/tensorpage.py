from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import Locators
from selenium.common.exceptions import NoSuchElementException
import allure


class TensorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_strength_people_click_more_about(self):
        with allure.step('Check to exist the block «The power is in people»'):
            try:
                self.driver.find_element(By.XPATH, Locators.strength)
            except NoSuchElementException:
                assert False
        with allure.step('Click the button «More» in the block «The power is in people»'):
            self.driver.find_element(By.XPATH, Locators.more_about_strength_people).click()

    @property
    def photos_working(self):
        return self.driver.find_elements(By.XPATH, Locators.photos_working)

    def is_photo_one_size(self):
        set_heights = []
        set_width = []

        for photo in self.photos_working:
            set_heights.append(photo.get_attribute('height'))
            set_width.append(photo.get_attribute('height'))
        return len(set(set_heights)) == 1 and len(set(set_width)) == 1

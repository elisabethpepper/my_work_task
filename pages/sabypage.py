from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure


class SabyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        with allure.step('Open https://saby.ru'):
            self.driver.get('https://saby.ru/')

    @property
    def contacts(self):
        return self.driver.find_element(By.XPATH, Locators.contacts)

    def check_click_more_offices(self):
        with allure.step('Switch to the section «Contacts»'):
            wait = WebDriverWait(self.driver, 10)
            wait.until(
                ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT, Locators.more_offices))
            ).click()

    @property
    def logo_tensor(self):
        return self.driver.find_element(By.CSS_SELECTOR, Locators.logo)

    @property
    def region(self):
        return self.driver.find_element(By.XPATH, Locators.current_region)

    @property
    def region_name(self):
        return self.region.text

    @property
    def partners(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(
            ec.visibility_of_all_elements_located((By.CSS_SELECTOR, Locators.partners))
        )

    def current_partners(self):
        current_info_partner = []

        for partner in self.partners:
            current_info_partner.append(partner.text)
        return current_info_partner

    def change_region(self, name_region):
        with allure.step('Change the region'):
            self.region.click()
            wait = WebDriverWait(self.driver, 10)
            region = wait.until(
                ec.visibility_of_element_located((By.XPATH, Locators.region_in_list.format(name_region)))
            )

            num_region = region.text.split(' ')[0]
            region.click()

            wait.until(
                ec.all_of(ec.title_contains(name_region), ec.url_contains(num_region))
            )

    def is_region_change(self, name_region, partners_list):
        with allure.step('Check the region change'):
            new_partners = self.current_partners()
            check_partners = len(list(set(partners_list) & set(new_partners))) == 0
            check_name = self.region_name == name_region
            return check_partners and check_name

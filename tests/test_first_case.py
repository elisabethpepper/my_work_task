from pages.sabypage import SabyPage
from pages.tensorpage import TensorPage
import allure


def test_first_task(driver):
    session = SabyPage(driver)
    session.open()

    session.contacts.click()
    session.check_click_more_offices()

    with allure.step('Find and click the tensor logo'):
        session.logo_tensor.click()

    with allure.step('Switch the tag to https://tensor.ru'):
        session.switch_page(1)
        session = TensorPage(driver)

    session.check_strength_people_click_more_about()
    with allure.step('Check to the url change'):
        assert driver.current_url == 'https://tensor.ru/about'

    with allure.step('Check the same size of all photos in the block «We are working»'):
        assert session.is_photo_one_size()

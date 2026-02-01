from pages.sabypage import SabyPage
import allure


def test_second_task(driver):
    session = SabyPage(driver)
    session.open()

    session.contacts.click()
    session.check_click_more_offices()

    current_partner_list = session.current_partners()
    with allure.step('Check the right region and changing partners list'):
        assert session.region.text == 'Ярославская обл.' and len(current_partner_list) > 0

    new_region = "Камчатский край"
    session.change_region(new_region)
    assert session.is_region_change(new_region, current_partner_list)

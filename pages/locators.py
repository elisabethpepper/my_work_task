class Locators:
    # saby page
    contacts = '//span[text()="Контакты"]'
    more_offices = 'офисов в регионе'

    # contacts
    logo = '#contacts_clients [class~="sbisru-Contacts__logo-tensor"]'
    current_region = '//*[@class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]/child::span'
    region_in_list = '//*[contains(text(),"{}")]'
    partners = '#contacts_list div[item-parent-key]'

    # tensor page
    strength = '//p[contains(@class,"tensor_ru-Index__card-title") and text()="Сила в людях"]'
    more_about_strength_people = '//p[contains(@class,"tensor_ru-Index__card-title") and text()="Сила в людях"]/following-sibling::p/child::a'
    photos_working = '//*[text()="Работаем"]/parent::*/following-sibling::*/child::*/descendant::img'

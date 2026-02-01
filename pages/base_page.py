class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def switch_page(self, index):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[index])


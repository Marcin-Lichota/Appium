from appium.webdriver.common.appiumby import AppiumBy

from test.views.base_view import BaseView


class ListView(BaseView):
    STRATUS = (AppiumBy.ACCESSIBILITY_ID, 'Stratus')
    CLOUD_TEXT = (AppiumBy.ID, 'android:id/message')

    def nav_back(self):
        from test.views.home_view import HomeView
        self.driver.back()
        return HomeView(self.driver)

    def find_stratus(self):
        self.swipe(self.STRATUS)

    def getstratustext(self):
        self.find(self.STRATUS).click()
        self.wait_for(self.CLOUD_TEXT)
        return self.find(self.CLOUD_TEXT).text




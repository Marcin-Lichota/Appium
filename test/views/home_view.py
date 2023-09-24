from appium.webdriver.common.appiumby import AppiumBy

from test.views.base_view import BaseView
from test.views.echo_view import EchoView
from test.views.list_view import ListView

class HomeView(BaseView):
    ECHO_ITEM = (AppiumBy.ACCESSIBILITY_ID, 'Echo Box')
    LIST_ITEM = (AppiumBy.ACCESSIBILITY_ID, 'List Demo')

    def nav_to_echo_box(self):
        self.wait_for(self.ECHO_ITEM).click()
        return EchoView(self.driver)

    def nav_to_list_demo(self):
        self.wait_for(self.LIST_ITEM).click()
        return ListView(self.driver)


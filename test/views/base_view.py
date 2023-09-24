import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseView(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)
    # swiping screen by 250 px until desired element is found
    def swipe(self, locator):
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']
        starty = screenHeight / 9 + 250
        endy = screenHeight / 9
        a = False
        while not a:
            try:
                self.driver.find_element(*locator).is_displayed()
                a = True
            except NoSuchElementException:
                actions = TouchAction(self.driver)
                actions.long_press(None, screenWidth / 2, starty).move_to(None, screenWidth / 2, endy).release().perform()
                a = False

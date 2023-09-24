import pytest
from appium import webdriver
from os import path
from appium.options.android import UiAutomator2Options
from test.views.home_view import HomeView

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, '..', 'test', 'TheApp.apk')
APPIUMS = ['http://localhost:4700', 'http://localhost:4701']

DEVICES_LIST = [
{
    'platformName': 'Android',
    'automationName': 'uiautomator2',

    'udid':'emulator-5554',
    'app': APP,
    "systemPort": 8200,

},
{
    'platformName': 'Android',
    'automationName': 'uiautomator2',

    'udid':'emulator-5556',
    'app': APP,
    "systemPort": 8201,

},]

#pytest -xdist is creating workers with names master gw1 and so on, so we extract that number, so we can use it as index
@pytest.fixture
def worker_num(worker_id):
    if worker_id == 'master':
        worker_id = 'gw0'
    return int(worker_id[2:])

@pytest.fixture
def server(worker_num):
    if worker_num >= len(APPIUMS):
        raise Exception('Too many workers for the number of Appium servers')
    return APPIUMS[worker_num]

@pytest.fixture
def caps(worker_num):
    cap_set = DEVICES_LIST
    if worker_num >= len(cap_set):
        raise Exception('Too many workers for the number of capability options.')
    return cap_set[worker_num]

@pytest.fixture
def driver(server, caps):
    options = UiAutomator2Options()
    options.load_capabilities(caps)
    driver = webdriver.Remote(command_executor=server, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def home(driver):
    return HomeView(driver)


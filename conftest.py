from datetime import datetime

import allure
import pytest
from selenium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--window-size=1440,1080')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    if request.node.rep_call.failed:
        try:
            allure.attach(driver.get_screenshot_as_png(), name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass
    # attach = driver.get_screenshot_as_png()
    # allure.attach(attach, name=f'Screenshot {datetime.today}', attachment_type=allure.attachment_type.PNG)
    driver.quit()

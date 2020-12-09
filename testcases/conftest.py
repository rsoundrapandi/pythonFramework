import pytest
from selenium import webdriver
import os
from datetime import datetime

driver = None
browser_name = None

parent_dir = os.path.dirname(os.getcwd())


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="B:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="path\\to\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":

        xfail = hasattr(report, "wasxfail")

        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = "reports/" + report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            parent_dir = os.path.dirname(os.getcwd()).split('/')[-1]

            if file_name:
                html = (
                        '<div><img src="/%s/testcases/%s" alt="screenshot" style="width:304px;height:228px;" '
                        'onclick="window.open(this.src)" align="right"/></div>' % (parent_dir, file_name)
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists("B:\\pythonprojects\\pythonframework\\testcases\\reports".format(parent_dir)):
        os.makedirs("B:\\pythonprojects\\pythonframework\\testcases\\reports".format(parent_dir))
    config.option.htmlpath = ("reports/" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html")



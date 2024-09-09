from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from lib.pages.basepage import BasePage
from lib.pages.homepage import HomePage

def before_all(context):
    driver = set_selenium_driver(context)
    driver.set_page_load_timeout(25)
    driver.maximize_window()

    context.web_driver = driver
    context.browser = BasePage(context)
    context.home = HomePage(context)

    context.all_contexts = {
        'home': context.home,
    }


def after_scenario(context, scenario):
    sep = '\n'
    steps = []
    for step in scenario.steps:
        steps.append(str(step).replace('<', '').replace('>', '').capitalize())
    if test_rail_report(context) == 'True':
        validate_scenario(scenario, context, sep.join(steps))
    pass


def after_all(context):
    if hasattr(context, 'web_driver'):
        context.web_driver.quit()
    print("===== That's all folks =====")

def after_step(context, step):
    if step.exception is not None:
        context.step_error = step.exception
        context.failed_step = step.name
    if step.status == 'failed':
        context.failed_step = step.name

def validate_scenario(scenario, context, steps):
    if scenario.status.name == 'failed':
        return print('Failed Step: ' + context.failed_step + '\n' + str(context.step_error))
    
    
def set_selenium_driver(context):
    env = context.config.userdata.get("driver", "local")
    if env == 'aws':
        driver = set_docker_driver()
    else:
        driver = set_local_driver()
    return driver

def set_local_driver() -> webdriver.Chrome:
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def set_docker_driver() -> webdriver.Remote:
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--lang=en-GB")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Remote(
        command_executor='http://0.0.0.0:4444/wd/hub',
        options=chrome_options
    )
    return driver

def test_rail_report(context):
    return context.config.userdata.get("testrail", "False")

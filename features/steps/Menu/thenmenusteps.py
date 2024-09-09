from behave import then, use_step_matcher
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

use_step_matcher("re")

@then('I should be redirected to the corresponding page')
def step_impl(context):
    expected_url = context.expected_url
    actual_url = context.browser.get_current_url()  # Asegúrate de usar el método correcto
    assert actual_url == expected_url, f"Expected URL {expected_url} but got {actual_url}"
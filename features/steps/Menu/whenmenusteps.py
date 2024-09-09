from behave import when, use_step_matcher
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


from lib.components.generalcomponents import GeneralComponents
from lib.helpers.generalhelpers import transformation_helper

@when('I click on each menu option')
def step_when_click_on_each_menu_option(context):
    page = context.browser  # Asegúrate de que esto sea una instancia de BasePage

    # Encuentra todos los elementos del menú usando el selector adecuado
    menu_items = page.find_elements(By.CSS_SELECTOR, ".HtHs-nav-list li a")

    for index in range(len(menu_items)):
        try:
            # Volver a encontrar los elementos del menú, en caso de que se vuelvan obsoletos
            menu_items = page.find_elements(By.CSS_SELECTOR, ".HtHs-nav-list li a")

            if index >= len(menu_items):
                break

            item = menu_items[index]
            # Extraer la URL esperada del atributo href
            expected_url = item.get_attribute('href')
            print(f"Testing menu item {index + 1} with URL: {expected_url}")

            # Hacer clic en la opción del menú
            item.click()

            # Esperar a que la URL cambie a la URL esperada
            WebDriverWait(page.web_driver, 10).until(EC.url_to_be(expected_url))
            print(f"Successfully navigated to: {expected_url}")

            # Verificar la redirección
            current_url = page.get_current_url()
            assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

            # Volver a la página principal para el siguiente enlace
            page.visit_page(page.base_url)
            print("Returned to the main page.")

            # Asegurarse de que los elementos del menú estén disponibles de nuevo después de regresar a la página principal
            WebDriverWait(page.web_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".HtHs-nav-list li a")))

        except TimeoutException:
            print(f"Timeout while waiting for the URL to change to {expected_url}")
        except Exception as e:
            print(f"An error occurred: {e}")
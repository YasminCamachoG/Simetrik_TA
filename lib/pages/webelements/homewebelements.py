from selenium.webdriver.common.by import By


class HomeWebElements:
    name_tag_input = (By.CSS_SELECTOR, 'div.udzg[role="combobox"][aria-label="Cabina Económica"]') 
    name_dropdown_column_input = (By.CSS_SELECTOR, 'div.prSa')  
    search_tag_input = (By.CSS_SELECTOR, 'div.udzg[role="combobox"][aria-label="Tipo de viaje Ida y vuelta"]')  
    cancel_button = (By.CSS_SELECTOR, 'div.c_neb-item-close > div[role="button"]')  
    create_column_disabled_button = (By.CSS_SELECTOR, 'div[role="button"]')  

    # Elementos adicionales para verificar que la página está abierta
    where_label = (By.CSS_SELECTOR, 'div.mc6t-logo')
    signin_button = (By.XPATH, '//div[span[text()="Iniciar sesión"]]')
    search_button = (By.CSS_SELECTOR, 'button.RxNS[aria-label="Buscar"]')
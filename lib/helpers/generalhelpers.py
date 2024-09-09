from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from lib.pages.webelements.homewebelements import HomeWebElements



def validate_text(comparison_type, text_a, text_b):
    if comparison_type == 'contain':
        return text_a.strip() in text_b.strip()
    else:
        return text_a.strip() == text_b.strip()


def transformation_helper(name, element_type):
    # Genera el nombre del atributo esperado en HomeWebElements
    formatted_name = '{}_{}'.format(name.lower(), element_type.lower())
    
    # Devuelve el nombre generado
    return formatted_name


def transformation_to_element_name(table_elements):
    element_final_list = []
    for element in table_elements:
        # Usa transformation_helper para obtener el nombre del atributo
        element_name = transformation_helper(element['name'], element['type'])
        
        # Obtiene el selector de HomeWebElements usando el nombre generado
        if hasattr(HomeWebElements, element_name):
            selector = getattr(HomeWebElements, element_name)
            element_final_list.append(selector)
        else:
            raise ValueError(f"Selector for element '{element_name}' not found in HomeWebElements.")
    
    return element_final_list


def transform_validation(expression):
    final_expression = True
    if expression != "should":
        final_expression = False
    return final_expression


def clean_behave_list(behave_list):
    cleaned_list = []
    for row in behave_list:
        cleaned_list.append(row[0])
    return cleaned_list


def split_and_replace_string(text_element) -> list:
    new_string = []
    for x in text_element.split(" "):
        new_string.append(x.replace("\n", ""))
    return new_string


def join_words(word_list) -> str:
    new_str = ""
    for word in word_list:
        new_str += word
    return new_str


def validate_wait_results(*waits):
    validation_results = []
    for wait in waits:
        if isinstance(wait, WebElement):
            validation_results.append(True)
        else:
            validation_results.append(wait)
    return validation_results

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

def is_element_present(driver, locator_type, locator_value):
    try: driver.find_element(by=locator_type, value=locator_value)
    except NoSuchElementException: return False
    return True

def title_matches(term, driver):
    return term in driver.title

def is_results_found(phrase, driver):
    return phrase not in driver.page_source

def upload_file(driver, id, file_path, submit_id):
    driver.find_element_by_id(id).send_keys(fp)
    driver.find_element_by_id(submit_id).click()

def execute_script(driver, js_string):
    driver.execute_script(js_string)

def drag_and_drop(driver, source_selector, source_value, target_selector, target_value):
    element = driver.find_element_by_name("source")
    target = driver.find_element_by_name("target")
    action_chains = ActionChains(driver)
    action_chains.drag_and_drop(element, target).perform()

def select_drop_down(driver, method, selector_method, selector, select_string):
    select = Select(driver, select_method, selector)
    if method == 'text':
        select.select_by_visible_text(select_string)
    elif method == 'index':
        select.select_by_index(select_string)
    elif method == 'value':
        select.select_by_value(select_string)
    else:
        raise ValueError('input method not valid')

def select_method(driver, selector_method, selector):
    if select_method == 'xpath':
        return driver.find_element_by_xapth(selector)
    elif select_method == 'id':
        return driver.find_element_by_id(selector)
    elif select_method == 'name':
        return driver.find_element_by_id(selector)
    else:
        raise ValueError('input method not valid')

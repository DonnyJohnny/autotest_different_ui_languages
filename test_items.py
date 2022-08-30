import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

button = None

def test_add_button_exist(browser):
    browser.get(link)
    time.sleep(1)                           # Увеличь значение, чтобы страница дольше отставалась открытой для проверки                                      
    button = 0
    
    try:
        print("Trying to find add button...")
        button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')))
        print("'Add to basket' button is found")
    finally:
        assert button != 0, "Failed to find 'Add to basket' button"
    
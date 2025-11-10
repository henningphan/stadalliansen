from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import time

class ServiceInfo:
    def __init__(self, description, start, end):
        self.description = description
        self.start = start
        self.end = end


def get_service_infos(username, password):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://stadalliansen.städportalen.se/")

    title = driver.title

    driver.implicitly_wait(0.5)

    username_box = driver.find_element(by=By.XPATH, value="//input[starts-with(@placeholder, 'Användarnamn')]")
    submit_button = driver.find_element(by=By.TAG_NAME, value="button")

    password_box = driver.find_element(by=By.XPATH, value="//input[starts-with(@type, 'password')]")
    username_box.send_keys(username)
    password_box.send_keys(password)
    submit_button.click()
    time.sleep(1)
    services_button = driver.find_element(by=By.XPATH, value="//a[@href='/services']")
    services_button.click()

    timeout_s = 20
    wait = WebDriverWait(driver, timeout_s)# .until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "service-info")))

    service_infos = driver.find_elements(by=By.CLASS_NAME, value="service-info")
    driver.quit()
    return service_infos

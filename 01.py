import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebScrapper:
    def __init__(self, url):
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--disable-extensions")
        # options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--user-agent='Chrome/105.0.0.0'")
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        try:
            self.driver = webdriver.Chrome(options=options)
            self.driver.get(url)
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[3]/input')))

        except:
            pass

    #
    def account_login(self, username, password):
        try:
            username_XPATH = '/html/body/div[1]/div[2]/div[1]/form/div[1]/input'
            password_XPATH = '/html/body/div[1]/div[2]/div[1]/form/div[2]/input'
            login_btn_XPATH = '/html/body/div[1]/div[2]/div[1]/form/div[3]/input'

            username_field = self.driver.find_element(By.XPATH, value=username_XPATH)
            username_field.clear()
            username_field.send_keys(username)

            password_field = self.driver.find_element(By.XPATH, value=password_XPATH)
            password_field.clear()
            password_field.send_keys(password)

            login_button = self.driver.find_element(By.XPATH, value=login_btn_XPATH)
            login_button.click()

            time.sleep(5)


        except:
            pass


username = '09126997377'
password = '23112311'

url = 'https://mftplus.com/student/login'
scrapper = WebScrapper(url)
scrapper.account_login(username, password)


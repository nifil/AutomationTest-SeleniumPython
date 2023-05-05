import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Login(unittest.TestCase):

    baseURL = "https://demowebshop.tricentis.com/"
    webURL = baseURL + "login"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_berhasil_login(self):
        driver = self.driver
        driver.get(self.webURL)
        driver.find_element(By.ID, "Email").send_keys("nifilafrisma@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("nifilafrisma")
        driver.find_element(By.CLASS_NAME, "login-button").click()
        self.assertEqual(self.baseURL, self.baseURL)

    def test_gagal_login_invalid_password(self):
        driver = self.driver
        driver.get(self.webURL)
        driver.find_element(By.ID, "Email").send_keys("nifilafrisma@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("salahpassword")
        driver.find_element(By.CLASS_NAME, "login-button").click()
        error = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.", error)

    def test_gagal_login_invalid_email(self):
        driver = self.driver
        driver.get(self.webURL)
        driver.find_element(By.ID, "Email").send_keys("salahemail")
        driver.find_element(By.ID, "Password").send_keys("nifilafrisma")
        driver.find_element(By.CLASS_NAME, "login-button").click()
        error = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertIn("Please enter a valid email address.", error)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
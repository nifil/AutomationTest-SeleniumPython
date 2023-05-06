import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Checkout(unittest.TestCase):

    baseURL = "https://demowebshop.tricentis.com/"
    webURL = baseURL + "cart"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_berhasil_checkout(self):
        driver = self.driver
        driver.get(self.baseURL+"login")
        driver.find_element(By.ID, "Email").send_keys("nifilafrisma@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("nifilafrisma")
        driver.find_element(By.CLASS_NAME, "login-button").click()
        driver.get(self.webURL)
        driver.find_element(By.ID, "termsofservice").click()
        driver.find_element(By.ID, "checkout").click()
        url = driver.current_url
        self.assertEqual(url, self.baseURL + "onepagecheckout")

    def test_gagal_checkout(self):
        driver = self.driver
        driver.get(self.baseURL+"login")
        driver.find_element(By.ID, "Email").send_keys("nifilafrisma@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("nifilafrisma")
        driver.find_element(By.CLASS_NAME, "login-button").click()
        driver.get(self.webURL)
        driver.find_element(By.ID, "checkout").click()
        warning = driver.find_element(By.ID, "terms-of-service-warning-box").text
        self.assertIn("Please accept the terms of service before the next step.", warning)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
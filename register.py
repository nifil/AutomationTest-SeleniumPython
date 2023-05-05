import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from data import dataInput
from baseRegister import registerUser

class Register(unittest.TestCase):

    baseURL = "https://demowebshop.tricentis.com/"
    webURL = baseURL + "register"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_berhasil_register(self):
        driver = self.driver
        driver.get(self.webURL)
        driver.find_element(By.ID, "FirstName").send_keys("Nifil")
        driver.find_element(By.ID, "LastName").send_keys("Afrisma")
        driver.find_element(By.ID, "Email").send_keys("nifilafrisma@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("nifilafrisma")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("nifilafrisma")
        driver.find_element(By.ID, "register-button").click()
        url = driver.current_url
        self.assertEqual(url, self.baseURL + "registerresult/1")

    def test_gagal_register_mengosongi_semua_kolom(self):
        driver = self.driver
        driver.get(self.webURL)
        driver.find_element(By.ID, "register-button").click()
        first_name = driver.find_element(By.CSS_SELECTOR, "[data-valmsg-for=FirstName]").text
        last_name = driver.find_element(By.CSS_SELECTOR, "[data-valmsg-for=LastName]").text
        self.assertIn("First name is required.", first_name)
        self.assertIn("Last name is required.", last_name)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class addToCart(unittest.TestCase):

    baseURL = "https://demowebshop.tricentis.com/"
    webURL = baseURL + "fiction"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_berhasil_add_cart(self):
        driver = self.driver
        driver.get(self.baseURL+"login")
        driver.find_element(By.ID, "Email").send_keys("nifilafrisma@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("nifilafrisma")
        driver.find_element(By.CLASS_NAME, "login-button").click()
        driver.get(self.webURL)
        driver.find_element(By.ID, "giftcard_2_RecipientName").send_keys("Nifil Afrisma")
        driver.find_element(By.ID, "giftcard_2_RecipientEmail").send_keys("nifilafrisma@gmail.com")
        driver.find_element(By.ID, "add-to-cart-button-2").click()
        qty = driver.find_element(By.CLASS_NAME, "cart-qty").text
        alerts = driver.find_elements(By.CLASS_NAME, 'bar-notification')
        for alert in alerts:
            text = alert.text
        assert qty != '(0)'
        self.assertIn("The product has been added to your shopping cart", text)

    def test_gagal_add_cart_mengosongkan_recipient_email(self):
        driver = self.driver
        driver.get(self.baseURL+"login")
        driver.find_element(By.ID, "Email").send_keys("nifilafrisma@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("nifilafrisma")
        driver.find_element(By.CLASS_NAME, "login-button").click()
        driver.get(self.webURL)
        driver.find_element(By.ID, "giftcard_2_RecipientName").send_keys("Nifil Afrisma")
        driver.find_element(By.ID, "add-to-cart-button-2").click()
        alerts = driver.find_elements(By.CLASS_NAME, 'bar-notification')
        for alert in alerts:
            text = alert.text
        self.assertIn("Enter valid recipient email", text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
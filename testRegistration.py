import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

print("Nazywam się ", __name__)

firstNameI = "Iwo"
lastNameI = "Nchen"
emailI = "iwonsien@com-com-com-com.com"
password = "Secret"
addressOne = "Beverly Hills"
addressTwo = "90210"
cityI = "Los Angeles"
zipCodeI = "90210"
phoneMobileI = "001155887744"
addressAliasI = "My fancy address"


class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        print("Startujemy")
        pass

    def testRegistratiom(self):
        signinButton = self.driver.find_element_by_class_name("login")
        signinButton.click()
        emailField = self.driver.find_element_by_id("email_create")
        emailField.send_keys(emailI)
        submitCreate = self.driver.find_element_by_id("SubmitCreate")
        submitCreate.click()

        genderButton = self.driver.find_element_by_id("id_gender2")
        genderButton.click()

        firstName = self.driver.find_element_by_id("customer_firstname")
        firstName.send_keys(firstNameI)
        lastName = self.driver.find_element_by_id("customer_lastname")
        lastName.send_keys(lastNameI)

        emailField2 = self.driver.find_element_by_id("email")
        emailValue = emailField2.get_attribute("value")
        assert emailValue == emailI
        passwordField = self.driver.find_element_by_id("passwd")
        passwordField.send_keys(password)

        days = Select(self.driver.find_element_by_id('days'))
        days.select_by_index(1)

        months = Select(self.driver.find_element_by_id('months'))
        months.select_by_index(3)

        years = Select(self.driver.find_element_by_id('years'))
        years.select_by_value('2000')

        specialOffers = self.driver.find_element_by_id("optin")
        specialOffers.click()

        #        firstNameControl = self.driver.find_element_by_id("firstname")
        #        firstNameControlValue = emailField2.get_attribute("value")

        address1 = self.driver.find_element_by_id("address1")
        address1.send_keys(addressOne)

        address2 = self.driver.find_element_by_id("address2")
        address2.send_keys(addressTwo)

        cityField = self.driver.find_element_by_id("city")
        cityField.send_keys(cityI)

        stateField = Select(self.driver.find_element_by_id('id_state'))
        stateField.select_by_value('5')

        zipCodeField = self.driver.find_element_by_id("postcode")
        zipCodeField.send_keys(zipCodeI)

        phoneMobileField = self.driver.find_element_by_id("phone_mobile")
        phoneMobileField.send_keys(phoneMobileI)

        addressAliasField = self.driver.find_element_by_id("alias")
        addressAliasField.clear()
        addressAliasField.send_keys(addressAliasI)

        submitButton = self.driver.find_element_by_id("submitAccount")
        submitButton.click()

        home = self.driver.find_element_by_class_name("navigation_page")
        assert home.text == 'My account'

        time.sleep(5)

        pass

    def tearDown(self):
        print("Sprzatamy")
        self.driver.quit()
        pass


if (__name__ == '__main__'):
    unittest.main()

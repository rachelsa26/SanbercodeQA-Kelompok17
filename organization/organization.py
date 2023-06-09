import unittest
import time
import baselogin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pageobject.data import inputan
from pageobject.locator import elemen
import HtmlTestRunner

class TestEditUser(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_organization_generalinfo(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.general_information).click() 
        
        time.sleep(5)

    def test_organization_location(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.location).click() 
        
        time.sleep(5)

    def test_organization_structure(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.structure).click()
        time.sleep(5)

    def test_search_loc_by_name(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.location).click() 
        driver.find_element(By.XPATH,elemen.name).send_keys("KRQNOIOMD") 
        driver.find_element(By.XPATH,elemen.search_but).click()
        
        time.sleep(5)

    def test_search_loc_by_name_empty(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.location).click() 
        driver.find_element(By.XPATH,elemen.search_but).click()
        
        time.sleep(5)

    def test_search_loc_by_name_wrong(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.location).click() 
        driver.find_element(By.XPATH,elemen.name).send_keys("zzzz")
        driver.find_element(By.XPATH,elemen.search_but).click()
        
        time.sleep(5)


    def test_search_loc_by_city(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.location).click() 
        driver.find_element(By.XPATH,elemen.city).send_keys("ja")
        driver.find_element(By.XPATH,elemen.search_but).click()
        
        time.sleep(5)

    def test_search_loc_by_city_empty(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.location).click() 
        driver.find_element(By.XPATH,elemen.city).send_keys(" ")
        driver.find_element(By.XPATH,elemen.search_but).click()
        
        time.sleep(5)

    def test_search_loc_by_city_wrong(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.location).click() 
        driver.find_element(By.XPATH,elemen.city).send_keys("zzzz")
        driver.find_element(By.XPATH,elemen.search_but).click()
        
        time.sleep(5) 

    def test_search_loc_by_country(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.location).click() 
        driver.find_element(By.XPATH,elemen.country).click()
        driver.find_element(By.XPATH,elemen.country_afg).click()
        driver.find_element(By.XPATH,elemen.search_but).click()
        time.sleep(5) 

    def test_search_loc_by_country_empty(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.location).click() 
        driver.find_element(By.XPATH,elemen.search_but).click()
        time.sleep(5) 

    def test_search_loc_by_country_wrong(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.location).click() 
        driver.find_element(By.XPATH,elemen.country).click()
        driver.find_element(By.XPATH,elemen.dum_country).click()
        driver.find_element(By.XPATH,elemen.search_but).click()
        time.sleep(5) 

    def test_editbutton_generalinfo(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.general_information).click() 
        driver.find_element(By.XPATH,elemen.edit_GE).click()
        time.sleep(5) 

    def test_editbutton_structure(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.structure).click() 
        driver.find_element(By.XPATH,elemen.edit_STR).click()
        time.sleep(5) 

    def test_search_loc_reset(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elemen.admin).click() 
        driver.find_element(By.XPATH,elemen.organization).click() 
        driver.find_element(By.XPATH,elemen.location).click() 
        driver.find_element(By.XPATH,elemen.name).send_keys("a") 
        driver.find_element(By.XPATH,elemen.city).send_keys("ja") 
        driver.find_element(By.XPATH,elemen.country).click()
        driver.find_element(By.XPATH,elemen.country_afg).click()
        driver.find_element(By.XPATH,elemen.search_but).click()
        time.sleep(5)
        driver.find_element(By.XPATH,elemen.reset).click()
        
        time.sleep(5)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ReportOrganization'))
# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPrueba1():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_prueba1(self):
    self.driver.get("http://localhost/form1.html")
    self.driver.set_window_size(550, 691)
    self.driver.find_element(By.ID, "nombre").click()
    self.driver.find_element(By.ID, "nombre").send_keys("pepe")
    self.driver.find_element(By.ID, "apellido").click()
    self.driver.find_element(By.ID, "apellido").send_keys("pepe")
    self.driver.find_element(By.ID, "dni").click()
    self.driver.find_element(By.ID, "dni").send_keys("12345678")
    self.driver.find_element(By.ID, "fecha_nacimiento").click()
    self.driver.find_element(By.ID, "fecha_nacimiento").send_keys("2024-01-08")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("pppp@ppp.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("111111")
    self.driver.find_element(By.ID, "r_password").click()
    self.driver.find_element(By.ID, "r_password").send_keys("111111")
    self.driver.find_element(By.ID, "otro").click()
    self.driver.find_element(By.ID, "coche").click()
    self.driver.find_element(By.ID, "bici").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(53)").click()
    assert self.driver.switch_to.alert.text == "pepe pepe"
    self.driver.find_element(By.NAME, "miform").click()
    self.driver.find_element(By.NAME, "miform").click()
    self.driver.find_element(By.ID, "nombre").click()
    self.driver.find_element(By.ID, "nombre").send_keys("aaaaa")
    self.driver.find_element(By.ID, "apellido").click()
    self.driver.find_element(By.ID, "apellido").send_keys("aaaa")
    self.driver.find_element(By.ID, "dni").click()
    self.driver.find_element(By.ID, "dni").send_keys("23456789")
    self.driver.find_element(By.ID, "fecha_nacimiento").click()
    self.driver.find_element(By.ID, "fecha_nacimiento").send_keys("2024-02-21")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("aaaaa@aaa.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("222222")
    self.driver.find_element(By.ID, "r_password").click()
    self.driver.find_element(By.ID, "r_password").send_keys("222222")
    self.driver.find_element(By.ID, "otro").click()
    self.driver.find_element(By.ID, "bici").click()
    self.driver.find_element(By.ID, "autos").click()
    dropdown = self.driver.find_element(By.ID, "autos")
    dropdown.find_element(By.XPATH, "//option[. = 'Toyota']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(53)").click()
    assert self.driver.switch_to.alert.text == "aaaaa aaaa"
  

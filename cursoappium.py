# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

caps = {}
caps["platformName"] = "Android"
caps["appium:deviceName"] = "emulator-5554"
caps["appium:appPackage"] = "com.example.cursoappium"
caps["appium:app"] = "C:\\Users\\pujucan.chaves\\Downloads\\app-curso-appium.apk"
caps["appium:connectHardwareKeyboard"] = "true"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps);

btnCadastrarPessoa = "button_cadastrar"
textInputNome = "TextInputNome"
textInputEmail = "TextInputEmail"
btnCadastrar = "BotaoCadastrar"
radioButtonHomem="radioButton_homem"
spinner_estados="spinner_estados"

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, btnCadastrarPessoa))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, textInputNome)))
driver.find_element(by=AppiumBy.ID, value=textInputNome).send_keys("Pujucan Wessen")
driver.find_element(by=AppiumBy.ID, value=textInputEmail).send_keys("pujucan@test.com")
driver.find_element(by=AppiumBy.ID, value=radioButtonHomem).click();
driver.find_element(by=AppiumBy.ID, value=spinner_estados).click()
driver.find_element(by=AppiumBy.ID, value=btnCadastrar).click()

resultados = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "snackbar_text")))
resultado = resultados.text

print('----------------------')
print(resultado)
print('----------------------')
assert resultado == 'Cadastro realizado com sucesso', 'Resultados divergentes entre o python e o Appium'

#TearDown
driver.quit()

#assert driver.find_element(by=AppiumBy.PARTIAL_LINK_TEXT, "Cadastro realizado com sucesso").text
#assert driver.find_element(By.XPATH("//contains[text(),“Cadastro realizado com sucesso”"))
#assert WebDriverWait(driver, 10).until(EC.xpath(("Cadastro realizado com sucesso")))
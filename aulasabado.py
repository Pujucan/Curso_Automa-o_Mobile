# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time


# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["appium:deviceName"] = "emulator-5554"
caps["appium:appPackage"] = "com.google.android.calculator"
caps["appium:appActivity"] = "com.android.calculator2.Calculator"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

num1 = driver.find_element(by=AppiumBy.ID, value="digit_1")
num2 = driver.find_element(by=AppiumBy.ID, value="digit_2")
num3 = driver.find_element(by=AppiumBy.ID, value="digit_3")
num4 = driver.find_element(by=AppiumBy.ID, value="digit_4")
num5 = driver.find_element(by=AppiumBy.ID, value="digit_5")
num6 = driver.find_element(by=AppiumBy.ID, value="digit_6")
num7 = driver.find_element(by=AppiumBy.ID, value="digit_7")
num8 = driver.find_element(by=AppiumBy.ID, value="digit_8")
num9 = driver.find_element(by=AppiumBy.ID, value="digit_9")
num0 = driver.find_element(by=AppiumBy.ID, value="digit_0")

# Operadores
multiplicar = driver.find_element(by=AppiumBy.ID, value="op_mul")
divisao = driver.find_element(by=AppiumBy.ID, value="op_div")
soma = driver.find_element(by=AppiumBy.ID, value="op_add")
subtracao = driver.find_element(by=AppiumBy.ID, value="op_sub")
igualdade = driver.find_element(by=AppiumBy.ID, value="eq")


#SOMA
#time.sleep(2) #wait implícito
#num1.click()
#soma.click()
#time.sleep(2)
#num5.click()
#igualdade.click()
#time.sleep(2)
#resultado = driver.find_element(by=AppiumBy.ID, value="result_final")
#resultado.click()

#soma = int(resultado.text)
#print('O resultado da soma via Appium foi: ', soma)


#SUBTRACAO
#time.sleep(2) #wait implícito
#num9.click()
#subtracao.click()
#time.sleep(2)
#num5.click()
#igualdade.click()
#time.sleep(2)
#resultado = driver.find_element(by=AppiumBy.ID, value="result_final")
#resultado.click()

#subtracao = int(resultado.text)
#print('O resultado da subtração via Appium foi: ', subtracao)

#MULTIPLICAÇÃO
time.sleep(2) #wait implícito
num7.click()
multiplicar.click()
time.sleep(2)
num5.click()
igualdade.click()
time.sleep(2)
resultado = driver.find_element(by=AppiumBy.ID, value="result_final")
resultado.click()

multiplicacao = int(resultado.text)
print('O resultado da multiplicação via Appium foi: ', multiplicacao)
assert multiplicacao == int(resultado.text), 'Resultados OK!'
print('Resultados '+ multiplicacao + ' é um inteiro')

#DIVISAO
#time.sleep(2) #wait implícito
#num9.click()
#divisao.click()
#time.sleep(2)
#num3.click()
#igualdade.click()
#time.sleep(2)
#resultado = driver.find_element(by=AppiumBy.ID, value="result_final")
#resultado.click()

#divisao = int(resultado.text)
#print('O resultado da divisão via Appium foi: ', divisao)

#TearDown
driver.quit()
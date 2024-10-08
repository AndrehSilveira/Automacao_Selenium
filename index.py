from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

navegador = webdriver.Chrome()

navegador.get("http://ri.magazineluiza.com.br/")
navegador.find_element(By.XPATH, '//*[@id="ContentInternal_linkCentral"]').click()
element = navegador.find_element(By.XPATH, '//*[@id="ContentInternal_ContentPlaceHolderConteudo_rptResultados_linkArq_Release1T_0"]/img')

action = webdriver.ActionChains(navegador)
action.context_click(element).perform() #clica com o botão direito

time.sleep(1)

pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')

time.sleep(3)

#input()

driver.quit()
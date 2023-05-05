import pyautogui
import pyperclip
import time
import pandas as pd

user = str(input("Qual o usuário do sistema Fraction? "))
passwd = str(input(f"Qual a senha do usuário {user}? "))

def open_jad():
    pyautogui.press("win") #Aperta tecla do windows
    pyautogui.write("chromium") # Escreve firefox na aba de procurar
    pyautogui.press("enter") # Enter para abrir o programa
    time.sleep(3) # Espera carregar o browser

    pyautogui.write("http://jadlog.com/FractionWeb/login.jad?state=invalid") # Seleciona a página que será utilizada
    pyautogui.press("enter") # Aperta enter
    time.sleep(2) # Espera carregar a página

    pyautogui.write(user) # Escreve o usuário
    pyautogui.press("tab")# Aperta TAB
#    click_on_options("screenshts/Senha.png", 2)# 2 clicks no campo senha do usuário para selecionar todo o conteúdo
    pyautogui.write(passwd) # Escreve senha
    pyautogui.press("tab")# Aperta TAB
    pyautogui.press("enter") # Aperta Enter
 
def click_on_options(screenshot, times, sleep_time):
    time.sleep(sleep_time)# Espera por precaução para carregar as opções
    cords = pyautogui.locateCenterOnScreen(screenshot) # Localiza o que se deseja clicar na tela
    pyautogui.click(cords, clicks=times)# Clica no que deseja e quantos clicks deseja

open_jad()
time.sleep(1)
click_on_options("screenshts/Financeiro_chrome_dark.png", 1, 2)
#click_on_options("screenshts/Faturamento.png", 1)
click_on_options("screenshts/Folha_Apoio_chrome_dark.png", 1, 1)
import pyautogui
import pyperclip
import time
import pandas as pd

def open_jad():
    pyautogui.press("win") #Aperta tecla do windows
    pyautogui.write("chromium") # Escreve firefox na aba de procurar
    pyautogui.press("enter") # Enter para abrir o programa
    time.sleep(2) # Espera carregar o browser

    pyautogui.write("http://jadlog.com/FractionWeb/login.jad?state=invalid") # Seleciona a página que será utilizada
    pyautogui.press("enter") # Aperta enter
    time.sleep(3) # Espera carregar a página

    pyautogui.write(user) # Escreve o usuário
    pyautogui.press("tab")# Aperta TAB
    pyautogui.write(passwd) # Escreve senha
    pyautogui.press("tab")# Aperta TAB
    pyautogui.press("enter") # Aperta Enter
 
def click_on_options(screenshot, times, sleep_time):
    time.sleep(sleep_time)# Espera por precaução para carregar as opções
    cords = pyautogui.locateCenterOnScreen(screenshot) # Localiza o que se deseja clicar na tela
    pyautogui.click(cords, clicks=times)# Clica no que deseja e quantos clicks deseja




user = str(input("Qual o usuário do sistema Fraction? "))
passwd = str(input(f"Qual a senha do usuário {user}? "))
cc = str(input("Qual a conta corrente a ser gerado o boleto? "))
open_jad()
click_on_options("screenshts/Financeiro_chrome_dark.png", 1, 1)
click_on_options("screenshts/Folha_Apoio_chrome_dark.png", 1, 1)
time.sleep(0.5)
pyautogui.press("f5")# Aperta f5 para carregar a página
click_on_options("screenshts/Boleto.png", 1, 0.5) # Clica no campo Boleto
click_on_options("screenshts/Correntista.png", 1, 0.5) # Clica no campo Correntista
pyautogui.press("tab")# Aperta TAB
pyautogui.write(cc) # Escreve a conta desejada
pyautogui.click(x=2534, y=567) # Clica no campo DAta
pyautogui.write("30/04/22") # Fechamento 2° quinzena
# pyautogui.write("15/04/22") # fechamento 1° quinzena
click_on_options("screenshts/pdf.png", 1, 0.5) # Gera o PDF
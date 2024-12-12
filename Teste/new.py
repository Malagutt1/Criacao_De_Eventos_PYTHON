import pyautogui 
import time
def login_sigaa():
    pyautogui.press("win")
    pyautogui.write("Chrome")
    pyautogui.press("Enter")
    pyautogui.press("control"+"shift"+"n") 
    time.sleep(2)
    pyautogui.write("https://sigaa.ifsc.edu.br/sigaa/verTelaLogin.do")
    pyautogui.press("Enter")
    time.sleep(2)
    pyautogui.click(x=790, y=384)
    pyautogui.write("david.js2007")
    pyautogui.press("tab")
    pyautogui.write("Aovivoeacores1@")
    pyautogui.press("Enter")
    time.sleep(2)
    pyautogui.click(x=376, y=702)
    return

def login_sigaa_ja_logado():
    pyautogui.press("win")
    pyautogui.write("Chrome")
    pyautogui.press("Enter")
    time.sleep(2)
    pyautogui.write("https://sigaa.ifsc.edu.br/sigaa/verTelaLogin.do")
    pyautogui.press("Enter")
    time.sleep(2)
    pyautogui.click(x=793, y=491)
    time.sleep(5)
    pyautogui.click(x=392, y=627)
    return

eu=input("Escolha um numero: ")
if eu == "1":
   login_sigaa()
elif eu =="2":
    login_sigaa_ja_logado()
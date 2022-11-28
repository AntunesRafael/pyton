from time import sleep
import pyautogui 

#ir para janela
pyautogui.hotkey('alt','tab')

sleep(1)

#exportar e configurar datas como var
with open('datas.txt','r') as data:
    for linha in data:
        dti = linha.split(',')[0]
        dtf = linha.split(',')[1]
        mes = linha.split(',')[2]
    #clicar e adicionar data 
    pyautogui.click(358,480,duration=1)
    pyautogui.write(dti)
    pyautogui.press('enter')
    pyautogui.write(dtf)
    pyautogui.click(361,567)
    sleep(0.9)
    pyautogui.click(691,525)
    sleep(0.4)
    pyautogui.click(776,475)
    pyautogui.write(mes)
    pyautogui.press('enter')
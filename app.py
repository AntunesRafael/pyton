from time import sleep
import pyautogui

sleep(2)

with open('DATAS.txt') as datas:
    for data in datas:
        datade = data.split(',')[2]
        dataate = data.split(',')[2]
        mes = data.split(',')[2]
#clicar no de e escrever a data
pyautogui.click(402, 455, duration=1); pyautogui.write(datade)
#clicar no até e escrever data e clicar para print
pyautogui.click(446, 489, duration=1); pyautogui.write(dataate); pyautogui.click(363, 585, duration=1)
#clicar em ok 
pyautogui.click(489, 581, duration=1)
#clicar em nome e digitar mes
pyautogui.click(689, 461, duration=1); pyautogui.write(mes)
#clicar em salvar
pyautogui.click(709, 509, duration=1)

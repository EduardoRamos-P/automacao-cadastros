#Importar bibliotecas
import pyautogui
import time

#esperar 5 segundos
time.sleep(5)

#pegar posição do mouse e armazena em uma variável
posicao = pyautogui.position()

#Imprimi a posição no terminal
print(posicao)
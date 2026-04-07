#Importar bibliotecas nescessárias para o código
import pyautogui
import time
#*impora a biblioteca "pandas" com o nome reduzido para apenas "pd"
import pandas as pd

#Dar uma pausa entre os comandos
pyautogui.PAUSE = 0.5
#Passo 1: Abrir navegador

#*Pressiona a tecla "windows"
pyautogui.press("win")
#*Digita chrome
pyautogui.write("chrome")
#*Pressiona "enter" e acessa o navegador
pyautogui.press("enter")
#*aguarda 5 segundos
time.sleep(5)

#Passo 2: Acessar o site da empressa

#*Digita o link na barra de pesquisa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
#*Pressiona "enter" e acessa o site
pyautogui.press("enter")
#*Pressiona "f11" para deixar em tela cheia
pyautogui.press("f11")
#*Espera 5 segundos 
time.sleep(5)
#Passo 3: Fazer login com a conta

#*Pressiona "tab" e entra no campo de digitação
pyautogui.press("tab")
#*Digita o Email
pyautogui.write("eduardorp47386666@gmail.com")
#*Pressiona "tab" e passa para o próximo campo
pyautogui.press("tab")
#*Digita a senha
pyautogui.write("edu123")
#*Pressiona "enter" e acessa a área de cadastro
pyautogui.press("enter")
time.sleep(5)
#Passo 4: Cadastrar produtos

#*Cria variável tabela com os valores estabelecidos na tabela em ".csv"
tabela = pd.read_csv("produtos.csv")
#*Cria uma lista com as colunas presentes na tabela
coluna = ["codigo","marca","tipo","categoria","preco_unitario","custo","obs"]
#*Passa por todas as linhas da tabela
for linha in tabela.index:
    #*Cria variável de contagem
    i = 0
    #*Digita todas as colunas antes de ir para a próxima linha
    while i < len(coluna):
        #*Pressiona "tab", passa por todos os campos de digitação e faz o retorno para o começo
        pyautogui.press("tab")
        if str(tabela.loc[linha,coluna[i]]) != "nan":
            pyautogui.write(str(tabela.loc[linha,coluna[i]]))
        i = i+1
    #*Pressiona "enter" e cadastra o produto
    pyautogui.press("enter")
    #*Clica fora do campo de digitação
    pyautogui.click(x=236, y=419)
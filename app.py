import requests
import os
from tkinter import *


def libreoffice():
    url = "https://download.documentfoundation.org/libreoffice/portable/7.2.5/LibreOfficePortable_7.2.5_MultilingualStandard.paf.exe"
    r = requests.get(url, stream=True)
    with open("arquivo.exe", 'wb') as f:
        f.write(r.content)
        print('Arquivo baixado com sucesso.')
    os.system('arquivo.exe')


menu_inicial = Tk()
menu_inicial.title("Autoinstalador de Programas")
menu_inicial['background'] = 'beige'
# menu_inicial.geometry("500x250+200+200")
menu_inicial.resizable(True, False)

# menu_inicial.minsize(500,250)
# menu_inicial.maxsize(700,400)

# menu_inicial.state("zoomed")
# menu_inicial.state("iconic")

# Dimensões da janela
largura = 800
altura = 500


# Obtendo dimensões do sistema
largura_tela = menu_inicial.winfo_screenwidth()
altura_tela = menu_inicial.winfo_screenheight()
print(largura_tela, altura_tela)

# Posição da janela
posx = largura_tela/2 - largura
posy = altura_tela/2 - altura

# Definindo a centralização da janela na tela
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

# Colocando ícone no menu da janela
menu_inicial.iconbitmap("icons/regua.ico")


# Criação de um botão
botao = Button(menu_inicial, text="Executar", command=libreoffice)
# O menu_inicial será o pai deste botão, ou seja, o botão estará contido no menu_inicial
# Nessa situação o botão ainda não aparece. Para fazermos para que ele apareça, ele deve ter um pack
# Em resumo todos os Widgets deverão ter esse pack
botao.pack()


label1 = Label(menu_inicial, text="Esté o matias
")


menu_inicial.mainloop()

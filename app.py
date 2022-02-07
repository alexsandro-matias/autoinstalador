from cProfile import label
from tkinter import font
from turtle import width
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


# label1 = Label(menu_inicial, text="matias",
#                bg='white', fg='green', font="Times")

# label2 = Label(menu_inicial, text="matias",
#                bg='white', fg='black', font="Arial 20 bold italic")

# label3 = Label(menu_inicial, text="matias", fg="grey",
#                font="Verdana 20 bold")
# label1.pack()
# label2.pack()
# label3.pack()

# Outra possibilidade seria deixar o bg em Hexadecimal.
# RGB - (Red, Green, Blue) -> bg = "#ff0000" <- nesta ordem


# Para formatar a largura e altura do Label.
# label_1 = Label(menu_inicial, text="Este é um Label",
#                 bg="Red", font="Arial 20", width=20)
# label_1.pack()

# Com essa linha
# menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
# A fonte do label irá se adaptar à janela.

# Colocando texto diferentes no mesmo label em linhas separadas.
#

# Existe a possibilidade de fechar com o pack() diretamente
# quando instanciamos os objeto Label.
# Para isso, basta já colocar no final da instância criada.
# label_1 = Label(
#     menu_inicial,
#     text="Frase1",
#     font="Arial 20"
# ).pack()

# Porém desta forma, não será mais possível realizar nenhuma alteração neste label.

# label_1 = Label(
#     menu_inicial,
#     text="Frase1\nFrase2",
#     font="Arial 20"
# )
# label_1.pack()

# Da mesma forma que as strings, o \n também permite a quebra de linha, ou seja,
# textos em várias linhas utilizando o mesmo objeto.

# Também é possível adicionar uma borda a esta label com o argumento borda.
# label_1 = Label(
#     menu_inicial,
#     text="solid",
#     border=15,  # Espessura da linha em pixels
#     relief="solid",  # forma como será a borda 1/6
#     font="Arial 20"
# )
# label_1.pack()
# label_1 = Label(
#     menu_inicial,
#     text="flat",
#     border=15,  # Espessura da linha em pixels
#     relief="flat",  # forma como será a borda 1/6
#     font="Arial 20"
# )
# label_1.pack()


# label_1 = Label(
#     menu_inicial,
#     text="Frase1\nFrase2",
#     border=15,  # Espessura da linha em pixels
#     relief="flat",  # forma como será a borda 1/6
#     font="Arial 20"
# )
# label_1 = Label(
#     menu_inicial,
#     text="raise",
#     border=15,  # Espessura da linha em pixels
#     relief="raise",  # forma como será a borda 1/6
#     font="Arial 20"
# )
# label_1.pack()


# label_1 = Label(
#     menu_inicial,
#     text="sunken",
#     border=20,  # Espessura da linha em pixels
#     relief="sunken",  # forma como será a borda 1/6
#     font="Arial 20"
# )
# label_1.pack()


# label_1 = Label(
#     menu_inicial,
#     text="ridge",
#     border=15,  # Espessura da linha em pixels
#     relief="ridge",  # forma como será a borda 1/6
#     font="Arial 20"
# )
# label_1.pack()

# label_1 = Label(
#     menu_inicial,
#     text="groove",
#     border=20,  # Espessura da linha em pixels
#     relief="groove",  # forma como será a borda 1/6
#     font="Arial 20"
# )
# label_1.pack()

# # Tipos de Relief:
# # Solid
# # flat
# # raise
# # sunken
# # ridge
# # groove


# Altura do label

# Label_1 = Label(
#     menu_inicial,
#     text="Frase de teste\nFrase de teste",
#     font="Arial 20",
#     bd=10,
#     width=27,
#     height=6,  # Altura de duas linhas ou frases
#     relief="solid",
#     # anchor=SW  # Pontos cardeais que orientam o texto no label
#     anchor=CENTER  # centralizado
# ).pack()
# # No caso acima, quando diminuimos o width, mais o texto vai sendo cortado.


# Outra forma de configuração dos atributos. Através do dicionário interno do objeto.
label2 = Label(menu_inicial)
label2['text'] = 'texto da label2.'
label2['font'] = 'Arial 20'
label2['bd'] = 1
label2['relief'] = "solid"
label2.pack()

# # Como se trata de um dicionário,
# # já possível verificar as chaves e os valores deste dicionário.

# for item in label2.keys():
#     print(item, " : ", label2[item])


# Aula 016 - Python tkinter - LABEL TEXTVARIABLE E STRINGVAR


texto = StringVar()
texto.set("Alexsandro")

# label3 = Label(menu_inicial, text=texto,
#                font="Arial 20", bg="red", fg="white")
# Nessa situação, o que será mostrado será referência da variável - PY_VAR0.
# Para isso, existe uma chave dentro do Tkinter chamada textvariable que pode receber
# o valor de texto.

label3 = Label(menu_inicial, textvariable=texto,
               font="Arial 20", bg="red", fg="grey")

label3.pack()


# Parei na aula 017 - Python tkinter - INTRODUÇÃO AO LAYOUT EM GRID
menu_inicial.mainloop()

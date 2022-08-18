from cProfile import label
import tkinter as tk
from tkinter import *
import os
from turtle import color


# Estrutura do app
root = tk.Tk()
root.geometry("404x550")
fundo = PhotoImage(file="background-jv.png")
label1 = Label(root, image=fundo)
label1.place(x=0, y=0)
root.title("JOGO DA VELHA")

# Variaveis do jogo
quad1 = StringVar()
quad2 = StringVar()
quad3 = StringVar()
quad4 = StringVar()
quad5 = StringVar()
quad6 = StringVar()
quad7 = StringVar()
quad8 = StringVar()
quad9 = StringVar()
vitoria1 = StringVar()
vitoria2 = StringVar()
velha = StringVar()
vencedor = StringVar()

# Definição da interface do jogo
simboloX = "X"
simboloO = "O"
clear = ""
rodada = 0
verifywin = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
v1 = ""
v2 = ""
v = ""
vitoria1.set("0")
vitoria2.set("0")
velha.set("0")

# Função de verificação de qual player ganhou ou se deu velha


def playerwin(player, velha):
    global quad1
    global verifywin
    global v1

    if (verifywin[0][0] == player) and (verifywin[1][0] == player) and (verifywin[2][0] == player):

        if player == "X":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 1\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("X")
        elif player == "O":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 2\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("O")

    elif (verifywin[0][1] == player) and (verifywin[1][1] == player) and (verifywin[2][1] == player):

        if player == "X":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 1\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("X")
        elif player == "O":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 2\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("O")

    elif (verifywin[0][2] == player) and (verifywin[1][2] == player) and (verifywin[2][2] == player):

        if player == "X":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 1\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("X")
        elif player == "O":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 2\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("O")

    elif (verifywin[0][0] == player) and (verifywin[0][1] == player) and (verifywin[0][2] == player):

        if player == "X":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 1\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("X")
        elif player == "O":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 2\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("O")

    elif (verifywin[1][0] == player) and (verifywin[1][1] == player) and (verifywin[1][2] == player):

        if player == "X":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 1\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("X")
        elif player == "O":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 2\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("O")

    elif (verifywin[2][0] == player) and (verifywin[2][1] == player) and (verifywin[2][2] == player):

        if player == "X":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 1\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("X")
        elif player == "O":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 2\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("O")

    elif (verifywin[0][0] == player) and (verifywin[1][1] == player) and (verifywin[2][2] == player):

        if player == "X":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 1\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("X")
        elif player == "O":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 2\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("O")

    elif (verifywin[0][2] == player) and (verifywin[1][1] == player) and (verifywin[2][0] == player):

        if player == "X":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 1\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("X")
        elif player == "O":
            vencedor.set("VITÓRIA!!\n\n\nPLAYER 2\n GANHOU O JOGO!!")
            textovitoria.place(x=10, y=8)
            placar("O")

    elif velha == 9:
        vencedor.set("DEU VELHA!!")
        textovitoria.place(x=10, y=8)
        placar("V")

# Função que controla dados do placar


def placar(player):
    global v1
    global v2
    global v

    if player == "X":
        v1 = v1 + "+1"
        res = str(eval(v1))
        vitoria1.set(res)
        v1 = res

    elif player == "O":
        v2 = v2 + "+1"
        res = str(eval(v2))
        vitoria2.set(res)
        v2 = res

    elif player == "V":
        v = v + "+1"
        res = str(eval(v))
        velha.set(res)
        v = res

# Função que reseta o jogo


def restart():
    global rodada
    global verifywin

    rodada = 0
    quad1.set("")
    quad2.set("")
    quad3.set("")
    quad4.set("")
    quad5.set("")
    quad6.set("")
    quad7.set("")
    quad8.set("")
    quad9.set("")
    verifywin = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    textovitoria.place_forget()

# Função de escolha da posição no tabuleiro


def escolha(quad, x, y):
    global simboloX
    global simboloO
    global clear
    global rodada
    global verifywin

    rodada = rodada + 1

    if (rodada == 1) or (rodada == 3) or (rodada == 5) or (rodada == 7) or (rodada == 9):
        clear = str(simboloX)
        quad.set(clear)
        verifywin[x][y] = clear
        playerwin(simboloX, rodada)

    if (rodada == 2) or (rodada == 4) or (rodada == 6) or (rodada == 8):
        clear = str(simboloO)
        quad.set(clear)
        verifywin[x][y] = clear
        playerwin(simboloO, rodada)


# Criação dos textos e botões do jogo
c0l0 = tk.Button(root, textvariable=quad1, command=lambda: escolha(
    quad1, 0, 0), width=3, height=1, font=["Maiandra GD", 48, "bold"], background="#0006ff", foreground="white")
c0l0.place(x=10, y=12)

c0l1 = tk.Button(root, textvariable=quad2, command=lambda: escolha(
    quad2, 1, 0), width=3, height=1, font=["Maiandra GD", 48, "bold"], background="#0006ff", foreground="white")
c0l1.place(x=10, y=155)

c0l2 = tk.Button(root, textvariable=quad3, command=lambda: escolha(
    quad3, 2, 0), width=3, height=1, font=["Maiandra GD", 48, "bold"], background="#0006ff", foreground="white")
c0l2.place(x=10, y=300)

c1l0 = tk.Button(root, textvariable=quad4, command=lambda: escolha(
    quad4, 0, 1), width=3, height=1, font=["Maiandra GD", 48, "bold"], background="#0006ff", foreground="white")
c1l0.place(x=140, y=12)

c1l1 = tk.Button(root, textvariable=quad5, command=lambda: escolha(
    quad5, 1, 1), width=3, height=1, font=["Maiandra GD", 48, "bold"], background="#0006ff", foreground="white")
c1l1.place(x=140, y=155)

c1l2 = tk.Button(root, textvariable=quad6, command=lambda: escolha(
    quad6, 2, 1), width=3, height=1, font=["Maiandra GD", 48, "bold"], background="#0006ff", foreground="white")
c1l2.place(x=140, y=300)

c2l0 = tk.Button(root, textvariable=quad7, command=lambda: escolha(
    quad7, 0, 2), width=3, height=1, font=["Maiandra GD", 48, "bold"], background="#0006ff", foreground="white")
c2l0.place(x=270, y=12)

c2l1 = tk.Button(root, textvariable=quad8, command=lambda: escolha(
    quad8, 1, 2), width=3, height=1, font=["Maiandra GD", 48, "bold"], background="#0006ff", foreground="white")
c2l1.place(x=270, y=155)

c2l2 = tk.Button(root, textvariable=quad9, command=lambda: escolha(
    quad9, 2, 2), width=3, height=1, font=["Maiandra GD", 48, "bold"], background="#0006ff", foreground="white")
c2l2.place(x=270, y=300)

win1 = tk.Label(root, textvariable=vitoria1, width=1, height=0, font=[
    "Maiandra GD", 14, "bold"], foreground="white", background="#0006ff")
win1.place(x=138, y=447)

win2 = tk.Label(root, textvariable=vitoria2, width=1, height=0, font=[
    "Maiandra GD", 14, "bold"], foreground="white", background="#0006ff")
win2.place(x=138, y=477)

winv = tk.Label(root, textvariable=velha, width=1, height=0, font=[
    "Maiandra GD", 14, "bold"], foreground="white", background="#0006ff")
winv.place(x=138, y=507)

reset = tk.Button(root, text="REINICIAR", command=restart, width=9, height=1, font=[
    "Maiandra GD", 15, "bold"], border=3, relief="solid", foreground="white", background="#0006ff")
reset.place(x=240, y=448)

fechar = tk.Button(root, text="FECHAR", command=root.quit, width=9, height=1, font=[
    "Maiandra GD", 15, "bold"], border=3, relief="solid", foreground="white", background="#0006ff")
fechar.place(x=240, y=495)

textovitoria = tk.Label(root, textvariable=vencedor, width=29, height=17, font=[
    "Maiandra GD", 16, "bold"], foreground="white", background="#0006ff")


root.mainloop()

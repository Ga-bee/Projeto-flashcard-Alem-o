from tkinter import *
import pandas as pd
from random import choice

#Dicionário que recebe a palavra escolhida em Alemão
escolhido = {}
cor_de_fundo = "#B1DDC6"

#Lê arquivo que contém as palavras

try:
    dados = pd.read_csv('../data/palavras_a_aprender.csv')
except FileNotFoundError:
    file = pd.read_csv('../data/German_words.txt.csv')
    a_aprender = file.to_dict(orient='records')
else:
    a_aprender = dados.to_dict(orient="records")

# print(file_file)


##----------------------Apaga as palavras conhecidas------------------
#Ativado ao clicar no botão "acerto"
def is_known():
    a_aprender.remove(escolhido)
    generate_words()
    dados = pd.DataFrame(a_aprender)
    dados.to_csv('../data/german_words.txt.csv',index=False)


##--------------------- Gera novas palavras -----------------------

def generate_words():
    global escolhido
    #Escolhe uma palavra aleatóriamente do arquivo

    escolhido = choice(a_aprender)
    # print(escolhido, escolhido["German"])

    #Muda no cartão a lingua e a palavra para alemão e palavra escolhida
    canvas.itemconfig(texto_lingua, text="German")
    canvas.itemconfig(texto_palavra, text=escolhido["German"])
    label_palavra.config(text=escolhido["German"])

    canvas.itemconfig(card_image, image= card_front)


    #cofigura o tempo até trocar a lingua e tradução
    window.after(5000, original_language)

#    word_label.config(text=words["Portuguese"])


# ##---------------------- UI Setup ----------------------------

window = Tk()
window.title('Flashcard App')
window.config(padx=50,pady=50,bg=cor_de_fundo)

#imagens do cartão
card_back = PhotoImage(file="../images/card_back.png")
card_front = PhotoImage(file="../images/card_front.png")

#imagens dos botões
imagem_botao_acerto=PhotoImage(file="../images/right.png")
imagem_botao_errado=PhotoImage(file="../images/wrong.png")

#ação do botão erro -> gera nova palavra
botao_erro = Button(image=imagem_botao_errado, highlightthickness=0,command=generate_words)
botao_erro.grid(row=1,column=0)

#ação do botão acerto -> apaga a palavra da lista(a mesma não volta a aparecer) e gera nova palavra
botao_acerto = Button(image=imagem_botao_acerto, highlightthickness=0,command=is_known)
botao_acerto.grid(row=1,column=1)

#Labels
label_lingua = Label(font=('Arial', 40, 'italic'), text='German')
label_palavra = Label(font=('Arial', 60, 'bold'), text='Portuguese')

#configura tela
canvas = Canvas(width=800,height=526)
card_image = canvas.create_image(400,263,image= card_front)
texto_lingua =  canvas.create_text(400,100,text='language', font=('Arial', 40, 'italic'))
texto_palavra = canvas.create_text(400,250,text='word', font=('Arial', 60, 'bold'))


canvas.config(bg= cor_de_fundo, highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)


def original_language():
    #Troca a lingua e traduz a palavra
    canvas.itemconfig(card_image,image= card_back)
    canvas.itemconfig(texto_lingua ,text='Portuguese')
    canvas.itemconfig(texto_palavra,text=escolhido["Portuguese"])
window.after(10,generate_words )
window.after(5000, original_language)



window.mainloop()
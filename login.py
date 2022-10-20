import time
from tkinter import *
from PIL import Image, ImageTk


ARQ_email = "arqv/email.txt"
ARQ_password = "arqv/password.txt"

def login():
  
  if tb_email.get() != "" and tb_password.get() != "":
      
    with open(ARQ_email,"r") as email:
      mail = email.read()
      if tb_email.get() == mail:
        print("Email correto")
      else:
        print("Email errado")
    email.close()
    
    
    
    with open(ARQ_password,"r") as password:
      passs = password.read()
      if tb_password.get() == passs:
        print("Password correto")
        tb_login_mensagem["text"] = 'login successfully :)'
      else:
        print("Password errado")
        tb_login_mensagem["text"] = 'wrong email or password :('
    password.close()
    
    

    text_email = ''
    text_password = ''
    tb_texto_email["text"] = text_email
    tb_texto_password["text"] = text_password
    tb_email.delete(0,END)
    tb_password.delete(0,END)
  
  else:
    text_email = 'Type your e-mail'
    text_password = "enter your password"
      
    tb_texto_email["text"] = text_email
    tb_texto_password["text"] = text_password
   
      
def Fechar():
  exit()
  
  
  
  
  
  
  
janela = Tk()
janela.title("Painel de Login")
img = ImageTk.PhotoImage(Image.open("arqv/ADICIONAR.png"))
label = Label(janela,image=img)
label.pack()

tb_email = Entry(janela)
tb_email.place(x=538,y=260,width=200,height=35)

tb_password = Entry(janela)
tb_password.place(x=538,y=350,width=200,height=35)

tb_botao = Button(janela,text="Login",command=login,activebackground="green", font=("arial",20))
tb_botao.place(x=559,y=421,width=172,height=47)

tb_texto_email = Label(janela, text="",background="black", foreground="red")
tb_texto_email.place(x=570,y=215,width=200,height=35)

tb_texto_password = Label(janela, text="",background="black", foreground="red")
tb_texto_password.place(x=620,y=305,width=200,height=35)


bt_sair = Button(janela,text="close", command=Fechar,activebackground="red")
bt_sair.place(x=20,y=8)


tb_login_mensagem = Label(janela, text="", background="black", foreground="red")
tb_login_mensagem.place(x=559,y=490)

#tb_login_successfully =  Label(janela, text="", background="black", foreground="green")
#tb_login_successfully.place(x=559,y=510)
janela.mainloop()

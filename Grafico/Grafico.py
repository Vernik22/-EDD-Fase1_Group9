from tkinter import *  #ventana
from tkinter import Menu    #menu
from tkinter import filedialog      # filechooser
from tkinter import scrolledtext    # textarea
from tkinter import messagebox      # message box
from tkinter import ttk             #combobox
import os


class Grafico:
   
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("1000x600")
        self.ventana.title(" [EDD] Fase-1" )
        self.ventana.configure(bg = '#F5A903')

        self.menu = Menu(self.ventana)

    

        self.ventana.config(menu=self.menu)

        self.txtEntrada = Entry(self.ventana,width=10)
        self.labelEntrada = Label(self.ventana, text='Entrada',bg='#F5A903')
        self.txtConsola = Entry(self.ventana,width=10)
        self.labelConsola = Label(self.ventana,text='Consola',bg='#F5A903')
        self.txtFilas = Entry(self.ventana, width=5 )

        self.txtEntrada = scrolledtext.ScrolledText(self.ventana, width=112,height=18)
        self.txtEntrada.place(x=42, y=30)
        self.labelEntrada.place(x=20, y=1)

        self.txtFilas.place(x=12, y= 30, width= 25 , height=293)
        self.txtConsola = scrolledtext.ScrolledText(self.ventana, width=70,height=10)
        self.txtConsola.place(x=12, y=390)
        self.labelConsola.place(x=12, y=370 )

        self.analiButton = Button(self.ventana, text= 'Analizar', padx= 25, pady=12, bg= 'grey',fg='white',command = self.ven2)
        self.analiButton.place(x=455, y=335)

        self.combo = ttk.Combobox(self.ventana,state="readonly",values= ["Elegir Lenguaje","Css","Js", "Html", "Rtm"] )
        self.combo.current(0)
        self.combo.place(x=455 ,y=3)


        self.ventana.mainloop()
    
    def ven2(self):
        ven2 = tablas()

class tablas:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("1000x600")
        self.ventana.title(" [EDD] Fase-1" )
        self.ventana.configure(bg = '#F5A903')

        self.ventana.mainloop()

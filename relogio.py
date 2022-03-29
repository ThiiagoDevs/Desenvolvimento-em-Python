import tkinter as tk
import datetime


class Telaprincipal:
    def __init__(self, master):
        self.nossaTela = master
        self.lblRelogio = tk.Label(
            self.nossaTela, font=('calibri', 26), fg='purple')
        self.lblRelogio.pack(pady=30, padx=30)
        self.alteracao()

    def alteracao(self):
        now = datetime.datetime.now()
        self.lblRelogio['text'] = now.strftime('%H:%M:%S')
        self.nossaTela.after(1000, self.alteracao)


janelaRaiz = tk.Tk()
Telaprincipal(janelaRaiz)
janelaRaiz.mainloop()

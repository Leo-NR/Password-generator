import tkinter as tk
import random

def gerar_senha():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*"
    senha_nova = "".join(random.choices(caracteres, k=12))
    texto_resultado["text"] = senha_nova

janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("300x200")

botao = tk.Button(janela, text="Gerar Senha Segura", command=gerar_senha)
botao.pack(pady=30)

texto_resultado = tk.Label(janela, text="Sua senha aparecerá aqui", font=("Arial", 14))
texto_resultado.pack()

janela.mainloop()

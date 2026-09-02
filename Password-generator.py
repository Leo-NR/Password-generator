import random
import string
import tkinter as tk
from tkinter import messagebox

textos = {
    "pt": {
        "titulo": "Gerador de Senhas Seguras",
        "tamanho": "Tamanho da Senha:",
        "letras": "Incluir Letras (A-Z)",
        "numeros": "Incluir Números (0-9)",
        "simbolos": "Incluir Símbolos (!@#)",
        "gerar": "Gerar Senha",
        "copiar": "Copiar Senha",
        "aviso_titulo": "Aviso",
        "aviso_msg": "Selecione pelo menos um tipo de caractere!",
        "sucesso_titulo": "Sucesso",
        "sucesso_msg": "Senha copiada para a área de transferência!",
        "padrao": "Sua senha aparecerá aqui"
    },
    "en": {
        "titulo": "Secure Password Generator",
        "tamanho": "Password Length:",
        "letras": "Include Letters (A-Z)",
        "numeros": "Include Numbers (0-9)",
        "simbolos": "Include Symbols (!@#)",
        "gerar": "Generate Password",
        "copiar": "Copy Password",
        "aviso_titulo": "Warning",
        "aviso_msg": "Select at least one character type!",
        "sucesso_titulo": "Success",
        "sucesso_msg": "Password copied to clipboard!",
        "padrao": "Your password will appear here"
    }
}

idioma_atual = "pt"

def mudar_idioma(novo_idioma):
    global idioma_atual
    idioma_atual = novo_idioma
    atualizar_textos()

def atualizar_textos():
    t = textos[idioma_atual]
    lbl_titulo.config(text=t["titulo"])
    lbl_tamanho.config(text=t["tamanho"])
    chk_letras.config(text=t["letras"])
    chk_numeros.config(text=t["numeros"])
    chk_simbolos.config(text=t["simbolos"])
    btn_gerar.config(text=t["gerar"])
    btn_copiar.config(text=t["copiar"])
    
    if texto_resultado.cget("text") in [textos["pt"]["padrao"], textos["en"]["padrao"]]:
        texto_resultado.config(text=t["padrao"])

def gerar_senha():
    t = textos[idioma_atual]
    tamanho = int(slider_tamanho.get())
    
    caracteres = ""
    if var_letras.get():
        caracteres += string.ascii_letters
    if var_numeros.get():
        caracteres += string.digits
    if var_simbolos.get():
        caracteres += string.punctuation
        
    if not caracteres:
        messagebox.showwarning(t["aviso_titulo"], t["aviso_msg"])
        return

    senha_nova = "".join(random.choices(caracteres, k=tamanho))
    texto_resultado.config(text=senha_nova)

def copiar_senha():
    t = textos[idioma_atual]
    senha = texto_resultado.cget("text")
    if senha and senha != t["padrao"]:
        janela.clipboard_clear()
        janela.clipboard_append(senha)
        messagebox.showinfo(t["sucesso_titulo"], t["sucesso_msg"])

janela = tk.Tk()
janela.title("Gerador de Senhas / Password Generator")
janela.geometry("350x430")
janela.resizable(False, False)

frame_idioma = tk.Frame(janela)
frame_idioma.pack(pady=5)
tk.Button(frame_idioma, text="PT 🇧🇷", width=5, command=lambda: mudar_idioma("pt")).pack(side=tk.LEFT, padx=5)
tk.Button(frame_idioma, text="EN 🇺🇸", width=5, command=lambda: mudar_idioma("en")).pack(side=tk.LEFT, padx=5)

lbl_titulo = tk.Label(janela, text="Gerador de Senhas Seguras", font=("Arial", 14, "bold"))
lbl_titulo.pack(pady=10)

lbl_tamanho = tk.Label(janela, text="Tamanho da Senha:")
lbl_tamanho.pack()
slider_tamanho = tk.Scale(janela, from_=6, to=32, orient=tk.HORIZONTAL)
slider_tamanho.set(12)
slider_tamanho.pack()

var_letras = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

chk_letras = tk.Checkbutton(janela, text="Incluir Letras (A-Z)", variable=var_letras)
chk_letras.pack(anchor="w", padx=70)
chk_numeros = tk.Checkbutton(janela, text="Incluir Números (0-9)", variable=var_numeros)
chk_numeros.pack(anchor="w", padx=70)
chk_simbolos = tk.Checkbutton(janela, text="Incluir Símbolos (!@#)", variable=var_simbolos)
chk_simbolos.pack(anchor="w", padx=70)

btn_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_gerar.pack(pady=15)

texto_resultado = tk.Label(janela, text="Sua senha aparecerá aqui", font=("Arial", 11), fg="blue", wraplength=320)
texto_resultado.pack(pady=5)

btn_copiar = tk.Button(janela, text="Copiar Senha", command=copiar_senha)
btn_copiar.pack(pady=5)

janela.mainloop()
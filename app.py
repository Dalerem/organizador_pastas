'''
import os
import shutil

def organizador_pastas(diretorio):
    tipos = {
        'Documentos': ['.docx', '.doc', '.xlxs', '.csv', '.txt', '.ppsx', '.ods', '.odt', '.odp', '.pdf'],
        'Imagens': ['.jpg', '.png', '.odg', '.jpeg', '.bmp'],
        'Vídeos': ['.mp4', '.mov', '.avi'],
        'Áudios': ['.mp3', '.wav'],
        'Programas': ['.exe']
    }

    for pasta in tipos.keys():
        caminho = os.path.join(diretorio, pasta)
        if not os.path.exists(caminho):
            os.makedirs(caminho)
        
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_arquivo):
            _, extensao = os.path.splitext(arquivo)
            for pasta, extensoes in tipos.items():
                if extensao.lower() in extensoes:
                    destino = os.path.join(diretorio, pasta, arquivo)
                    shutil.move(caminho_arquivo, destino)
                    print(f'Movido: {arquivo} -> {pasta}')
                    break

if __name__ == '__main__':
    organizador_pastas(r'D:\Documentos\Fotos_tudo\variados\VanessaSipros')
'''
'''
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organizador_pastas(diretorio):
    tipos = {
        'Documentos': ['.docx', '.doc', '.xlsx', '.csv', '.txt', '.ppsx', '.ods', '.odt', '.odp', '.pdf'],
        'Imagens': ['.jpg', '.png', '.odg', '.jpeg', '.bmp'],
        'Vídeos': ['.mp4', '.mov', '.avi'],
        'Áudios': ['.mp3', '.wav'],
        'Programas': ['.exe']
    }

    for pasta in tipos.keys():
        caminho = os.path.join(diretorio, pasta)
        if not os.path.exists(caminho):
            os.makedirs(caminho)

    movidos = []
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_arquivo):
            _, extensao = os.path.splitext(arquivo)
            for pasta, extensoes in tipos.items():
                if extensao.lower() in extensoes:
                    destino = os.path.join(diretorio, pasta, arquivo)
                    shutil.move(caminho_arquivo, destino)
                    movidos.append(f'{arquivo} -> {pasta}')
                    break
    return movidos

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        entrada_pasta.delete(0, tk.END)
        entrada_pasta.insert(0, pasta)

def organizar():
    pasta = entrada_pasta.get()
    if not pasta or not os.path.exists(pasta):
        messagebox.showerror("Erro", "Selecione um diretório válido!")
        return
    
    movidos = organizador_pastas(pasta)
    if movidos:
        messagebox.showinfo("Concluído", f"Arquivos organizados:\n\n" + "\n".join(movidos))
    else:
        messagebox.showinfo("Concluído", "Nenhum arquivo foi movido.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Organizador de Pastas")
janela.geometry("500x200")

# Widgets
tk.Label(janela, text="Selecione o diretório para organizar:", font=("Arial", 12)).pack(pady=10)

entrada_pasta = tk.Entry(janela, width=50)
entrada_pasta.pack(pady=5)

tk.Button(janela, text="Procurar", command=selecionar_pasta).pack(pady=5)
tk.Button(janela, text="Organizar", command=organizar).pack(pady=10)

# Rodar a interface
janela.mainloop()
'''

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def organizador_pastas(diretorio, progress_bar, label_percent, log_box):
    tipos = {
        'Documentos': ['.docx', '.doc', '.xlsx', '.csv', '.txt', '.ppsx', '.ods', '.odt', '.odp', '.pdf'],
        'Imagens': ['.jpg', '.png', '.odg', '.jpeg', '.bmp', '.gif', '.webp', '.svg', '.tiff'],
        'Vídeos': ['.mp4', '.mov', '.avi'],
        'Áudios': ['.mp3', '.wav']
    }

    # Criar pastas
    for pasta in tipos.keys():
        caminho = os.path.join(diretorio, pasta)
        if not os.path.exists(caminho):
            os.makedirs(caminho)

    arquivos = [a for a in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, a))]
    total = len(arquivos)
    movidos = []

    for i, arquivo in enumerate(arquivos, start=1):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        _, extensao = os.path.splitext(arquivo)
        for pasta, extensoes in tipos.items():
            if extensao.lower() in extensoes:
                destino = os.path.join(diretorio, pasta, arquivo)
                shutil.move(caminho_arquivo, destino)
                movidos.append(f'{arquivo} -> {pasta}')
                # Atualiza log em tempo real
                log_box.insert(tk.END, f"Movido: {arquivo} -> {pasta}")
                log_box.see(tk.END)
                break

        # Atualiza barra e porcentagem
        progresso = int((i / total) * 100)
        progress_bar['value'] = progresso
        label_percent.config(text=f"{progresso}%")
        janela.update_idletasks()

    return movidos

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        entrada_pasta.delete(0, tk.END)
        entrada_pasta.insert(0, pasta)

def organizar():
    pasta = entrada_pasta.get()
    if not pasta or not os.path.exists(pasta):
        messagebox.showerror("Erro", "Selecione um diretório válido!")
        return
    
    progress_bar['value'] = 0
    label_percent.config(text="0%")
    log_box.delete(0, tk.END)  # limpa log anterior
    
    movidos = organizador_pastas(pasta, progress_bar, label_percent, log_box)
    
    if movidos:
        messagebox.showinfo("Concluído", f"{len(movidos)} arquivos organizados com sucesso!")
    else:
        messagebox.showinfo("Concluído", "Nenhum arquivo foi movido.")
    
    # Limpa campo após concluir
    entrada_pasta.delete(0, tk.END)
    progress_bar['value'] = 100
    label_percent.config(text="100%")

# Criando janela principal
janela = tk.Tk()
janela.title("Organizador de Pastas")
janela.geometry("600x400")

# Widgets
tk.Label(janela, text="Selecione o diretório para organizar:", font=("Arial", 12)).pack(pady=10)

entrada_pasta = tk.Entry(janela, width=50)
entrada_pasta.pack(pady=5)

tk.Button(janela, text="Procurar", command=selecionar_pasta).pack(pady=5)
tk.Button(janela, text="Organizar", command=organizar).pack(pady=10)

# Barra de progresso + porcentagem
frame_progress = tk.Frame(janela)
frame_progress.pack(pady=10)

progress_bar = ttk.Progressbar(frame_progress, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(side="left", padx=5)

label_percent = tk.Label(frame_progress, text="0%")
label_percent.pack(side="left")

# Log em tempo real
tk.Label(janela, text="Log de arquivos movidos:", font=("Arial", 11)).pack(pady=5)
log_box = tk.Listbox(janela, width=80, height=10)
log_box.pack(pady=5)

# Rodar interface
janela.mainloop()
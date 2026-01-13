import tkinter as tk
import random
import time
import threading

GRID_SIZE = 12   # número de quadradinhos por linha/coluna
CELL_SIZE = 25   # tamanho de cada quadradinho

def iniciar_instalacao():
    botao_inicio.config(state="disabled")
    threading.Thread(target=rodar_instalacao, daemon=True).start()

def rodar_instalacao():
    etapas = [
        "Verificando compatibilidade cerebral...",
        "Copiando arquivos mentais...",
        "Expandindo pacotes neurais...",
        "Instalando interface fluida...",
        "Ativando módulo Anti‑Vírus Neural...",
        "Escaneando sinapses em busca de malware...",
        "Nenhuma ameaça encontrada. Sistema limpo!",
        "Finalizando instalação...",
        "Windows 11 instalado com sucesso no seu cérebro!"
    ]

    for etapa in etapas:
        status_var.set(etapa)
        # muda cores várias vezes para simular "instalação"
        for _ in range(20):
            for cell in cells:
                cor = "#%06x" % random.randint(0, 0xFFFFFF)
                canvas.itemconfig(cell, fill=cor)
            time.sleep(0.05)
        time.sleep(0.5)

    status_var.set("Instalação concluída!")
    botao_inicio.config(state="normal")

# Janela principal
root = tk.Tk()
root.title("Instalador Neural do Windows 11 + Anti‑Vírus")
root.configure(bg="black")
root.geometry("500x550")

status_var = tk.StringVar(value="Aguardando início...")

# Label de status
status_label = tk.Label(root, textvariable=status_var, fg="white", bg="black", font=("Consolas", 12))
status_label.pack(pady=10)

# Canvas com grade de quadradinhos
canvas = tk.Canvas(root, width=GRID_SIZE*CELL_SIZE, height=GRID_SIZE*CELL_SIZE, bg="black", highlightthickness=0)
canvas.pack(pady=20)

cells = []
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        x1 = j * CELL_SIZE
        y1 = i * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        cell = canvas.create_rectangle(x1, y1, x2, y2, fill="gray", outline="")
        cells.append(cell)

# Botão de início
botao_inicio = tk.Button(root, text="Começar Instalação", command=iniciar_instalacao,
                         bg="black", fg="white", font=("Consolas", 12))
botao_inicio.pack(pady=20)

root.mainloop()

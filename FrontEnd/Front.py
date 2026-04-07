import tkinter as tk
import Tradutor
import Request as RQ

def label_dinamico():
    # Atualização de Label dinâmico
    Atividade = RQ.buscar_atividade()
    Tradu = Tradutor.Traduzir_texto(Atividade)
    lblD.config(Tradu)


# primeira parte do front end:
root = tk.Tk()
root.title("FewNew")
root.geometry("400x400")

#Label de chamada
lbl1 = tk.Label(root, text="Clique no botão abaixo e receba uma nova ideia: ")
lbl1.pack(pady=20)

#Label Dinâmico
lblD = tk.Label(root,text=" ")
lblD.pack(pady=23)

    
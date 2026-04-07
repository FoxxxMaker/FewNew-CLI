import tkinter as tk
import Tradutor
import Request as RQ

def label_dinamico():
    try:
        # busca a atividade
        Atividade = RQ.buscar_atividade()
        # Atualização de Label dinâmico
        Tradu = Tradutor.Traduzir_texto(Atividade)
        lblD.config(text=Tradu)
    except Exception as ex:
        print("Erro na tradução:", ex)
    return 


# primeira parte do front end:
root = tk.Tk()
root.title("FewNew")
root.geometry("400x400")

#Label de chamada
lbl1 = tk.Label(root, text="Clique no botão abaixo e receba uma nova ideia: ")
lbl1.pack(pady=20)

#Label Dinâmico
lblD = tk.Label(root,text="Aperte o botão!")
lblD.pack(pady=23)

#Botão para o mudar o Label dinâmico
btn = tk.Button(root, text="Descubra!", command=label_dinamico)
btn.pack(pady=25)

print(RQ.buscar_atividade())

root.mainloop()    
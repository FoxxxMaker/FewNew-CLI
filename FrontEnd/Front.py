import tkinter as tk

class app:
    # primeira parte do front end:
    root = tk.Tk()
    root.title("FewNew")
    root.geometry("400x400")

    lbl1 = tk.Label(root, text="Clique no botão abaixo e receba uma nova ideia: ")
    lbl1.pack(pady=20)

    
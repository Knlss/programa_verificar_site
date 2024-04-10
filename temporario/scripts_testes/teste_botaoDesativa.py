import tkinter as tk

def mostrar_valor_variavel():
    print("Valor atual de variavel_apagar_depois:", variavel_apagar_depois.get())

def definir_valor_apagar_depois():
    if checkbox_var1.get():
        variavel_apagar_depois.set(0)
        checkbox2.config(state="disabled")
        mostrar_valor_variavel()
    else:
        checkbox2.config(state="normal")

# Criando a janela principal
janela = tk.Tk()
janela.title("Exemplo de Checkbutton")

# Variáveis de controle para os Checkbuttons
checkbox_var1 = tk.BooleanVar()
variavel_apagar_depois = tk.IntVar()

# Criando o primeiro Checkbutton
checkbox1 = tk.Checkbutton(janela, text="Apagar depois", variable=checkbox_var1, command=definir_valor_apagar_depois)
checkbox1.pack(anchor=tk.W)

# Criando o segundo Checkbutton
checkbox2 = tk.Checkbutton(janela, text="Outra opção", variable=variavel_apagar_depois, onvalue=757, offvalue=0, command=mostrar_valor_variavel)
checkbox2.pack(anchor=tk.W)

# Iniciando o loop da aplicação
janela.mainloop()

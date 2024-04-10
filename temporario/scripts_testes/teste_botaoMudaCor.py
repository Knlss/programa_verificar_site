import tkinter as tk

def mudar_cor(cor):
    botao_inicial.configure(bg=cor)

def toggle_menu():
    if menu_cores.winfo_ismapped():
        menu_cores.grid_forget()  # Oculta o menu de cores
    else:
        menu_cores.grid(row=1, column=0, sticky="ew")  # Exibe o menu de cores

# Criando a janela principal
janela = tk.Tk()
janela.title("Exemplo de Botão com Cores")

# Criando o botão inicial
botao_inicial = tk.Button(janela, text="☰", width=5, height=2, command=toggle_menu)
botao_inicial.grid(row=0, column=0, padx=10, pady=10)

# Criando o frame para o menu de cores
menu_cores = tk.Frame(janela)
cores = ["red", "green", "blue", "yellow", "orange", "purple"]

# Adicionando botões de cor ao menu
for i, cor in enumerate(cores):
    botao_cor = tk.Button(menu_cores, bg=cor, width=5, height=2, command=lambda c=cor: mudar_cor(c))
    botao_cor.grid(row=0, column=i, padx=5, pady=5)

# Ocultando o menu de cores inicialmente
menu_cores.grid_forget()

# Iniciando o loop da aplicação
janela.mainloop()

import tkinter as tk

# Criar janela principal
root = tk.Tk()
root.title("Janela Rolável")

# Criar uma scrollbar vertical
scrollbar = tk.Scrollbar(root, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Criar uma área de rolagem
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)

# Conectar a scrollbar à área de rolagem
scrollbar.config(command=canvas.yview)

# Função para adicionar mais conteúdo à janela
def add_content():
    canvas.create_text(200, y, text="Novo conteúdo", anchor="w")
    y += 20  # Atualizar a posição y para o próximo texto

# Adicionar algum conteúdo inicial à janela
y = 10
for i in range(20):
    canvas.create_text(200, y, text="Conteúdo " + str(i), anchor="w")
    y += 20

# Atualizar o scroll region para permitir a rolagem
canvas.config(scrollregion=canvas.bbox("all"))

# Conectar eventos de rolagem para rolar a janela principal
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

# Botão para adicionar mais conteúdo
add_button = tk.Button(root, text="Adicionar Conteúdo", command=add_content)
add_button.pack()

# Iniciar loop de eventos
root.mainloop()

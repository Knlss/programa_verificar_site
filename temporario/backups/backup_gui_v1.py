import tkinter as tk

def criar_janela():
    root = tk.Tk()
    return root

def criar_scrollbar(root):
    scrollbar = tk.Scrollbar(root, orient="vertical")
    scrollbar.pack(side="right", fill="y")
    return scrollbar

def criar_canvas(root, scrollbar):
    canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=canvas.yview)
    return canvas

def adicionar_texto(canvas, y):
    canvas.create_text(200, y, text="Conteúdo " + str(y//20), anchor="w")

def configurar_rolagem(canvas):
    def on_mouse_wheel(event):
        if event.delta < 0:
            if canvas.yview()[1] < 1.0:
                canvas.yview_scroll(1, "units")
        elif event.delta > 0:
            if canvas.yview()[0] > 0.0:
                canvas.yview_scroll(-1, "units")
    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

def atualizar_canvas(canvas):
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def main():
    root = criar_janela()
    scrollbar = criar_scrollbar(root)
    canvas = criar_canvas(root, scrollbar)

    y = 10
    for i in range(20):
        adicionar_texto(canvas, y)
        y += 20

    configurar_rolagem(canvas)
    atualizar_canvas(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()

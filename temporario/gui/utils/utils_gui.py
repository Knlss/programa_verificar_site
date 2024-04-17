import sys
import tkinter as tk

sys.path.append("temporario")

import gui.config.settings as settings

class CreateFrame:
    def __init__(self, father, height, width, anchor, relx, rely, bg, frame_type):
        self.frame_type = frame_type
        if self.frame_type == "place":
            self.frame = tk.Frame(father, height=height, width=width, bg=bg)
            self.frame.place(anchor=anchor, relx=relx, rely=rely)
        elif self.frame_type == "grid":
            father.grid_rowconfigure(0, weight=1)
            father.grid_columnconfigure((0, 1, 2), weight=1)
            self.frame = tk.Frame(father, width=width, bg=bg)
            self.frame.grid(row=height, column=anchor, sticky="nsew")
        elif self.frame_type == "pack":
            self.frame = tk.Frame(father, bg=bg)
            self.frame.pack(side=height, fill=width, expand=anchor)
        else:
            raise ValueError("Tipo de frame não suportado: {}".format(frame_type))
        
# ---------------------------------------------------------------------------------------------------------

class CreateElement:

    def create_button(self, father, height, width, anchor, relx, rely, bg, fg, font, text, command):
        self.frame = tk.Button(father, height=height, width=width, text=text, font=font, bg=bg, fg=fg, command=command)
        self.frame.place(anchor=anchor, relx=relx, rely=rely)

    def create_checkbutton(self, **info):
        self.frame = tk.Button(self.father, **info)

    def create_input(self, **info):
        self.frame = tk.Label(self.father, **info)
    
    def create_label(self, **info):
        self.frame = tk.Label(self.father, **info)
    
# ---------------------------------------------------------------------------------------------------------

"""

        Vou fazer o seguinte: seguindo a mesma lógica do createFrame, irei executar um metodo por vez
    informando uma lista de cada tipo por vez. Ela vai receber o mesmo tratamento da lista de frame info
    obtendo o pai com .pop e definindo numa variavel. Essa variavel vai ser usada para obter o valor do 
    pai do elemento atual que esta contido na lista de frames, e depois vai instanciar em cadeia um novo
    elemento, usando o metodo especifico do tipo, e passando a variavel father como pai, e **info como o 
    resto das informações. Nisso, numa outra lista chamada elements, que no caso é um dicionario, esse 
    elemento recem criado vai ser armazenado com .frame, ou seja, vai armazenar o proprio objeto tkinter,
    e como chave, vai ter seu nome que foi definido na lista de info do seu tipo particular

        Vou usar 4 dicionarios de dicionarios diferentes, um para botao, outro label, outro checkbutton, outro
    input. Acaba que terei que fazer +4 for in, alem do for in dos frames.

"""

def create_window(largura, altura):
    root = tk.Tk()
    root.geometry(f"{largura}x{altura}")
    root.resizable(False, False)
    settings.frames["root"] = root
    return root

def main():
    root = create_window(1250, 650)

    for frame_name, info in settings.frames_info.items():
        father_key = info.pop("father", None)
        father = settings.frames[father_key]
        frame = CreateFrame(father, **info)
        settings.frames[frame_name] = frame.frame

    root.mainloop()

if __name__ == "__main__":
    main()
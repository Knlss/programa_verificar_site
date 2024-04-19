import sys
import tkinter as tk

sys.path.append("temporario")

import gui.config.settings as settings

class CreateFrame:

    def create_place_frame(self, father, width, height, anchor, relx, rely, bg):
        frame = tk.Frame(father, width=width, height=height, bg=bg)
        frame.place(anchor=anchor, relx=relx, rely=rely)
        return frame

    def create_grid_frame(self, father, width, bg, row, column):
        father.grid_rowconfigure(0, weight=1)
        father.grid_columnconfigure((0, 1, 2), weight=1)
        frame = tk.Frame(father, width=width, bg=bg)
        frame.grid(row=row, column=column, sticky="nsew")
        return frame

    def create_pack_frame(self, father, bg, side, fill, expand):
        frame = tk.Frame(father, bg=bg)
        frame.pack(side=side, fill=fill, expand=expand)
        return frame


class CreateElement:

    def create_button(self, father, width, height, anchor, relx, rely, bg, activebg, fg, activefg, font, text, cursor, command, relwidth=None, relheight=None):
        if relheight or relwidth != None:
            if relheight and relwidth != None:
                frame = tk.Button(father, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, font=font, text=text, cursor=cursor, command=command)
                frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
                return frame
            else:
                if relheight != None:
                    frame = tk.Button(father, width=width, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, font=font, text=text, cursor=cursor, command=command)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relheight=relheight)
                    return frame
                elif relwidth != None:
                    frame = tk.Button(father, height=height, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, font=font, text=text, cursor=cursor, command=command)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth)
                    return frame
        else:
            frame = tk.Button(father, width=width, height=height, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, font=font, text=text, cursor=cursor, command=command)
            frame.place(anchor=anchor, relx=relx, rely=rely)
            return frame

    def create_checkbutton(self, father, width, height, anchor, relx, rely, bg, activebg, fg, activefg, selectcolor, font, text, cursor, variable, command, relwidth=None, relheight=None):
        if relheight or relwidth != None:
            if relheight and relwidth != None:
                    frame = tk.Checkbutton(father, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, selectcolor=selectcolor, font=font, text=text, cursor=cursor, variable=variable, command=command)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
                    return frame
            else:
                if relheight != None:
                    frame = tk.Checkbutton(father, width=width, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, selectcolor=selectcolor, font=font, text=text, cursor=cursor, variable=variable, command=command)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relheight=relheight)
                    return frame
                elif relwidth != None:
                    frame = tk.Checkbutton(father, height=height, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, selectcolor=selectcolor, font=font, text=text, cursor=cursor, variable=variable, command=command)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth)
                    return frame
        else:
            frame = tk.Checkbutton(father, width=width, height=height, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, selectcolor=selectcolor, font=font, text=text, cursor=cursor, variable=variable, command=command)
            frame.place(anchor=anchor, relx=relx, rely=rely)
            return frame

    def create_input(self, father, width, anchor, relx, rely, bg, fg, font, cursor, relwidth=None):
        if relwidth != None:
            frame = tk.Entry(father, bg=bg, fg=fg, font=font, cursor=cursor)
            frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth)
            return frame
        else:
            frame = tk.Entry(father, width=width, bg=bg, fg=fg, font=font, cursor=cursor)
            frame.place(anchor=anchor, relx=relx, rely=rely)
            return frame

    def create_label(self, father, width, height, anchor, relx, rely, bg, fg, font, justify, cursor, relwidth=None, relheight=None):
        if relheight or relwidth != None:
            if relheight and relwidth != None:
                frame = tk.Label(father, bg=bg, fg=fg, font=font, justify=justify, cursor=cursor)
                frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
                return frame
            else:
                if relheight != None:
                    frame = tk.Label(father, width=width, bg=bg, fg=fg, font=font, justify=justify, cursor=cursor)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relheight=relheight)
                    return frame
                elif relwidth != None:
                    frame = tk.Label(father, height=height, bg=bg, fg=fg, font=font, justify=justify, cursor=cursor)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth)
                    return frame
        else:
            frame = tk.Label(father, width=width, height=height, bg=bg, fg=fg, font=font, justify=justify, cursor=cursor)
            frame.place(anchor=anchor, relx=relx, rely=rely)
            return frame

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
    return root

def main():
    frame_config = settings.FrameConfig()

    root = create_window(1250, 650)
    frame_config.frames["root"] = root

    for frame_name, info in frame_config.frames_pack_info.items():
        instance = CreateFrame()
        father_key = info.pop("father", None)
        father = frame_config.frames[father_key]
        frame = instance.create_pack_frame(father, **info)
        frame_config.frames[frame_name] = frame

    for frame_name, info in frame_config.frames_grid_info.items():
        instance = CreateFrame()
        father_key = info.pop("father", None)
        father = frame_config.frames[father_key]
        frame = instance.create_grid_frame(father, **info)
        frame_config.frames[frame_name] = frame

    for frame_name, info in frame_config.frames_place_info.items():
        instance = CreateFrame()
        father_key = info.pop("father", None)
        father = frame_config.frames[father_key]
        frame = instance.create_place_frame(father, **info)
        frame_config.frames[frame_name] = frame

    root.mainloop()


'''for element_name, info in settings.elements_place_info.items():
father_key = info.pop("father", None)
father = settings.elements[father_key]
frame = CreateElement(father, **info)
settings.elements[element_name] = frame.frame'''

if __name__ == "__main__":
    main()
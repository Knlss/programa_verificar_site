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

class CreateElement:
    def __init__(self, father, height, width, anchor, relx, rely, bg, element_type):
        pass



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
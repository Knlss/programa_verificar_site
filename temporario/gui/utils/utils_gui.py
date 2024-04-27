import sys
import tkinter as tk

sys.path.append("temporario")

import gui.config.settings as settings
import gui.config.sett2 as sett2

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

    def __init__(self):
        self.el_cmd = sett2.ElementCommand()

    def create_button(self, father, width, height, anchor, relx, rely, bg, activebg, fg, activefg, font, text, cursor, command, state, relwidth=None, relheight=None):

        if relheight or relwidth != None:
            if relheight and relwidth != None:
                frame = tk.Button(father, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, font=font, text=text, cursor=cursor, command=command, state=state)
                frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
                return frame
            else:
                if relheight != None:
                    frame = tk.Button(father, width=width, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, font=font, text=text, cursor=cursor, command=command, state=state)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relheight=relheight)
                    return frame
                elif relwidth != None:
                    frame = tk.Button(father, height=height, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, font=font, text=text, cursor=cursor, command=command, state=state)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth)
                    return frame
        else:
            frame = tk.Button(father, width=width, height=height, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, font=font, text=text, cursor=cursor, command=command, state=state)
            frame.place(anchor=anchor, relx=relx, rely=rely)
            return frame

    def create_checkbutton(self, father, width, height, anchor, relx, rely, bg, activebg, fg, activefg, selectcolor, font, text, cursor, variable, command, state, relwidth=None, relheight=None):
        if relheight or relwidth != None:
            if relheight and relwidth != None:
                    frame = tk.Checkbutton(father, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, selectcolor=selectcolor, font=font, text=text, cursor=cursor, variable=variable, command=command, state=state)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
                    return frame
            else:
                if relheight != None:
                    frame = tk.Checkbutton(father, width=width, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, selectcolor=selectcolor, font=font, text=text, cursor=cursor, variable=variable, command=command, state=state)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relheight=relheight)
                    return frame
                elif relwidth != None:
                    frame = tk.Checkbutton(father, height=height, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, selectcolor=selectcolor, font=font, text=text, cursor=cursor, variable=variable, command=command, state=state)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth)
                    return frame
        else:
            frame = tk.Checkbutton(father, width=width, height=height, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, selectcolor=selectcolor, font=font, text=text, cursor=cursor, variable=variable, command=command, state=state)
            frame.place(anchor=anchor, relx=relx, rely=rely)
            return frame

    def create_input(self, father, width, anchor, relx, rely, bg, fg, font, cursor, textvariable, limit_lenght, state, relwidth=None):
        locals()[textvariable] = tk.StringVar()
        stringvar = locals()[textvariable]
        stringvar.trace_add("write", lambda *args: (self.el_cmd.limit_lenght(stringvar, textvariable, limit_lenght), stringvar))
        if relwidth != None:
            frame = tk.Entry(father, bg=bg, fg=fg, font=font, cursor=cursor, textvariable=stringvar, state=state)
            frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth)
            return frame
        else:
            frame = tk.Entry(father, width=width, bg=bg, fg=fg, font=font, cursor=cursor, textvariable=stringvar, state=state)
            frame.place(anchor=anchor, relx=relx, rely=rely)
            return frame
        

    def create_label(self, father, width, height, anchor, relx, rely, bg, fg, font, justify, text, cursor, relwidth=None, relheight=None):
        if relheight or relwidth != None:
            if relheight and relwidth != None:
                frame = tk.Label(father, bg=bg, fg=fg, font=font, justify=justify, text=text, cursor=cursor)
                frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
                return frame
            else:
                if relheight != None:
                    frame = tk.Label(father, width=width, bg=bg, fg=fg, font=font, justify=justify, text=text, cursor=cursor)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relheight=relheight)
                    return frame
                elif relwidth != None:
                    frame = tk.Label(father, height=height, bg=bg, fg=fg, font=font, justify=justify, text=text, cursor=cursor)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth)
                    return frame
        else:
            frame = tk.Label(father, width=width, height=height, bg=bg, fg=fg, font=font, justify=justify, text=text, cursor=cursor)
            frame.place(anchor=anchor, relx=relx, rely=rely)
            return frame

def create_window(largura, altura):
    root = tk.Tk()
    root.geometry(f"{largura}x{altura}")
    root.resizable(False, False)
    return root

def root_click(event):
    if event.num == 1:  # Verifica se o evento é um clique esquerdo do mouse
            dc = sett2.gen_cfg.styles["border_styles"]["cell_border_left"]
            dd = sett2.gen_cfg.styles["cell_styles"]["alignment_cell"]
            print(dc)

def main():

    root = create_window(1250, 650)
    root.bind("<Button-1>", root_click)
    settings.frame_config.frames["root"] = root

    for item_type, item_info in [
            (settings.frame_config.frames_pack_info, CreateFrame().create_pack_frame),
            (settings.frame_config.frames_grid_info, CreateFrame().create_grid_frame),
            (settings.frame_config.frames_place_info, CreateFrame().create_place_frame),
            (settings.element_config.elements_button_info, CreateElement().create_button),
            (settings.element_config.elements_entry_info, CreateElement().create_input),
            (settings.element_config.elements_checkbutton_info, CreateElement().create_checkbutton),
            (settings.element_config.elements_label_info, CreateElement().create_label)
        ]:
        for item_name, info in item_type.items():
            instance = item_info
            father_key = info.pop("father")
            father = settings.frame_config.frames[father_key]
            frame = instance(father, **info)
            if item_type is settings.frame_config.frames_pack_info or item_type is settings.frame_config.frames_grid_info or item_type is settings.frame_config.frames_place_info:
                settings.frame_config.frames[item_name] = frame
            else:
                settings.element_config.elements[item_name] = frame


    root.mainloop()

if __name__ == "__main__":
    main()
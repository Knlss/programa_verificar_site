import tkinter as tk

def create_window(largura, altura):
    root = tk.Tk()
    root.geometry(f"{largura}x{altura}")
    return root

def create_master_frame(father):
    master_frame = tk.Frame(father, bg="black")
    master_frame.pack(fill="both", expand=True)
    return master_frame

def create_top_half_frame(father):
    top_half_frame = tk.Frame(father, bg="white")
    return top_half_frame

def create_bottom_half_frame(father):
    bottom_half_frame = tk.Frame(father, bg="blue")
    return bottom_half_frame

def set_frame_size_top(father, frame):
    width_father = father.winfo_width()
    height_father = father.winfo_height() / 2
    frame.place(x=0, y=0, width=width_father, height=height_father)

def set_frame_size_bottom(father, frame):
    width_father = father.winfo_width()
    height_father = father.winfo_height() / 2
    frame.place(x=0, y=height_father, width=width_father, height=height_father)

def bind_resize_handler_top(root, master_frame, frame):
    def resize_handler(event):
        set_frame_size_top(master_frame, frame)

    root.bind("<Configure>", resize_handler)

def bind_resize_handler_bottom(root, master_frame, frame):
    def resize_handler(event):
        set_frame_size_bottom(master_frame, frame)

    root.bind("<Configure>", resize_handler)

def main():
    root = create_window(1200, 600)
    master_frame = create_master_frame(root)

    top_half_frame = create_top_half_frame(master_frame)
    bottom_half_frame = create_bottom_half_frame(master_frame)

    set_frame_size_top(master_frame, top_half_frame)
    bind_resize_handler_top(root, master_frame, top_half_frame)

    set_frame_size_bottom(master_frame, bottom_half_frame)
    bind_resize_handler_bottom(root, master_frame, bottom_half_frame)

    root.mainloop()

if __name__ == "__main__":
    main()

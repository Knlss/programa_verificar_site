import tkinter as tk

# ----------------------------------------------------------------------------------

def create_left_top_frame(father):
    right_top_frame = tk.Frame(father, bg="orange", width=400)
    right_top_frame.pack(side=tk.LEFT, fill=tk.BOTH)

def create_center_top_frame(father):
    right_top_frame = tk.Frame(father, bg="green", width=400)
    right_top_frame.pack(side=tk.CENTER, fill=tk.BOTH)

def create_right_top_frame(father):
    right_top_frame = tk.Frame(father, bg="purple", width=400)
    right_top_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

# ----------------------------------------------------------------------------------

def create_left_bottom_frame(father):
    right_top_frame = tk.Frame(father, bg="brown", width=400)
    right_top_frame.pack(side=tk.LEFT, fill=tk.BOTH)

def create_center_bottom_frame(father):
    right_top_frame = tk.Frame(father, bg="magenta", width=400)
    right_top_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)

def create_right_bottom_frame(father):
    right_top_frame = tk.Frame(father, bg="turquoise", width=400)
    right_top_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

# ----------------------------------------------------------------------------------

def create_window(largura, altura):
    root = tk.Tk()
    root.geometry(f"{largura}x{altura}")
    return root

def create_master_frame(father):
    master_frame = tk.Frame(father, bg="black")
    master_frame.pack(fill="both", expand=True)
    return master_frame

def create_top_half_frame(father):
    top_half_frame = tk.Frame(father, bg="yellow")
    top_half_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    return top_half_frame

def create_bottom_half_frame(father):
    bottom_half_frame = tk.Frame(father, bg="blue")
    bottom_half_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    return bottom_half_frame

def main():
    root = create_window(1200, 600)
    master_frame = create_master_frame(root)

    top_half_frame = create_top_half_frame(master_frame)
    bottom_half_frame = create_bottom_half_frame(master_frame)

    top_left_frame = create_left_top_frame(top_half_frame)
    top_center_frame = create_center_top_frame(top_half_frame)
    top_right_frame = create_right_top_frame(top_half_frame)

    bottom_left_frame = create_left_bottom_frame(bottom_half_frame)
    bottom_center_frame = create_center_bottom_frame(bottom_half_frame)
    bottom_right_frame = create_right_bottom_frame(bottom_half_frame)

    root.mainloop()

if __name__ == "__main__":
    main()

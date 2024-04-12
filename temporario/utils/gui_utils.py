import tkinter as tk

# ----------------------------------------------------------------------------------

def create_select_color_frame(father, x, y):
    select_color_frame = tk.Frame(father, height=40, width=40, bg="lightcoral")
    select_color_frame.place(anchor="center", relx=x, rely=y)
    return select_color_frame

def create_default_check_frame(father):
    default_check_frame = tk.Frame(father, height=20, width=164, bg="coral")
    default_check_frame.place(anchor="s", relx=0.8, rely=1)
    return default_check_frame

def create_select_title_color_frame(father, x, y):
    select_title_color_frame = tk.Frame(father, height=10, width=60, bg="lightcoral")
    select_title_color_frame.place(anchor="center", relx=x, rely=y)
    return select_title_color_frame

def create_title_program_frame(father):
    title_program_frame = tk.Frame(father, height=80, bg="pink")
    title_program_frame.place(anchor="n", relx=0.5, rely=0, relwidth=1.5)  # Coloca o title_program_frame no topo central da janela
    return title_program_frame

def create_title_cell_frame(father):
    title_cell_frame = tk.Frame(father, height=50, bg="cyan", width=250)
    title_cell_frame.place(anchor="n", relx=0.5, rely=0.05)  # Coloca o title_program_frame no topo central da janela
    return title_cell_frame

def create_config_cell_frame(father):
    config_cell_frame = tk.Frame(father, bg="cyan", height=180, width=280)
    config_cell_frame.place(anchor="n", relx=0.5, rely=0.3)
    return config_cell_frame

def create_title_border_frame(father):
    title_border_frame = tk.Frame(father, height=50, bg="cyan", width=250)
    title_border_frame.place(anchor="n", relx=0.5, rely=0.05)  # Coloca o title_program_frame no topo central da janela
    return title_border_frame

def create_config_border_frame(father):
    config_border_frame = tk.Frame(father, bg="cyan", height=180, width=280)
    config_border_frame.place(anchor="n", relx=0.5, rely=0.3)
    return config_border_frame

def create_title_color_frame(father):
    title_color_frame = tk.Frame(father, height=50, bg="cyan", width=250)
    title_color_frame.place(anchor="n", relx=0.5, rely=0.05)  # Coloca o title_program_frame no topo central da janela
    return title_color_frame

def create_config_color_frame(father):
    config_color_frame = tk.Frame(father, bg="cyan", height=200, width=280)
    config_color_frame.place(anchor="n", relx=0.5, rely=0.3)
    return config_color_frame

def create_status_frame(father):
    status_frame = tk.Frame(father, height=10, bg="brown")
    status_frame.place(anchor="s", relx=0.5, rely=1, relwidth=1.5)  # Coloca o title_program_frame no topo central da janela
    return status_frame

def create_process_frame(father):
    process_frame = tk.Frame(father, height=40, width=120, bg="cyan")
    process_frame.place(anchor="center", relx=0.5, rely=0.55)
    return process_frame

def create_files_frame(father):
    files_frame = tk.Frame(father, height=180, width=300, bg="cyan")
    files_frame.place(anchor="center", relx=0.29, rely=0.6)
    return files_frame

def create_input_frame(father):
    input_frame = tk.Frame(father, height=120, width=140, bg="cyan")
    input_frame.place(anchor="center", relx=0.78, rely=0.6)
    return input_frame

def create_left_top_frame(father):
    father.grid_rowconfigure(0, weight=1)
    father.grid_columnconfigure((0, 1, 2), weight=1)
    left_top_frame = tk.Frame(father, bg="orange", width=320)
    left_top_frame.grid(row=0, column=0, sticky="nsew")
    return left_top_frame

def create_center_top_frame(father):
    father.grid_rowconfigure(0, weight=1)
    father.grid_columnconfigure((0, 1, 2), weight=1)
    center_top_frame = tk.Frame(father, bg="green", width=620)
    center_top_frame.grid(row=0, column=1, sticky="nsew")
    return center_top_frame

def create_right_top_frame(father):
    father.grid_rowconfigure(0, weight=1)
    father.grid_columnconfigure((0, 1, 2), weight=1)
    right_top_frame = tk.Frame(father, bg="purple", width=320)
    right_top_frame.grid(row=0, column=2, sticky="nsew")
    return right_top_frame


# ----------------------------------------------------------------------------------

def create_left_bottom_frame(father):
    father.grid_rowconfigure(0, weight=1)
    father.grid_columnconfigure((0, 1, 2), weight=1)
    left_top_frame = tk.Frame(father, bg="#FFDAB9", width=400)
    left_top_frame.grid(row=0, column=0, sticky="nsew")
    return left_top_frame

def create_center_bottom_frame(father):
    father.grid_rowconfigure(0, weight=1)
    father.grid_columnconfigure((0, 1, 2), weight=1)
    center_top_frame = tk.Frame(father, bg="#008080", width=400)
    center_top_frame.grid(row=0, column=1, sticky="nsew")
    return center_top_frame

def create_right_bottom_frame(father):
    father.grid_rowconfigure(0, weight=1)
    father.grid_columnconfigure((0, 1, 2), weight=1)
    right_top_frame = tk.Frame(father, bg="navy", width=400)
    right_top_frame.grid(row=0, column=2, sticky="nsew")
    return right_top_frame

# ----------------------------------------------------------------------------------

def create_window(largura, altura):
    root = tk.Tk()
    root.geometry(f"{largura}x{altura}")
    root.resizable(False, False)
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
    root = create_window(1250, 650)
    master_frame = create_master_frame(root)

    top_half_frame = create_top_half_frame(master_frame)
    bottom_half_frame = create_bottom_half_frame(master_frame)

    top_left_frame = create_left_top_frame(top_half_frame)
    top_center_frame = create_center_top_frame(top_half_frame)
    top_right_frame = create_right_top_frame(top_half_frame)
    bottom_left_frame = create_left_bottom_frame(bottom_half_frame)
    bottom_center_frame = create_center_bottom_frame(bottom_half_frame)
    bottom_right_frame = create_right_bottom_frame(bottom_half_frame)

    title_program_frame = create_title_program_frame(top_center_frame)
    status_frame = create_status_frame(top_center_frame)
    process_frame = create_process_frame(top_right_frame)

    files_frame = create_files_frame(top_center_frame)
    input_frame = create_input_frame(top_center_frame)

    title_cell_frame = create_title_cell_frame(bottom_left_frame)
    config_cell_frame = create_config_cell_frame(bottom_left_frame)

    title_border_frame = create_title_border_frame(bottom_center_frame)
    config_border_frame = create_config_border_frame(bottom_center_frame)

    title_color_frame = create_title_color_frame(bottom_right_frame)
    config_color_frame = create_config_color_frame(bottom_right_frame)

    select_color_frame1 = create_select_color_frame(config_color_frame, 0.2, 0.3)
    select_color_frame2 = create_select_color_frame(config_color_frame, 0.5, 0.3)
    select_color_frame3 = create_select_color_frame(config_color_frame, 0.8, 0.3)
    select_color_frame4 = create_select_color_frame(config_color_frame, 0.5, 0.75)

    select_title_color_frame1 = create_select_title_color_frame(config_color_frame, 0.2, 0.13)
    select_title_color_frame2 = create_select_title_color_frame(config_color_frame, 0.5, 0.13)
    select_title_color_frame3 = create_select_title_color_frame(config_color_frame, 0.8, 0.13)
    select_title_color_frame4 = create_select_title_color_frame(config_color_frame, 0.5, 0.58)

    default_check_frame = create_default_check_frame(bottom_right_frame)


    root.mainloop()

if __name__ == "__main__":
    main()

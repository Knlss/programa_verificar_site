import tkinter as tk

# ---------------------------------------------------

def create_input_title_cell_frame(father):
    input_title_cell_frame = tk.Frame(father, width=200, height=20, bg="lightcoral")
    input_title_cell_frame.place(anchor="center", relx=0.5, rely=0.1)
    return input_title_cell_frame

def create_fontsize_cell_frame(father):
    input_fontsize_cell_frame = tk.Frame(father, width=100, height=20, bg="lightcoral")
    input_fontsize_cell_frame.place(anchor="center", relx=0.5, rely=0.38)
    return input_fontsize_cell_frame

def create_alignment_left_cell_frame(father):
    input_alignment_left_cell_frame = tk.Frame(father, width=60, height=60, bg="lightcoral")
    input_alignment_left_cell_frame.place(anchor="center", relx=0.2, rely=0.78)
    return input_alignment_left_cell_frame

def create_alignment_center_cell_frame(father):
    input_alignment_center_cell_frame = tk.Frame(father, width=60, height=60, bg="lightcoral")
    input_alignment_center_cell_frame.place(anchor="center", relx=0.5, rely=0.78)
    return input_alignment_center_cell_frame

def create_alignment_right_cell_frame(father):
    input_alignment_right_cell_frame = tk.Frame(father, width=60, height=60, bg="lightcoral")
    input_alignment_right_cell_frame.place(anchor="center", relx=0.8, rely=0.78)
    return input_alignment_right_cell_frame

def create_title_frame(father):
    input_frame = tk.Frame(father, width=150, height=10, bg="lightcoral")
    input_frame.place(anchor="center", relx=0.5, rely=0.55)
    return input_frame

def create_titlefont_frame(father):
    inputfont_frame = tk.Frame(father, width=80, height=10, bg="lightcoral")
    inputfont_frame.place(anchor="center", relx=0.5, rely=0.28)
    return inputfont_frame

# ---------------------------------------------------

def create_select_color_frame(father, x, y):
    select_color_frame = tk.Frame(father, height=40, width=40, bg="lightcoral")
    select_color_frame.place(anchor="center", relx=x, rely=y)
    return select_color_frame

def create_select_title_color_frame(father, x, y):
    select_title_color_frame = tk.Frame(father, height=10, width=60, bg="lightcoral")
    select_title_color_frame.place(anchor="center", relx=x, rely=y)
    return select_title_color_frame

def create_select_border_frame(father, x, y):
    select_border_frame = tk.Frame(father, height=70, width=70, bg="lightcoral")
    select_border_frame.place(anchor="center", relx=x, rely=y)
    return select_border_frame

def create_select_title_border_frame(father, x, y):
    select_title_border_frame = tk.Frame(father, height=10, width=60, bg="lightcoral")
    select_title_border_frame.place(anchor="center", relx=x, rely=y)
    return select_title_border_frame

def create_default_check_frame(father):
    default_check_frame = tk.Frame(father, height=20, width=168, bg="lightcoral")
    default_check_frame.place(anchor="s", relx=0.8, rely=1)
    return default_check_frame

def create_top_bottom_frame(father, column, bg, width):
    father.grid_rowconfigure(0, weight=1)
    father.grid_columnconfigure((0, 1, 2), weight=1)
    top_bottom_frame = tk.Frame(father, bg=bg, width=width)
    top_bottom_frame.grid(row=0, column=column, sticky="nsew")
    return top_bottom_frame

def create_secondary_frame(father, height, width, anchor, relx, rely, bg, relwidth=None):
    if relwidth == None:
        secondary_frame = tk.Frame(father, width=width, height=height, bg=bg)
        secondary_frame.place(anchor=anchor, relx=relx, rely=rely)
        return secondary_frame
    elif relwidth != None:
        secondary_frame = tk.Frame(father, height=height, bg=bg)
        secondary_frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth)
        return secondary_frame
    

def create_window(largura, altura):
    root = tk.Tk()
    root.geometry(f"{largura}x{altura}")
    root.resizable(False, False)
    return root

def create_master_frame(father):
    master_frame = tk.Frame(father, bg="black")
    master_frame.pack(fill="both", expand=True)
    return master_frame

def create_half_frame(father, side, bg):
    half_frame = tk.Frame(father, bg=bg)
    half_frame.pack(side=side, fill=tk.BOTH, expand=True)
    return half_frame

def main():
    root = create_window(1250, 650)
    master_frame = create_master_frame(root)

    top_half_frame = create_half_frame(master_frame, tk.TOP, "yellow")
    bottom_half_frame = create_half_frame(master_frame, tk.BOTTOM, "blue")

    top_left_frame = create_top_bottom_frame(top_half_frame, 0, "orange", 320)
    top_center_frame = create_top_bottom_frame(top_half_frame, 1, "green", 620)
    top_right_frame = create_top_bottom_frame(top_half_frame, 2, "purple", 320)
    bottom_left_frame = create_top_bottom_frame(bottom_half_frame, 0, "#FFDAB9", 400)
    bottom_center_frame = create_top_bottom_frame(bottom_half_frame, 1, "#008080", 400)
    bottom_right_frame = create_top_bottom_frame(bottom_half_frame, 2, "navy", 400)

    title_program_frame = create_secondary_frame(top_center_frame, 80, 0, "n", 0.5, 0, "cyan", 1.5 )
    status_frame = create_secondary_frame(top_center_frame, 10, 0, "s", 0.5, 1, "cyan", 1.5)

    process_frame = create_secondary_frame(top_right_frame, 40, 120, "center", 0.5, 0.55, "cyan")

    files_frame = create_secondary_frame(top_center_frame, 180, 300, "center", 0.29, 0.6, "cyan")
    input_frame = create_secondary_frame(top_center_frame, 120, 140, "center", 0.78, 0.6, "cyan")

    title_cell_frame = create_secondary_frame(bottom_left_frame, 50, 250, "n", 0.5, 0.05, "cyan")
    config_cell_frame = create_secondary_frame(bottom_left_frame, 200, 280, "n", 0.5, 0.3, "cyan")

    title_border_frame = create_secondary_frame(bottom_center_frame, 50, 250, "n", 0.5, 0.05, "cyan")
    config_border_frame = create_secondary_frame(bottom_center_frame, 200, 280, "n", 0.5, 0.3, "cyan")


    title_color_frame = create_secondary_frame(bottom_right_frame, 50, 250, "n", 0.5, 0.05, "cyan")
    config_color_frame = create_secondary_frame(bottom_right_frame, 200, 280, "n", 0.5, 0.3, "cyan")

    select_color_frame1 = create_select_color_frame(config_color_frame, 0.2, 0.3)
    select_color_frame2 = create_select_color_frame(config_color_frame, 0.5, 0.3)
    select_color_frame3 = create_select_color_frame(config_color_frame, 0.8, 0.3)
    select_color_frame4 = create_select_color_frame(config_color_frame, 0.5, 0.75)

    select_title_color_frame1 = create_select_title_color_frame(config_color_frame, 0.2, 0.13)
    select_title_color_frame2 = create_select_title_color_frame(config_color_frame, 0.5, 0.13)
    select_title_color_frame3 = create_select_title_color_frame(config_color_frame, 0.8, 0.13)
    select_title_color_frame4 = create_select_title_color_frame(config_color_frame, 0.5, 0.58)

    select_border_frame1 = create_select_border_frame(config_border_frame, 0.25, 0.28)
    select_border_frame2 = create_select_border_frame(config_border_frame, 0.25, 0.78)
    select_border_frame3 = create_select_border_frame(config_border_frame, 0.75, 0.28)
    select_border_frame4 = create_select_border_frame(config_border_frame, 0.75, 0.78)

    select_title_color_frame1 = create_select_title_border_frame(config_border_frame, 0.25, 0.06)
    select_title_color_frame2 = create_select_title_border_frame(config_border_frame, 0.25, 0.56)
    select_title_color_frame3 = create_select_title_border_frame(config_border_frame, 0.75, 0.06)
    select_title_color_frame4 = create_select_title_border_frame(config_border_frame, 0.75, 0.56)

# ----------------------------------------------------------------------------

    input_title_cell_frame = create_input_title_cell_frame(config_cell_frame)
    input_fontsize_cell_frame = create_fontsize_cell_frame(config_cell_frame)
    input_alignment_left_cell_frame = create_alignment_left_cell_frame(config_cell_frame)
    input_alignment_center_cell_frame = create_alignment_center_cell_frame(config_cell_frame)
    input_alignment_right_cell_frame = create_alignment_right_cell_frame(config_cell_frame)
    input_title_frame = create_title_frame(config_cell_frame)
    input_titlefont_frame = create_titlefont_frame(config_cell_frame)

    default_check_frame = create_default_check_frame(bottom_right_frame)

# ----------------------------------------------------------------------------


    root.mainloop()

if __name__ == "__main__":
    main()

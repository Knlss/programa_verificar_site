import tkinter as tk
from . import sett2

class FrameConfig:
    def __init__(self):
        self.frames = {}
        self.frames_pack_info = {
            "master": {"father":"root", "bg":"black", "side":tk.LEFT, "fill":tk.BOTH, "expand":True},

            "upper": {"father":"master", "bg":"yellow", "side":tk.TOP, "fill":tk.BOTH, "expand":True},
            "lower": {"father":"master", "bg":"blue", "side":tk.BOTTOM, "fill":tk.BOTH, "expand":True},
        }

        self.frames_grid_info = {
            "up_left":  {"father":"upper", "width":320, "bg":"#FFFDFB", "row":0, "column":0},
            "up_center":  {"father":"upper", "width":620, "bg":"#FFFDFB", "row":0, "column":1},
            "up_right":  {"father":"upper", "width":320, "bg":"#FFFDFB", "row":0, "column":2},

            "low_left":  {"father":"lower", "width":400, "bg":"#FFFDFB", "row":0, "column":0},
            "low_center":  {"father":"lower", "width":400, "bg":"#FFFDFB", "row":0, "column":1},
            "low_right":  {"father":"lower", "width":400, "bg":"#FFFDFB", "row":0, "column":2}
        }

        self.frames_place_info = {
            "border_pack_lower": {"father":"lower", "width":1250, "height":2, "anchor":"center", "relx":0.5, "rely":0.05, "bg":"black"}, 

            "border_grid_low_left": {"father":"low_left", "width":2, "height":310, "anchor":"center", "relx":1, "rely":0.53, "bg":"black"}, 
            "border_grid_low_center1": {"father":"low_center", "width":2, "height":310, "anchor":"center", "relx":1, "rely":0.53, "bg":"black"}, 
            "border_grid_low_center2": {"father":"low_center", "width":2, "height":310, "anchor":"center", "relx":0, "rely":0.53, "bg":"black"}, 
            "border_grid_low_right": {"father":"low_right", "width":2, "height":310, "anchor":"center", "relx":0, "rely":0.53, "bg":"black"}, 

            "program_title":  {"father":"up_center", "width":620, "height":80, "anchor":"n", "relx":0.5, "rely":0, "bg":"#FFFDFB"}, 
            "program_status":  {"father":"up_center", "width":620, "height":20, "anchor":"s", "relx":0.5, "rely":1, "bg":"#FFFDFB"},
            "program_process":  {"father":"up_right", "width":120, "height":40, "anchor":"center", "relx":0.5, "rely":0.55, "bg":"#FFFDFB"},

            "folder_select":  {"father":"up_center", "width":300, "height":180, "anchor":"center", "relx":0.29, "rely":0.6, "bg":"#FFFDFB"},
            "column_select":  {"father":"up_center", "width":140, "height":120, "anchor":"center", "relx":0.78, "rely":0.6, "bg":"#FFFDFB"},

            "cell_section_title":  {"father":"low_left", "width":250, "height":50, "anchor":"n", "relx":0.5, "rely":0.05, "bg":"#FFFDFB"},
            "border_section_title":  {"father":"low_center", "width":250, "height":50, "anchor":"n", "relx":0.5, "rely":0.05, "bg":"#FFFDFB"},
            "color_section_title":  {"father":"low_right", "width":250, "height":50, "anchor":"n", "relx":0.5, "rely":0.05, "bg":"#FFFDFB"},

            "cell_section_config":  {"father":"low_left", "width":280, "height":200, "anchor":"n", "relx":0.5, "rely":0.3, "bg":"#FFFDFB"},
            "border_section_config":  {"father":"low_center", "width":280, "height":200, "anchor":"n", "relx":0.5, "rely":0.3, "bg":"#FFFDFB"},
            "color_section_config":  {"father":"low_right", "width":280, "height":200, "anchor":"n", "relx":0.5, "rely":0.3, "bg":"#FFFDFB"},

            "color_ac_select":  {"father":"color_section_config", "width":40, "height":40, "anchor":"center", "relx":0.2, "rely":0.3, "bg":"#FFFDFB"},
            "color_in_select":  {"father":"color_section_config", "width":40, "height":40, "anchor":"center", "relx":0.5, "rely":0.3, "bg":"#FFFDFB"},
            "color_ti_select":  {"father":"color_section_config", "width":40, "height":40, "anchor":"center", "relx":0.8, "rely":0.3, "bg":"#FFFDFB"},
            "color_bo_select":  {"father":"color_section_config", "width":40, "height":40, "anchor":"center", "relx":0.5, "rely":0.75, "bg":"#FFFDFB"},

            "color_ac_select_title":  {"father":"color_section_config", "width":70, "height":14, "anchor":"center", "relx":0.2, "rely":0.13, "bg":"#FFFDFB"},
            "color_in_select_title":  {"father":"color_section_config", "width":70, "height":14, "anchor":"center", "relx":0.5, "rely":0.13, "bg":"#FFFDFB"},
            "color_ti_select_title":  {"father":"color_section_config", "width":70, "height":14, "anchor":"center", "relx":0.8, "rely":0.13, "bg":"#FFFDFB"},
            "color_bo_select_title":  {"father":"color_section_config", "width":70, "height":14, "anchor":"center", "relx":0.5, "rely":0.58, "bg":"#FFFDFB"},

            "border_le_select":  {"father":"border_section_config", "width":70, "height":70, "anchor":"center", "relx":0.25, "rely":0.78, "bg":"#FFFDFB"},
            "border_ri_select":  {"father":"border_section_config", "width":70, "height":70, "anchor":"center", "relx":0.75, "rely":0.78, "bg":"#FFFDFB"},
            "border_up_select":  {"father":"border_section_config", "width":70, "height":70, "anchor":"center", "relx":0.25, "rely":0.28, "bg":"#FFFDFB"},
            "border_low_select":  {"father":"border_section_config", "width":70, "height":70, "anchor":"center", "relx":0.75, "rely":0.28, "bg":"#FFFDFB"},

            "border_le_select_title":  {"father":"border_section_config", "width":60, "height":14, "anchor":"center", "relx":0.25, "rely":0.56, "bg":"#FFFDFB"},
            "border_ri_select_title":  {"father":"border_section_config", "width":60, "height":14, "anchor":"center", "relx":0.75, "rely":0.56, "bg":"#FFFDFB"},
            "border_up_select_title":  {"father":"border_section_config", "width":60, "height":14, "anchor":"center", "relx":0.25, "rely":0.06, "bg":"#FFFDFB"},
            "border_low_select_title":  {"father":"border_section_config", "width":60, "height":14, "anchor":"center", "relx":0.75, "rely":0.06, "bg":"#FFFDFB"},

            "column_title_def":  {"father":"cell_section_config", "width":200, "height":20, "anchor":"center", "relx":0.5, "rely":0.1, "bg":"#FFFDFB"},
            "fontsize_def":  {"father":"cell_section_config", "width":100, "height":20, "anchor":"center", "relx":0.5, "rely":0.38, "bg":"#FFFDFB"},
            "alignment_le_def":  {"father":"cell_section_config", "width":60, "height":60, "anchor":"center", "relx":0.2, "rely":0.78, "bg":"#FFFDFB"},
            "alignment_ce_def":  {"father":"cell_section_config", "width":60, "height":60, "anchor":"center", "relx":0.5, "rely":0.78, "bg":"#FFFDFB"},
            "alignment_ri_def":  {"father":"cell_section_config", "width":60, "height":60, "anchor":"center", "relx":0.8, "rely":0.78, "bg":"#FFFDFB"},

            "alignment_def_title":  {"father":"cell_section_config", "width":150, "height":14, "anchor":"center", "relx":0.5, "rely":0.55, "bg":"#FFFDFB"},
            "fontsize_def_title":  {"father":"cell_section_config", "width":150, "height":14, "anchor":"center", "relx":0.5, "rely":0.28, "bg":"#FFFDFB"},

            "default_mode_select":  {"father":"up_right", "width":168, "height":20, "anchor":"s", "relx":0.7, "rely":1, "bg":"#FFFDFB"},

            "input_column_def":  {"father":"column_select", "width":80, "height":20, "anchor":"center", "relx":0.5, "rely":0.35, "bg":"#FFFDFB"},
            "output_column_def":  {"father":"column_select", "width":80, "height":20, "anchor":"center", "relx":0.5, "rely":0.75, "bg":"#FFFDFB"},

            "input_column_def_title":  {"father":"column_select", "width":110, "height":14, "anchor":"center", "relx":0.5, "rely":0.2, "bg":"#FFFDFB"},
            "output_column_def_title":  {"father":"column_select", "width":110, "height":14, "anchor":"center", "relx":0.5, "rely":0.6, "bg":"#FFFDFB"},

            "archive_select":  {"father":"folder_select", "width":250, "height":20, "anchor":"center", "relx":0.5, "rely":0.30, "bg":"#FFFDFB"},
            "path_select":  {"father":"folder_select", "width":250, "height":20, "anchor":"center", "relx":0.5, "rely":0.7, "bg":"#FFFDFB"},

            "archive_select_title": {"father":"folder_select", "width":180, "height":20, "anchor":"center", "relx":0.5, "rely":0.15, "bg":"#FFFDFB"},
            "path_select_title": {"father":"folder_select", "width":180, "height":20, "anchor":"center", "relx":0.5, "rely":0.55, "bg":"#FFFDFB"}
        }

class ElementConfig:
    def __init__(self):

        self.elements = {}

        self.elements_button_info = {
            "process_button": {"father":"program_process", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 12 bold", "text":"PROCESSAR", "cursor":"hand2", "command":lambda: print(0), "relwidth":1, "relheight":1, "state":tk.NORMAL},

            "archive_button": {"father":"archive_select", "width":0, "height":0, "anchor":"center", "relx":0.949, "rely":0.5, "bg":"lightgray", "activebg":"gray", "fg":"black", "activefg":"#1A1110", "font":"helvetica", "text":"▼", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.1, "relheight":1, "state":tk.NORMAL},
            
            "folder_button": {"father":"path_select", "width":0, "height":0, "anchor":"center", "relx":0.949, "rely":0.5, "bg":"lightgray", "activebg":"gray", "fg":"black", "activefg":"#1A1110", "font":"helvetica", "text":"▼", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.1, "relheight":1, "state":tk.NORMAL},
            
            "size_button": {"father":"fontsize_def", "width":0, "height":0, "anchor":"center", "relx":0.874, "rely":0.5, "bg":"lightgray", "activebg":"gray", "fg":"black", "activefg":"#1A1110", "font":"helvetica", "text":"▼", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.25, "relheight":1, "state":tk.NORMAL},
            
            "align_left_button": {"father":"alignment_le_def", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 15 bold", "text":"←", "cursor":"hand2", "command":lambda: sett2.el_cmd.select_alignment("left", self.elements["align_left_button"], self.elements["align_center_button"], self.elements["align_right_button"]), "relwidth":0.9, "relheight":0.9, "state":tk.NORMAL},
            
            "align_center_button": {"father":"alignment_ce_def", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 15 bold", "text":"•", "cursor":"hand2", "command":lambda: sett2.el_cmd.select_alignment("center", self.elements["align_left_button"], self.elements["align_center_button"], self.elements["align_right_button"]), "relwidth":0.9, "relheight":0.9, "state":tk.NORMAL},
            
            "align_right_button": {"father":"alignment_ri_def", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 15 bold", "text":"→", "cursor":"hand2", "command":lambda: sett2.el_cmd.select_alignment("right", self.elements["align_left_button"], self.elements["align_center_button"], self.elements["align_right_button"]), "relwidth":0.9, "relheight":0.9, "state":tk.NORMAL},
            
            "border_top_button": {"father":"border_up_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 12", "text":"─", "cursor":"hand2", "command":lambda: self.elements["border_top_button"].config(bg="gray") if sett2.el_cmd.select_border("top", "cell") else self.elements["border_top_button"].config(bg="#F9F0F0"), "relwidth":0.8, "relheight":0.8, "state":tk.NORMAL},
            
            "border_bottom_button": {"father":"border_low_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 12", "text":"─", "cursor":"hand2", "command":lambda: self.elements["border_bottom_button"].config(bg="gray") if sett2.el_cmd.select_border("bottom", "cell") else self.elements["border_bottom_button"].config(bg="#F9F0F0"), "relwidth":0.8, "relheight":0.8, "state":tk.NORMAL},
            
            "border_left_button": {"father":"border_le_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 12", "text":"│", "cursor":"hand2", "command":lambda: self.elements["border_left_button"].config(bg="gray") if sett2.el_cmd.select_border("left", "cell") else self.elements["border_left_button"].config(bg="#F9F0F0"), "relwidth":0.8, "relheight":0.8, "state":tk.NORMAL},
            
            "border_right_button": {"father":"border_ri_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 12", "text":"│", "cursor":"hand2", "command":lambda: self.elements["border_right_button"].config(bg="gray") if sett2.el_cmd.select_border("right", "cell") else self.elements["border_right_button"].config(bg="#F9F0F0"), "relwidth":0.8, "relheight":0.8, "state":tk.NORMAL},
            
            "color_ac_button": {"father":"color_ac_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 10", "text":"☰", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.9, "relheight":0.9, "state":tk.NORMAL},
            
            "color_ti_button": {"father":"color_ti_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 10", "text":"☰", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.9, "relheight":0.9, "state":tk.NORMAL},

            "color_in_button": {"father":"color_in_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 10", "text":"☰", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.9, "relheight":0.9, "state":tk.NORMAL},
            
            "color_bo_button": {"father":"color_bo_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 10", "text":"☰", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.9, "relheight":0.9, "state":tk.NORMAL}
        }

        self.elements_checkbutton_info = {
            "default_mode_checkbutton": {"father":"default_mode_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "selectcolor":"", "font":"helvetica 10 bold", "text":"Redefinir para Padrão", "cursor":"hand2", "variable":"entry_default", "command":lambda: print(0), "relwidth":1, "relheight":1, "state":tk.NORMAL}
        }
        
        self.elements_entry_info = {
            "archive_show_entry": {"father":"archive_select", "width":0, "anchor":"center", "relx":0.448, "rely":0.5, "bg":"white", "fg":"black", "font":"helvetica 10", "cursor":"arrow", "relwidth":0.9, "textvariable":"entry_archive", "limit_lenght":None, "state":tk.DISABLED},
            
            "folder_show_entry": {"father":"path_select", "width":0, "anchor":"center", "relx":0.448, "rely":0.5, "bg":"white", "fg":"black", "font":"helvetica 10", "cursor":"arrow", "relwidth":0.9, "textvariable":"entry_folder", "limit_lenght":None, "state":tk.DISABLED},
            
            "input_column_entry": {"father":"input_column_def", "width":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"white", "fg":"black", "font":"helvetica 10", "cursor":"hand2", "relwidth":1, "textvariable":"entry_input", "limit_lenght":1, "state":tk.NORMAL},
            
            "output_column_entry": {"father":"output_column_def", "width":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"white", "fg":"black", "font":"helvetica 10", "cursor":"hand2", "relwidth":1, "textvariable":"entry_output", "limit_lenght":1, "state":tk.NORMAL},
            
            "input_name_entry": {"father":"column_title_def", "width":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"white", "fg":"black", "font":"helvetica 10", "cursor":"hand2", "relwidth":1, "textvariable":"entry_name", "limit_lenght":10, "state":tk.NORMAL},
            
            "size_show_entry": {"father":"fontsize_def", "width":0, "anchor":"center", "relx":0.373, "rely":0.5, "bg":"white", "fg":"black", "font":"helvetica 10", "cursor":"arrow", "relwidth":0.75, "textvariable":"entry_size", "limit_lenght":None, "state":tk.DISABLED},
        }

        self.elements_label_info = {
            "program_label": {"father":"program_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 40 bold", "justify":"center", "text":"Website Checker", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "status_label": {"father":"program_status", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"teste", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "archive_label": {"father":"archive_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Arquivo Selecionado:", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "folder_label": {"father":"path_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Caminho para Download:", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "input_label": {"father":"input_column_def_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 8 bold", "justify":"center", "text":"Coluna de Entrada:", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "output_label": {"father":"output_column_def_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 8 bold", "justify":"center", "text":"Coluna de Saída:", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "cell_label": {"father":"cell_section_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 20 bold", "justify":"center", "text":"Células", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "size_label": {"father":"fontsize_def_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Tamanho da Fonte:", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "align_label": {"father":"alignment_def_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Alinhamento:", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "border_label": {"father":"border_section_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 20 bold", "justify":"center", "text":"Bordas", "cursor":"arrow", "relwidth":1, "relheight":1},

            "border_up_label": {"father":"border_up_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Superior", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "border_low_label": {"father":"border_low_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Inferior", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "border_le_label": {"father":"border_le_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Esquerda", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "border_ri_label": {"father":"border_ri_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Direita", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "color_label": {"father":"color_section_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 20 bold", "justify":"center", "text":"Cores", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "color_ac_label": {"father":"color_ac_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Acessível", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "color_ti_label": {"father":"color_ti_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Excedido", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "color_in_label": {"father":"color_in_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Inacessível", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "color_bo_label": {"father":"color_bo_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Bordas", "cursor":"arrow", "relwidth":1, "relheight":1},
        }

frame_config = FrameConfig()
element_config = ElementConfig()
import tkinter as tk

class FrameConfig:
    def __init__(self):
        self.frames = {}
        self.frames_pack_info = {
            "master": {"father":"root", "bg":"black", "side":tk.LEFT, "fill":tk.BOTH, "expand":True},

            "upper": {"father":"master", "bg":"yellow", "side":tk.TOP, "fill":tk.BOTH, "expand":True},
            "lower": {"father":"master", "bg":"blue", "side":tk.BOTTOM, "fill":tk.BOTH, "expand":True},
        }
        self.frames_grid_info = {
            "up_left":  {"father":"upper", "width":320, "bg":"orange", "row":0, "column":0},
            "up_center":  {"father":"upper", "width":620, "bg":"green", "row":0, "column":1},
            "up_right":  {"father":"upper", "width":320, "bg":"purple", "row":0, "column":2},

            "low_left":  {"father":"lower", "width":400, "bg":"#FFDAB9", "row":0, "column":0},
            "low_center":  {"father":"lower", "width":400, "bg":"#008080", "row":0, "column":1},
            "low_right":  {"father":"lower", "width":400, "bg":"navy", "row":0, "column":2}
        }
        self.frames_place_info = {
            "program_title":  {"father":"up_center", "width":620, "height":80, "anchor":"n", "relx":0.5, "rely":0, "bg":"cyan"}, 
            "program_status":  {"father":"up_center", "width":620, "height":10, "anchor":"s", "relx":0.5, "rely":1, "bg":"cyan"},
            "program_process":  {"father":"up_right", "width":120, "height":40, "anchor":"center", "relx":0.5, "rely":0.55, "bg":"cyan"},

            "folder_select":  {"father":"up_center", "width":300, "height":180, "anchor":"center", "relx":0.29, "rely":0.6, "bg":"cyan"},
            "column_select":  {"father":"up_center", "width":140, "height":120, "anchor":"center", "relx":0.78, "rely":0.6, "bg":"cyan"},

            "cell_section_title":  {"father":"low_left", "width":250, "height":50, "anchor":"n", "relx":0.5, "rely":0.05, "bg":"cyan"},
            "border_section_title":  {"father":"low_center", "width":250, "height":50, "anchor":"n", "relx":0.5, "rely":0.05, "bg":"cyan"},
            "color_section_title":  {"father":"low_right", "width":250, "height":50, "anchor":"n", "relx":0.5, "rely":0.05, "bg":"cyan"},

            "cell_section_config":  {"father":"low_left", "width":280, "height":200, "anchor":"n", "relx":0.5, "rely":0.3, "bg":"cyan"},
            "border_section_config":  {"father":"low_center", "width":280, "height":200, "anchor":"n", "relx":0.5, "rely":0.3, "bg":"cyan"},
            "color_section_config":  {"father":"low_right", "width":280, "height":200, "anchor":"n", "relx":0.5, "rely":0.3, "bg":"cyan"},

            "color_ac_select":  {"father":"color_section_config", "width":40, "height":40, "anchor":"center", "relx":0.2, "rely":0.3, "bg":"lightcoral"},
            "color_in_select":  {"father":"color_section_config", "width":40, "height":40, "anchor":"center", "relx":0.5, "rely":0.3, "bg":"lightcoral"},
            "color_ti_select":  {"father":"color_section_config", "width":40, "height":40, "anchor":"center", "relx":0.8, "rely":0.3, "bg":"lightcoral"},
            "color_bo_select":  {"father":"color_section_config", "width":40, "height":40, "anchor":"center", "relx":0.5, "rely":0.75, "bg":"lightcoral"},

            "color_ac_select_title":  {"father":"color_section_config", "width":60, "height":10, "anchor":"center", "relx":0.2, "rely":0.13, "bg":"lightcoral"},
            "color_in_select_title":  {"father":"color_section_config", "width":60, "height":10, "anchor":"center", "relx":0.5, "rely":0.13, "bg":"lightcoral"},
            "color_ti_select_title":  {"father":"color_section_config", "width":60, "height":10, "anchor":"center", "relx":0.8, "rely":0.13, "bg":"lightcoral"},
            "color_bo_select_title":  {"father":"color_section_config", "width":60, "height":10, "anchor":"center", "relx":0.5, "rely":0.58, "bg":"lightcoral"},

            "border_le_select":  {"father":"border_section_config", "width":70, "height":70, "anchor":"center", "relx":0.25, "rely":0.28, "bg":"lightcoral"},
            "border_ri_select":  {"father":"border_section_config", "width":70, "height":70, "anchor":"center", "relx":0.25, "rely":0.78, "bg":"lightcoral"},
            "border_up_select":  {"father":"border_section_config", "width":70, "height":70, "anchor":"center", "relx":0.75, "rely":0.28, "bg":"lightcoral"},
            "border_low_select":  {"father":"border_section_config", "width":70, "height":70, "anchor":"center", "relx":0.75, "rely":0.78, "bg":"lightcoral"},

            "border_le_select_title":  {"father":"border_section_config", "width":60, "height":10, "anchor":"center", "relx":0.25, "rely":0.06, "bg":"lightcoral"},
            "border_ri_select_title":  {"father":"border_section_config", "width":60, "height":10, "anchor":"center", "relx":0.25, "rely":0.56, "bg":"lightcoral"},
            "border_up_select_title":  {"father":"border_section_config", "width":60, "height":10, "anchor":"center", "relx":0.75, "rely":0.06, "bg":"lightcoral"},
            "border_low_select_title":  {"father":"border_section_config", "width":60, "height":10, "anchor":"center", "relx":0.75, "rely":0.56, "bg":"lightcoral"},

            "column_title_def":  {"father":"cell_section_config", "width":200, "height":20, "anchor":"center", "relx":0.5, "rely":0.1, "bg":"lightcoral"},
            "fontsize_def":  {"father":"cell_section_config", "width":100, "height":20, "anchor":"center", "relx":0.5, "rely":0.38, "bg":"lightcoral"},
            "alignment_le_def":  {"father":"cell_section_config", "width":60, "height":60, "anchor":"center", "relx":0.2, "rely":0.78, "bg":"lightcoral"},
            "alignment_ce_def":  {"father":"cell_section_config", "width":60, "height":60, "anchor":"center", "relx":0.5, "rely":0.78, "bg":"lightcoral"},
            "alignment_ri_def":  {"father":"cell_section_config", "width":60, "height":60, "anchor":"center", "relx":0.8, "rely":0.78, "bg":"lightcoral"},

            "alignment_def_title":  {"father":"cell_section_config", "width":150, "height":10, "anchor":"center", "relx":0.5, "rely":0.55, "bg":"lightcoral"},
            "fontsize_def_title":  {"father":"cell_section_config", "width":80, "height":10, "anchor":"center", "relx":0.5, "rely":0.28, "bg":"lightcoral"},

            "default_mode_select":  {"father":"up_right", "width":168, "height":20, "anchor":"s", "relx":0.8, "rely":1, "bg":"lightcoral"},

            "input_column_def":  {"father":"column_select", "width":80, "height":20, "anchor":"center", "relx":0.5, "rely":0.35, "bg":"lightcoral"},
            "output_column_def":  {"father":"column_select", "width":80, "height":20, "anchor":"center", "relx":0.5, "rely":0.75, "bg":"lightcoral"},

            "input_column_def_title":  {"father":"column_select", "width":60, "height":10, "anchor":"center", "relx":0.5, "rely":0.2, "bg":"lightcoral"},
            "output_column_def_title":  {"father":"column_select", "width":60, "height":10, "anchor":"center", "relx":0.5, "rely":0.6, "bg":"lightcoral"},

            "archive_select":  {"father":"folder_select", "width":250, "height":20, "anchor":"center", "relx":0.5, "rely":0.30, "bg":"lightcoral"},
            "path_select":  {"father":"folder_select", "width":250, "height":20, "anchor":"center", "relx":0.5, "rely":0.7, "bg":"lightcoral"},

            "archive_select_title": {"father":"folder_select", "width":60, "height":10, "anchor":"center", "relx":0.5, "rely":0.15, "bg":"lightcoral"},
            "path_select_title": {"father":"folder_select", "width":60, "height":10, "anchor":"center", "relx":0.5, "rely":0.55, "bg":"lightcoral"}
        }
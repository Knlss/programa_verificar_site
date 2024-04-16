import tkinter as tk


frames = {}

frames_info = {

    "master": {"father":"root", "height":tk.LEFT, "width":tk.BOTH, "anchor": True, "relx":None, "rely":None, "bg":"black", "frame_type":"pack"},

    "upper": {"father":"master", "height":tk.TOP, "width":tk.BOTH, "anchor": True, "relx":None, "rely":None, "bg":"yellow", "frame_type":"pack"},
    "lower": {"father":"master", "height":tk.BOTTOM, "width":tk.BOTH, "anchor": True, "relx":None, "rely":None, "bg":"blue", "frame_type":"pack"},

    "up_left":  {"father":"upper", "height":0, "width":320, "anchor":0, "relx":None, "rely":None, "bg":"orange", "frame_type":"grid"},
    "up_center":  {"father":"upper", "height":0, "width":620, "anchor":1, "relx":None, "rely":None, "bg":"green", "frame_type":"grid"},
    "up_right":  {"father":"upper", "height":0, "width":320, "anchor":2, "relx":None, "rely":None, "bg":"purple", "frame_type":"grid"},

    "low_left":  {"father":"lower", "height":0, "width":400, "anchor":0, "relx":None, "rely":None, "bg":"#FFDAB9", "frame_type":"grid"},
    "low_center":  {"father":"lower", "height":0, "width":400, "anchor":1, "relx":None, "rely":None, "bg":"#008080", "frame_type":"grid"},
    "low_right":  {"father":"lower", "height":0, "width":400, "anchor":2, "relx":None, "rely":None, "bg":"navy", "frame_type":"grid"},

    "program_title":  {"father":"up_center", "height":80, "width":620, "anchor":"n", "relx":0.5, "rely":0, "bg":"cyan", "frame_type":"place"}, 
    "program_status":  {"father":"up_center", "height":10, "width":620, "anchor":"s", "relx":0.5, "rely":1, "bg":"cyan", "frame_type":"place"},
    "program_process":  {"father":"up_right", "height":40, "width":120, "anchor":"center", "relx":0.5, "rely":0.55, "bg":"cyan", "frame_type":"place"},

    "folder_select":  {"father":"up_center", "height":180, "width":300, "anchor":"center", "relx":0.29, "rely":0.6, "bg":"cyan", "frame_type":"place"},
    "column_select":  {"father":"up_center", "height":120, "width":140, "anchor":"center", "relx":0.78, "rely":0.6, "bg":"cyan", "frame_type":"place"},

    "cell_section_title":  {"father":"low_left", "height":50, "width":250, "anchor":"n", "relx":0.5, "rely":0.05, "bg":"cyan", "frame_type":"place"},
    "border_section_title":  {"father":"low_center", "height":50, "width":250, "anchor":"n", "relx":0.5, "rely":0.05, "bg":"cyan", "frame_type":"place"},
    "color_section_title":  {"father":"low_right", "height":50, "width":250, "anchor":"n", "relx":0.5, "rely":0.05, "bg":"cyan", "frame_type":"place"},

    "cell_section_config":  {"father":"low_left", "height":200, "width":280, "anchor":"n", "relx":0.5, "rely":0.3, "bg":"cyan", "frame_type":"place"},
    "border_section_config":  {"father":"low_center", "height":200, "width":280, "anchor":"n", "relx":0.5, "rely":0.3, "bg":"cyan", "frame_type":"place"},
    "color_section_config":  {"father":"low_right", "height":200, "width":280, "anchor":"n", "relx":0.5, "rely":0.3, "bg":"cyan", "frame_type":"place"},

    "color_ac_select":  {"father":"color_section_config", "height":40, "width":40, "anchor":"center", "relx":0.2, "rely":0.3, "bg":"lightcoral", "frame_type":"place"},
    "color_in_select":  {"father":"color_section_config", "height":40, "width":40, "anchor":"center", "relx":0.5, "rely":0.3, "bg":"lightcoral", "frame_type":"place"},
    "color_ti_select":  {"father":"color_section_config", "height":40, "width":40, "anchor":"center", "relx":0.8, "rely":0.3, "bg":"lightcoral", "frame_type":"place"},
    "color_bo_select":  {"father":"color_section_config", "height":40, "width":40, "anchor":"center", "relx":0.5, "rely":0.75, "bg":"lightcoral", "frame_type":"place"},

    "color_ac_select_title":  {"father":"color_section_config", "height":10, "width":60, "anchor":"center", "relx":0.2, "rely":0.13, "bg":"lightcoral", "frame_type":"place"},
    "color_in_select_title":  {"father":"color_section_config", "height":10, "width":60, "anchor":"center", "relx":0.5, "rely":0.13, "bg":"lightcoral", "frame_type":"place"},
    "color_ti_select_title":  {"father":"color_section_config", "height":10, "width":60, "anchor":"center", "relx":0.8, "rely":0.13, "bg":"lightcoral", "frame_type":"place"},
    "color_bo_select_title":  {"father":"color_section_config", "height":10, "width":60, "anchor":"center", "relx":0.5, "rely":0.58, "bg":"lightcoral", "frame_type":"place"},

    "border_le_select":  {"father":"border_section_config", "height":70, "width":70, "anchor":"center", "relx":0.25, "rely":0.28, "bg":"lightcoral", "frame_type":"place"},
    "border_ri_select":  {"father":"border_section_config", "height":70, "width":70, "anchor":"center", "relx":0.25, "rely":0.78, "bg":"lightcoral", "frame_type":"place"},
    "border_up_select":  {"father":"border_section_config", "height":70, "width":70, "anchor":"center", "relx":0.75, "rely":0.28, "bg":"lightcoral", "frame_type":"place"},
    "border_low_select":  {"father":"border_section_config", "height":70, "width":70, "anchor":"center", "relx":0.75, "rely":0.78, "bg":"lightcoral", "frame_type":"place"},

    "border_le_select_title":  {"father":"border_section_config", "height":10, "width":60, "anchor":"center", "relx":0.25, "rely":0.06, "bg":"lightcoral", "frame_type":"place"},
    "border_ri_select_title":  {"father":"border_section_config", "height":10, "width":60, "anchor":"center", "relx":0.25, "rely":0.56, "bg":"lightcoral", "frame_type":"place"},
    "border_up_select_title":  {"father":"border_section_config", "height":10, "width":60, "anchor":"center", "relx":0.75, "rely":0.06, "bg":"lightcoral", "frame_type":"place"},
    "border_low_select_title":  {"father":"border_section_config", "height":10, "width":60, "anchor":"center", "relx":0.75, "rely":0.56, "bg":"lightcoral", "frame_type":"place"},

    "column_title_def":  {"father":"cell_section_config", "height":20, "width":200, "anchor":"center", "relx":0.5, "rely":0.1, "bg":"lightcoral", "frame_type":"place"},
    "fontsize_def":  {"father":"cell_section_config", "height":20, "width":100, "anchor":"center", "relx":0.5, "rely":0.38, "bg":"lightcoral", "frame_type":"place"},
    "alignment_le_def":  {"father":"cell_section_config", "height":60, "width":60, "anchor":"center", "relx":0.2, "rely":0.78, "bg":"lightcoral", "frame_type":"place"},
    "alignment_ce_def":  {"father":"cell_section_config", "height":60, "width":60, "anchor":"center", "relx":0.5, "rely":0.78, "bg":"lightcoral", "frame_type":"place"},
    "alignment_ri_def":  {"father":"cell_section_config", "height":60, "width":60, "anchor":"center", "relx":0.8, "rely":0.78, "bg":"lightcoral", "frame_type":"place"},

    "alignment_def_title":  {"father":"cell_section_config", "height":10, "width":150, "anchor":"center", "relx":0.5, "rely":0.55, "bg":"lightcoral", "frame_type":"place"},
    "fontsize_def_title":  {"father":"cell_section_config", "height":10, "width":80, "anchor":"center", "relx":0.5, "rely":0.28, "bg":"lightcoral", "frame_type":"place"},

    "default_mode_select":  {"father":"up_right", "height":20, "width":168, "anchor":"s", "relx":0.8, "rely":1, "bg":"lightcoral", "frame_type":"place"},

    "input_column_def":  {"father":"column_select", "height":20, "width":80, "anchor":"center", "relx":0.5, "rely":0.35, "bg":"lightcoral", "frame_type":"place"},
    "output_column_def":  {"father":"column_select", "height":20, "width":80, "anchor":"center", "relx":0.5, "rely":0.75, "bg":"lightcoral", "frame_type":"place"},

    "input_column_def_title":  {"father":"column_select", "height":10, "width":60, "anchor":"center", "relx":0.5, "rely":0.2, "bg":"lightcoral", "frame_type":"place"},
    "output_column_def_title":  {"father":"column_select", "height":10, "width":60, "anchor":"center", "relx":0.5, "rely":0.6, "bg":"lightcoral", "frame_type":"place"},

    "archive_select":  {"father":"folder_select", "height":20, "width":250, "anchor":"center", "relx":0.5, "rely":0.30, "bg":"lightcoral", "frame_type":"place"},
    "path_select":  {"father":"folder_select", "height":20, "width":250, "anchor":"center", "relx":0.5, "rely":0.7, "bg":"lightcoral", "frame_type":"place"},

    "archive_select_title": {"father":"folder_select", "height":10, "width":60, "anchor":"center", "relx":0.5, "rely":0.15, "bg":"lightcoral", "frame_type":"place"},
    "path_select_title": {"father":"folder_select", "height":10, "width":60, "anchor":"center", "relx":0.5, "rely":0.55, "bg":"lightcoral", "frame_type":"place"}

}
import os
from tkinter import filedialog
import verificacao_sites.config.settings as settings

def file_selector():
    excel_file = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")])
    excel_filename = os.path.splitext(os.path.basename(excel_file))[0]
    excel_future_name = excel_filename + '_result.xlsx'

    inf_saves(excel_file, excel_filename, excel_future_name)

def directory_selector():
    directory = filedialog.askdirectory()

    inf_saves(directory=directory)

def inf_saves(file=None, filename=None, future_filename=None, directory=None):
    if file != None:
        settings.files_dict["file"] = file
        settings.files_dict["filename"] = filename
        settings.files_dict["future_filename"] = future_filename
    if directory != None:
        settings.files_dict["directory"] = directory
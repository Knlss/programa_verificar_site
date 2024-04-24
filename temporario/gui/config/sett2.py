import tkinter as tk
import os
from tkinter import filedialog
from openpyxl import load_workbook

class ElementCommand:
    def __init__(self):
        self.files_dict = {'file': None, 'filename': None, 'future_filename': None, 'directory': None}

    def limit_lenght(self, stringvar, limit):
        value = stringvar.get()
        if len(value) > limit:
            stringvar.set(value[:limit])

    def file_selector(self):
        excel_file = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")])
        excel_filename = os.path.splitext(os.path.basename(excel_file))[0]
        excel_future_name = excel_filename + '_result.xlsx'
        self.inf_saves(excel_file, excel_filename, excel_future_name)

    def directory_selector(self):
        directory = filedialog.askdirectory()
        self.inf_saves(directory=directory)

    def inf_saves(self, file=None, filename=None, future_filename=None, directory=None):
        if file != None:
            self.files_dict["file"] = file
            self.files_dict["filename"] = filename
            self.files_dict["future_filename"] = future_filename
        if directory != None:
            self.files_dict["directory"] = directory
import tkinter as tk

def limit_length(*args):
    value = element_config.config_variables["inout_stringvar"].get()
    if len(value) > element_config.config_variables["inout_limit_lenght"]:
        element_config.config_variables["inout_stringvar"].set(value[:element_config.config_variables["inout_limit_lenght"]])

config_variables = {
    "inout_limit_lenght":1,
    "inout_stringvar": tk.StringVar(),
    "inout_entry": config_variables["inout_stringvar"].trace_add("write", gui.limit_length)
}

class CommandElement:
    def __init__(self):
        self.config_variables = {
            "inout_limit_lenght":1,
            "inout_stringvar": tk.StringVar(),
            "inout_entry": self.config_variables["inout_stringvar"].trace_add("write", gui.limit_length)
        }

    def limit_lenght(self, stringvar, limit):
        stringvar.trace_add("write", self.limit_lenght)
        pass
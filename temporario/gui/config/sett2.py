import tkinter as tk

class ElementCommand:

    def limit_lenght(self, stringvar, limit):
        value = stringvar.get()
        if len(value) > limit:
            stringvar.set(value[:limit])
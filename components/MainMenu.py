import tkinter as tk
from style import styles


class MainMenu(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background = styles.BACKGROUND)
        self.init_widgets()
    
    def init_widgets(self):
        tk.Button(
            self,
            text = 'Hacer un Test',
            command = lambda: self.manager.home_to_select(),
            **styles.STYLE,
            relief = tk.FLAT,
            activebackground = styles.BACKGROUND,
            activeforeground =styles.TEXT
        ).pack(**styles.PACK)

        tk.Button(
            self,
            text = 'Crear un Test',
            command = lambda: self.manager.home_to_create(),
            **styles.STYLE,
            relief = tk.FLAT,
            activebackground = styles.BACKGROUND,
            activeforeground =styles.TEXT
        ).pack(**styles.PACK)

        tk.Button(
            self,
            text = 'Editar un Test',
            command = lambda: self.manager.home_to_update(),
            **styles.STYLE,
            relief = tk.FLAT,
            activebackground = styles.BACKGROUND,
            activeforeground =styles.TEXT
        ).pack(**styles.PACK)

        tk.Button(
            self,
            text = 'Eliminar un Test',
            command = lambda: self.manager.home_to_delete(),
            **styles.STYLE,
            relief = tk.FLAT,
            activebackground = styles.BACKGROUND,
            activeforeground =styles.TEXT
        ).pack(**styles.PACK)
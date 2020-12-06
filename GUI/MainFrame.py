import tkinter as tk
from GUI.GameFrame import GameFrame
from GUI.OptionsFrame import OptionsFrame


class MainFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.game_frame = GameFrame(self, bg='#008000')
        self.options_frame = OptionsFrame(self, bg='#cccccc')
        self.bind('<Configure>', lambda _: self.on_resize())

    def on_resize(self):
        self.options_frame.place(x=self.winfo_width() - 288, width=288, relheight=1)
        self.game_frame.place(x=0, width=self.winfo_width() - 288, relheight=1)

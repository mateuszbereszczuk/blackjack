import tkinter as tk
from GUI.GameFrame import GameFrame
from GUI.OptionsFrame import OptionsFrame


class MainFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.game_frame = GameFrame(self, bg='#008000')
        self.options_frame = OptionsFrame(self, bg='#cccccc')

        self.game_frame.place(relwidth=0.8, relheight=1)
        self.options_frame.place(relx=0.8, relwidth=0.2, relheight=1)

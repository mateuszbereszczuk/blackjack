from GUI.MainFrame import MainFrame
import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    MainFrame(root, width=1440, height=1000).pack(fill="both", expand=True)
    root.mainloop()

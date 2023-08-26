#!/usr/bin/env python3
import tkinter as tk
import prem_search

header_size = 30
text_size = 21
bg_color = "white"

class FootyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set layout

class HeaderLabel(tk.Label):
    def __init__(self, master, text="Header"):
        super().__init__(master)
        self.config(font=("Arial", header_size), bg="white", text=text)
        self.pack(side="left")

def set_fullscreen(window):
    def callback():
        window.attributes('-fullscreen', True)
    window.after(100, callback)

def main():
    root = FootyApp()
    header = HeaderLabel(root, "Footy")

    set_fullscreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()

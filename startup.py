#!/usr/bin/env python3
import tkinter as tk

def main():
    root = tk.Tk()

    tk.Label(root, text="Footy").pack()

    def set_fullscreen():
        root.attributes("-fullscreen", True)

    root.after(100, set_fullscreen)

    root.mainloop()

if __name__ == "__main__":
    main()

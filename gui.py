import tkinter
from tkinter import *

from core import split_entry
from password import make_password


def center(windows):
    windows.update_idletasks()
    width = windows.winfo_width()
    height = windows.winfo_height()
    x = (windows.winfo_screenwidth() // 2) - (width // 2)
    y = (windows.winfo_screenheight() // 2) - (height // 2)
    windows.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def get_password(event):
    password, salt, length = split_entry(event.widget.get())
    root.clipboard_clear()
    root.clipboard_append(make_password(password, salt, length))
    root.update()
    root.withdraw()


if __name__ == '__main__':
    root = tkinter.Tk()
    root.overrideredirect(1)
    root.geometry('{}x{}'.format("140", "20"))
    root.resizable(width=FALSE, height=FALSE)
    center(root)
    entry = Entry(root, show="*", width=140)
    entry.bind('<Return>', get_password)
    entry.pack(fill=BOTH, expand=True)
    entry.focus()
    root.mainloop()

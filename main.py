# import tkinter for creating GUI apps
import tkinter as tk
from tkinter import filedialog, messagebox

# create main application window.
root = tk.Tk() 

#set window titlebar name.
root.title("simple Text Editor")

#window size.
root.geometry("800x600")


#--------------- TEXT EDITOR AREA ----------------------------------------

#create text area in text editor.
text = tk.Text(
    root,                     #parent window
    wrap = tk.WORD,           # wrap text by word (not char)
    font = ("Helvetica", 12)  # font style & size.

)

text.pack(expand = True,fill = tk.BOTH)

# starts and keeps the window open.
root.mainloop()


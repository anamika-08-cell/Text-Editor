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

#main logic starts now.

# function 1 - to create a new file
def new_file( ):
    text.delete(1.0, tk.END)

# function 2 - to open a new file.
def open_file():
    #open file dialogue dikhana hoga.
    file_path= filedialog.askopenfile(
        defaultextension=" .txt", 
        filetypes= [("Text Files", "*.txt")]  
    )

    if file_path:
        #open selected file
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())


#function 3 - save the file
def save_file():
 #open save file dialogue
 file_path= filedialog.askopenfilename(
     defaultextension=" .txt", 
     filetypes= [("Text Files", "*.txt")] 
 )

 if file_path:
    with open(file_path, "w") as file:
       file.write(text.get(1.0, tk.END))
 
 messagebox.showinfo("Info", "File saved successfully")

# starts and keeps the window open.
root.mainloop()


from tkinter import *
import tkinter.filedialog as fd
from tkinter.scrolledtext import ScrolledText
import platform
filepath = ""

def setfilepath(path):
	global filepath
	filepath = path

def openfile():
	path = fd.askopenfilename()
	if not path==():
		with open(path, 'r') as f:
			code = f.read()
			editor.delete('1.0', END)
			editor.insert("1.0", code)
			setfilepath(path)

def savefile():
	if filepath == "":
		saveasfile()
	else:
		with open(filepath, 'w') as f:
			code = editor.get('1.0', END)
			f.write(code)

def saveasfile():
	path = fd.asksaveasfilename()
	if not path==():
		with open(path, 'w') as f:
			code = editor.get('1.0', END)
			f.write(code)
			setfilepath(path)

root = Tk()
root.wm_title("Tedit")
editor = ScrolledText(wrap=WORD, undo=True)
editor.pack(fill=BOTH, expand=True)
menubar = Menu(root)
fileMenu = Menu(menubar, tearoff=False)
fileMenu.add_command(label="Open", command=openfile)
fileMenu.add_command(label="Save", command=savefile)
fileMenu.add_command(label="Save As", command=saveasfile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.destroy)
editMenu = Menu(menubar, tearoff=False)
editMenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: editor.event_generate('<<Cut>>'))
editMenu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: editor.event_generate('<<Copy>>'))
editMenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: editor.event_generate('<<Paste>>'))
editMenu.add_separator()
editMenu.add_command(label="Undo", accelerator="Ctrl+Z", command=editor.edit_undo)
editMenu.add_command(label="Redo", accelerator="Ctrl+Shift+Z", command=editor.edit_redo)
menubar.add_cascade(label="File", menu=fileMenu)
menubar.add_cascade(label="Edit", menu=editMenu)
root.config(menu=menubar)
root.bind()
root.mainloop()
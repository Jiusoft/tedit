from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import platform

filepath = ""

def setfilepath(path):
	global filepath
	filepath = path

def openfile():
	path = fd.askopenfilename()
	if path == "":
		mb.showerror("Tedit","Vous n'avez sélectionné aucun fichier texte !")
	else:
		with open(path, 'r') as f:
			code = f.read()
			editor.delete('1.0', END)
			editor.insert("1.0", code)
			setfilepath(path)
			root.wm_title("Tedit - " + filepath)

def savefile():
	if filepath == "":
		mb.showerror("Tedit","Vous n'avez aucun nom à votre fichier texte !")
	else:
		with open(filepath, 'w') as f:
			code = editor.get('1.0', END)
			f.write(code)
			root.wm_title("Tedit - " + filepath)

def saveasfile():
	path = fd.asksaveasfilename()
	if path == "":
		mb.showerror("Tedit","Vous n'avez aucun nom à votre fichier texte !")
	else:
		with open(path, 'w') as f:
			code = editor.get('1.0', END)
			f.write(code)
			setfilepath(path)
			root.wm_title("Tedit - " + filepath)

root = Tk()
root.wm_title("Tedit - Sans titre")
root.iconbitmap("icons/tedit.ico")
editor = ScrolledText(wrap=WORD, undo=True)
editor.pack(fill=BOTH, expand=True)
menubar = Menu(root)
fileMenu = Menu(menubar, tearoff=False)
fileMenu.add_command(label="Ouvrir", command=openfile)
fileMenu.add_command(label="Enregistrer", command=savefile, accelerator="Ctrl+S")
fileMenu.add_command(label="Enregistrer sous", command=saveasfile)
fileMenu.add_separator()
fileMenu.add_command(label="Quitter", command=root.destroy)
editMenu = Menu(menubar, tearoff=False)
editMenu.add_command(label="Couper", accelerator="Ctrl+X", command=lambda: editor.event_generate('<<Cut>>'))
editMenu.add_command(label="Copier", accelerator="Ctrl+C", command=lambda: editor.event_generate('<<Copy>>'))
editMenu.add_command(label="Coller", accelerator="Ctrl+V", command=lambda: editor.event_generate('<<Paste>>'))
editMenu.add_separator()
editMenu.add_command(label="Annuler", accelerator="Ctrl+Z", command=editor.edit_undo)
editMenu.add_command(label="Refaire", accelerator="Ctrl+Shift+Z", command=editor.edit_redo)
menubar.add_cascade(label="Fichier", menu=fileMenu)
menubar.add_cascade(label="Éditer", menu=editMenu)
root.config(menu=menubar)
root.bind()
root.mainloop()
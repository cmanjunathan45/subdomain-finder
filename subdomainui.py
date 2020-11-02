import requests
import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox
import webbrowser

root=tk.Tk()
root.title("SubDomain Scanner | Manjunathan C")
root.geometry("800x600")
root.config(bg="#1e2761")
root.iconphoto(True,tk.PhotoImage(file="icon.png"))

def scan():
	textShow.delete("1.0",END)
	url=urlEntry.get()
	if url=="":
		messagebox.showerror("Error","Please Enter An URL")
	else:
		file=open("wordlist.txt")
		content=file.read()
		subdomain=content.splitlines()
		for i in subdomain:
			sub_url=f"http://{i}.{url}"
			try:
				requests.get(sub_url)
				showText=f"{i}.{url}\n"
				textShow.insert(END,showText)
			except:
				pass

def save():
	root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
	if root.filename is None:
		return
	file_save =  str(textShow.get(1.0,END))
	root.filename.write(file_save)
	root.filename.close()

urlLabel=Label(root,text="ENTER THE URL ( Without HTTP )",bg="#1e2761",fg="white",font=("courier",15,"bold italic"))
urlLabel.place(x=330,y=20)

urlEntry=Entry(root,fg="#1e2761",bg="white",font=("courier",15,"bold italic"),width=30,borderwidth=6)
urlEntry.place(x=220,y=50)

buttonScan=Button(root,text="Scan",fg="#1e2761",bg="white",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=scan)
buttonScan.place(x=430,y=100)

buttonClear=Button(root,text="Clear",fg="#1e2761",bg="white",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=lambda:urlEntry.delete(0,END))
buttonClear.place(x=270,y=100)

textShow=Text(root,bg="white",fg="#1e2761",font=("courier",15,"bold italic"),width=50,height=16,borderwidth=6)
textShow.place(x=90,y=157)

textButtonClear=Button(root,text="Clear",bg="white",fg="#1e2761",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=lambda:textShow.delete("1.0",END))
textButtonClear.place(x=410,y=520)

textButtonSave=Button(root,text="Save",bg="white",fg="#1e2761",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=save)
textButtonSave.place(x=550,y=520)

exitButton=Button(root,text="Exit",bg="white",fg="#1e2761",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=lambda:root.destroy())
exitButton.place(x=270,y=520)

buttonContact=Button(root,text="Contact",bg="white",fg="#1e2761",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=lambda:webbrowser.open("https://github.com/cmanjunathan45"))
buttonContact.place(x=130,y=520)

root.mainloop()

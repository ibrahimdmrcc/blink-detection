from tkinter import *
from function import dino
from function import pdf_video_set
from function import healt
import webbrowser
from tkinter.ttk import Combobox
from tkinter import colorchooser

pencere = Tk()
pencere.title("EYE-CONTROL")
pencere.geometry("900x600+500+200")
pencere.resizable(FALSE, FALSE)

def choose_color():
	renk=colorchooser.askcolor(title="select color")
	pencere.config(bg=renk[1])

def start():
    basla()

def stop():
    pencere.destroy()

def basla():
	if (v.get()==3):
		healt()

	elif (v.get()==2):
		dino()

	elif (v.get()==1):
		pdf_video_set('left','right')

	elif(v.get()==4):
		webbrowser.open_new("https://www.youtube.com/")
		pdf_video_set('j','l')

	elif(v.get()==5):
		pdf_video_set(kutu1.get(),kutu2.get())
		print(kutu1.get())

v = IntVar()
radio1 = Radiobutton(pencere, text='Mode : READING', variable=v, value=1, font=("Open Sans", "10", "bold"),fg="grey").place(x=80, y=150)

radio2 = Radiobutton(pencere, text='Mode : DINO GAME', variable=v, value=2,font=("Open Sans", "10", "bold"),fg="gray").place(x=80, y=190)

radio3 = Radiobutton(pencere, text='Mode : HEALTHY EYE', variable=v, value=3, font=("Open Sans", "10", "bold"),fg="gray").place(x=80, y=230)

radio4 = Radiobutton(pencere, text='Mode : YOUTUBE VIDEO CONTROLLER', variable=v, value=4, font=("Open Sans", "10", "bold"),fg="gray").place(x=80, y=270)

radio5 = Radiobutton(pencere, text='Set Mode', variable=v, value=5, font=("Open Sans", "10", "bold"),fg="gray").place(x=500, y=135)

backGround = Button(pencere,text="choose background color",command=choose_color,borderwidth=2, relief="groove", bg="grey").place(x=750, y=570)

Button(text="START", command=start, width=20, height=3, borderwidth=5, relief="groove", bg="green", fg="white",font=("Open Sans", "10", "bold")).place(x=240, y=400)

Button(text="QUIT", command=stop, width=20, height=3, borderwidth=5, relief="groove", bg="#f10400", fg="white",font=("Open Sans", "10", "bold")).place(x=460, y=400)


lis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
	   'w', 'x', 'y', 'z','f1', 'f2', 'f3', 'f4', 'backspace', 'alt', 'left', 'right', 'up', 'down', 'tab', 'enter',
	    'ctrl', 'delete','end', '+', '-', '/', '<', '>', '\"']


kutu1 = Combobox(pencere, value=lis)
kutu2 = Combobox(pencere, value=lis)
kutu1.place(x=630, y=185)
kutu2.place(x=630, y=225)


Label(text="AVAILABLE MODES", bg="#2230af", borderwidth=5, relief="groove", width=40, height=4, fg="white", font=("Open Sans", "10", "bold normal" )).place(x=30, y=30)

Label(text="SET MODE", bg="#2230af", borderwidth=5, relief="groove", width=40, height=4, fg="white", font=("Times", "11", "bold normal")).place(x=470,y=30)

Label(text="-> LEFT EYE", width=10, height=1, fg="gray", pady=8, font=("Open Sans", "10", "bold")).place(x=500,y=185)

Label(text=" -> RIGHT EYE", width=10, height=1, fg="gray", pady=8, font=("Open Sans", "10", "bold")).place(x=500,y=225)

Label(text="(Please click for set mode)", width=25, height=1, fg="red",font=("Open Sans", "10", "normal")).place(x=600, y=135)

mainloop()
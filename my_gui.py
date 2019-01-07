from tkinter import *
from datetime import datetime
import time

root = Tk()
root.title("Calculator")
root.geometry("600x350+400+160")
root.resizable(False, False)

icon = PhotoImage(file='Apps-accessories-calculator-icon.png')
root.call('wm', 'iconphoto', root._w, icon)
root.configure(background="#CEECF5")

f1 = Frame(root, width=300, height = 136, bd= 3, bg="#FACC2E")
f1.place(x=55, y= 60)

f2 = Frame(root, width=163,height=70,bd=1,bg="#F6CEF5")
f2.place(x=362,y=60)

title = Label(root, font=('Times',16,'bold'),bg="#CEECF5", text="Calculator")
title.place(x=240,y=10)

themes = Label(f2, font=('Times',8,'bold'),bg="#F6CEF5", text="Themes")
themes.place(x=2,y=2)

num1 = Label(f1, font=('Times', 14, 'bold'), text="Number 1")
num1.place(x=20, y=32)

num2 = Label(f1, font=('Times', 14, 'bold'), text="Number 2")
num2.place(x=20, y=70)

number1 = StringVar()
number2 = StringVar()

txtbox1 = Entry(f1, width= 10, font=('Times', 14, 'bold'), textvariable=number1, bg="#CEF6EC")
txtbox1.place(x=120, y=32)

txtbox2 = Entry(f1, width= 10, font=('Times', 14, 'bold'), textvariable=number2, bg="#CEF6EC")
txtbox2.place(x=120, y=70)

txt = Text (root, width=16, height=2,  font=('Times', 14, 'bold'), bg="#F2F5A9")
txt.place(x=362, y=148)

def date_time():
	#_time = time.asctime(time.localtime(time.time()))
	_time = time.ctime()
	return _time
ltime = Label(root,font=('Times', 10, 'bold'), text=date_time())
ltime.place(x=57,y=16)

'''def copy_txt():
    mytext = txtbox1.get()
    txt.insert(END, mytext)
    txtbox1.delete(0, END)'''
def change_theme1():
	root.configure(background="#BCA9F5")
	if title.configure(background="#BCA9F5")==False:
		title.configure(background="#BCA9F5")
def change_theme2():
	root.configure(background="#C8FE2E")
	if title.configure(background="#C8FE2E")==False:
		title.configure(background="#C8FE2E")
def change_theme3():
	root.configure(background="#FE9A2E")
	if title.configure(background="#FE9A2E")==False:
		title.configure(background="#FE9A2E")

def addition():
    num1 = float(number1.get())
    num2 = float(number2.get())
    result_add = num1 + num2
    if txt == " ":
    	txt.insert(END, result_add)
    else:
    	reset()
    	txt.insert(END, result_add)

def substract():
    num1 = float(number1.get())
    num2 = float(number2.get())
    result_sub = num1 - num2
    if txt == " ":
    	txt.insert(END, result_sub)
    else:
    	reset()
    	txt.insert(END, result_sub)

def multiply():
	num1 = float(number1.get())
	num2 = float(number2.get())
	result_mult = num1 * num2
	if txt == " ":
		txt.insert(END, result_mult)
	else:
		reset()
		txt.insert(END, result_mult)

def division():
    num1 = float(number1.get())
    num2 = float(number2.get())
    result_div = num1 / num2
    if txt == " ":
    	txt.insert(END, result_div)
    else:
    	reset()
    	txt.insert(END, result_div)

def reset():
	txtbox1.delete(0, END)
	txtbox2.delete(0, END)
	txt.delete("1.0", "end")

reset_button = Button(root,padx=6,pady=1, font=('Times',14,'bold'), text="Reset",  width=13, height=2, bg="#81F79F",fg="#642EFE", bd=3,command=reset)
reset_button.place(x=362, y=210)

theme_button1 = Button(f2, font=('Times',14,'bold'), text="",  width=3, height=1, bg="#BCA9F5",fg="#642EFE", bd=3,command=change_theme1)
theme_button1.place(x=6, y=22)

theme_button2 = Button(f2, font=('Times',14,'bold'), text="",  width=3, height=1, bg="#C8FE2E",fg="#642EFE", bd=3,command=change_theme2)
theme_button2.place(x=58, y=22)

theme_button3 = Button(f2, font=('Times',14,'bold'), text="",  width=3, height=1, bg="#FE9A2E",fg="#642EFE", bd=3,command=change_theme3)
theme_button3.place(x=110, y=22)

addition_but = Button(root,font=('Times',14,'bold'), text="+",  width=5, height=2, bg="#A9E2F3",fg="#642EFE", bd=3, command=addition)
addition_but.place(x=57, y=210)

substract_but = Button(root,font=('Times',14,'bold'), text="-",  width=5, height=2, bg="#A9E2F3",fg="#642EFE", bd=3, command=substract)
substract_but.place(x=135, y=210)

multiply_but = Button(root,font=('Times',14,'bold'), text="*",  width=5, height=2, bg="#A9E2F3",fg="#642EFE", bd=3, command=multiply)
multiply_but.place(x=215, y=210)

division_but = Button(root,font=('Times',14,'bold'), text="/",  width=5, height=2, bg="#A9E2F3",fg="#642EFE", bd=3, command=division)
division_but.place(x=290, y=210)

root.mainloop()

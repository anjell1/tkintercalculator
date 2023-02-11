from tkinter import *
import tkinter.messagebox
import math
import webbrowser
import speech_recognition as sr
import pyttsx3 as p
import datetime
import webbrowser
import time
from pyttsx3 import speak
import tkinter.filedialog
import subprocess

## speak part
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
###
root = Tk()
root.geometry("280x390")
root.title("Calculator")
root.resizable(width= False , height= False)
switch = None
#
# Button on press
def btn1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


def btn2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def btn3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def btn4_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


def btn5_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


def btn6_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


def btn7_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


def btn8_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


def btn9_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')


def btn0_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)


def btnp_clicked():
    pos = len(disp.get())
    disp.insert(pos, '+')



def btnm_clicked():
    pos = len(disp.get())
    disp.insert(pos, '-')


def btnml_clicked():
    pos = len(disp.get())
    disp.insert(pos, '*')


def btnd_clicked():
    pos = len(disp.get())
    disp.insert(pos, '/')


def btnc_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '0')


def sin_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else:
            ans = math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def cos_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.cos(math.radians(ans))
        else:
            ans = math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
        
                
def tan_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.tan(math.radians(ans))
        else:
            ans = math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def arcsin_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.asin(ans))
        else:
            ans = math.asin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
def arccos_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.acos(ans))
        else:
            ans = math.acos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
def arctan_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.atan(ans))
        else:
            ans = math.atan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def pow_clicked():
    pos = len(disp.get())
    disp.insert(pos, '**')


def round_clicked():
    try:
        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def logarithm_clicked():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def fact_clicked():
    try:
        ans = float(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def sqr_clicked():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def dot_clicked():
    pos = len(disp.get())
    disp.insert(pos, '.')


def pi_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))

def e_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))

def bl_clicked():
    pos = len(disp.get())
    disp.insert(pos, '(')

def br_clicked():
    pos = len(disp.get())
    disp.insert(pos, ')')

def del_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])

def conv_clicked():
    global switch
    if switch is None:
        switch = True
        conv_btn['text'] = "Deg"
    else:
        switch = None
        conv_btn['text'] = "Rad"

def ln_clicked():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def mod_clicked():
    pos = len(disp.get())
    disp.insert(pos, '%')

def btneq_clicked(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)

    except:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
# Label
data = StringVar()

disp = Entry(root, font="Arial 26", fg="black", bg="#FFEFDB",bd=2, justify=LEFT, insertbackground="#abbab1", cursor="arrow")
disp.bind("<Return>", btneq_clicked)
disp.bind("<Escape>", btnc_clicked)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.bind("<Key-.>", key_event)
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=False, fill=BOTH)
# Row 1 Buttons
btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=False, fill=BOTH)

btnc = Button(btnrow1, text="C", font="Arial 26", relief=RAISED  , bd=2, command=btnc_clicked, fg="green", bg="#333333",width=3,height=1)
btnc.pack(side=LEFT, expand=False, fill=BOTH)
def b_h24(e24):
    btnc["bg"] = "white"

def b_l24(e24):
    btnc["bg"] = "#333333"

btnc.bind("<Enter>",b_h24)
btnc.bind("<Leave>",b_l24)

mod_btn = Button(btnrow1, text="%", font="Arial 26", relief=RAISED, bd=2, command=mod_clicked, fg="lightgreen", bg="#333333",width=3,height=1)
mod_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h20(e20):
    mod_btn["bg"] = "darkgray"

def b_l20(e20):
    mod_btn["bg"] = "#333333"

mod_btn.bind("<Enter>",b_h20)
mod_btn.bind("<Leave>",b_l20)

btnd = Button(btnrow1, text="/", font="Arial 26", relief=RAISED, bd=2, command=btnd_clicked, fg="lightgreen", bg="#333333",width=3,height=1)
btnd.pack(side=LEFT, expand=False, fill=BOTH)
def b_h28(e28):
    btnd["bg"] = "darkgray"

def b_l28(e28):
    btnd["bg"] = "#333333"

btnd.bind("<Enter>",b_h28)
btnd.bind("<Leave>",b_l28)

btnml = Button(btnrow1, text="*", font="Arial 26", relief=RAISED, bd=2, command=btnml_clicked, fg="lightgreen", bg="#333333",width=3,height=1)
btnml.pack(side=LEFT, expand=False, fill=BOTH)
def b_h02(e02):
    btnml["bg"] = "darkgray"

def b_l02(e02):
    btnml["bg"] = "#333333"

btnml.bind("<Enter>",b_h02)
btnml.bind("<Leave>",b_l02)

sqr_btn = Button(btnrow1, text=" √x ", font="Arial 26", relief=RAISED, bd=2, command=sqr_clicked, fg="white", bg="#333333",width=4,height=1)
sqr_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h22(e22):
    sqr_btn["bg"] = "darkgray"
def b_l22(e22):
    sqr_btn["bg"] = "#333333"

sqr_btn.bind("<Enter>",b_h22)
sqr_btn.bind("<Leave>",b_l22)

pi_btn = Button(btnrow1, text="π", font="Arial 26", relief=RAISED, bd=2, command=pi_clicked, fg="white", bg="#333333",width=4,height=1)
pi_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h(e):
    pi_btn["bg"] = "darkgray"

def b_l(e):
    pi_btn["bg"] = "#333333"

pi_btn.bind("<Enter>",b_h)
pi_btn.bind("<Leave>",b_l)

fact_btn = Button(btnrow1, text=" x! ", font="Arial 26", relief=RAISED, bd=2, command=fact_clicked, fg="white", bg="#333333",width=4,height=1)
fact_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h1(e1):
    fact_btn["bg"] = "darkgray"

def b_l1(e2):
    fact_btn["bg"] = "#333333"

fact_btn.bind("<Enter>",b_h1)
fact_btn.bind("<Leave>",b_l1)



# Row 2 Buttons
btnrow2 = Frame(root)
btnrow2.pack(expand=False, fill=BOTH)

btn7 = Button(btnrow2, text="7", font="Arial 26", relief=RAISED, bd=2, command=btn7_clicked, fg="white", bg="#333333",width=3,height=1)
btn7.pack(side=LEFT, expand=False, fill=BOTH)
def b_h17(e17):
    btn7["bg"] = "darkgray"
def b_l17(e17):
    btn7["bg"] = "#333333"

btn7.bind("<Enter>",b_h17)
btn7.bind("<Leave>",b_l17)

btn8 = Button(btnrow2, text="8", font="Arial 26", relief=RAISED, bd=2 ,command=btn8_clicked, fg="white", bg="#333333",width=3,height=1)
btn8.pack(side=LEFT, expand=False, fill=BOTH)
def b_h18(e18):
    btn8["bg"] = "darkgray"
def b_l18(e18):
    btn8["bg"] = "#333333"

btn8.bind("<Enter>",b_h18)
btn8.bind("<Leave>",b_l18)

btn9 = Button(btnrow2, text="9", font="Arial 26", relief=RAISED, bd=2, command=btn9_clicked, fg="white", bg="#333333",width=3,height=1)
btn9.pack(side=LEFT, expand=False, fill=BOTH)
def b_h19(e19):
    btn9["bg"] = "darkgray"
def b_l19(e19):
    btn9["bg"] = "#333333"

btn9.bind("<Enter>",b_h19)
btn9.bind("<Leave>",b_l19)

btnp = Button(btnrow2, text="+", font="Arial 26", relief=RAISED, bd=2, command=btnp_clicked, fg="lightgreen", bg="#333333",width=3,height=1)
btnp.pack(side=LEFT, expand=False, fill=BOTH)
def b_h9(e9):
    btnp["bg"] = "darkgray"
def b_l9(e9):
    btnp["bg"] = "#333333"

btnp.bind("<Enter>",b_h9)
btnp.bind("<Leave>",b_l9)

sin_btn = Button(btnrow2, text="Sin", font="Arial 26", relief=RAISED, bd=2, command=sin_clicked, fg="white", bg="#333333",width=4,height=1)
sin_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h3(e3):
    sin_btn["bg"] = "darkgray"
def b_l3(e3):
    sin_btn["bg"] = "#333333"

sin_btn.bind("<Enter>",b_h3)
sin_btn.bind("<Leave>",b_l3)

cos_btn = Button(btnrow2, text="cos", font="Arial 26", relief=RAISED, bd=2, command=cos_clicked, fg="white", bg="#333333",width=4,height=1)
cos_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h4(e4):
    cos_btn["bg"] = "darkgray"

def b_l4(e4):
    cos_btn["bg"] = "#333333"

cos_btn.bind("<Enter>",b_h4)
cos_btn.bind("<Leave>",b_l4)

tan_btn = Button(btnrow2, text="tan", font="Arial 26", relief=RAISED, bd=2, command=tan_clicked, fg="white", bg="#333333",width=4,height=1)
tan_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h5(e5):
    tan_btn["bg"] = "darkgray"

def b_l5(e5):
    tan_btn["bg"] = "#333333"

tan_btn.bind("<Enter>",b_h5)
tan_btn.bind("<Leave>",b_l5)






# Row 3 Buttons
btnrow3 = Frame(root)
btnrow3.pack(expand=False, fill=BOTH)

btn4 = Button(btnrow3, text="4", font="Arial 26", relief=RAISED, bd=2, command=btn4_clicked, fg="white", bg="#333333",width=3,height=1)
btn4.pack(side=LEFT, expand=False, fill=BOTH)
def b_h66(e66):
    btn4["bg"] = "darkgray"
def b_l66(e66):
    btn4["bg"] = "#333333"

btn4.bind("<Enter>",b_h66)
btn4.bind("<Leave>",b_l66)

btn5 = Button(btnrow3, text="5", font="Arial 26", relief=RAISED, bd=2, command=btn5_clicked, fg="white", bg="#333333",width=3,height=1)
btn5.pack(side=LEFT, expand=False, fill=BOTH)
def b_h77(e77):
    btn5["bg"] = "darkgray"
def b_l77(e77):
    btn5["bg"] = "#333333"

btn5.bind("<Enter>",b_h77)
btn5.bind("<Leave>",b_l77)

btn6 = Button(btnrow3, text="6", font="Arial 26", relief=RAISED, bd=2, command=btn6_clicked, fg="white", bg="#333333",width=3,height=1)
btn6.pack(side=LEFT, expand=False, fill=BOTH)
def b_h88(e88):
    btn6["bg"] = "darkgray"

def b_l88(e88):
    btn6["bg"] = "#333333"

btn6.bind("<Enter>",b_h88)
btn6.bind("<Leave>",b_l88)

btnm = Button(btnrow3, text="-", font="Arial 26", relief=RAISED, bd=2, command=btnm_clicked, fg="lightgreen", bg="#333333",width=3,height=1)
btnm.pack(side=LEFT, expand=False, fill=BOTH)
def b_h99(e99):
    btnm["bg"] = "darkgray"

def b_l99(e99):
    btnm["bg"] = "#333333"

btnm.bind("<Enter>",b_h99)
btnm.bind("<Leave>",b_l99)

sinh_btn = Button(btnrow3, text="Sin-¹", font="Arial 26", relief=RAISED, bd=2, command=arcsin_clicked, fg="white", bg="#333333",width=4,height=1)
sinh_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h33(e33):
    sinh_btn["bg"] = "darkgray"
def b_l33(e33):
    sinh_btn["bg"] = "#333333"

sinh_btn.bind("<Enter>",b_h33)
sinh_btn.bind("<Leave>",b_l33)

cosh_btn = Button(btnrow3, text="Cos-¹", font="Arial 26", relief=RAISED, bd=2, command=arccos_clicked, fg="white", bg="#333333",width=4,height=1)
cosh_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h44(e44):
    cosh_btn["bg"] = "darkgray"
def b_l44(e44):
    cosh_btn["bg"] = "#333333"

cosh_btn.bind("<Enter>",b_h44)
cosh_btn.bind("<Leave>",b_l44)

tanh_btn = Button(btnrow3, text="tan-¹", font="Arial 26", relief=RAISED, bd=2, command=arctan_clicked, fg="white", bg="#333333",width=4,height=1)
tanh_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h55(e55):
    tanh_btn["bg"] = "darkgray"
def b_l55(e55):
    tanh_btn["bg"] = "#333333"

tanh_btn.bind("<Enter>",b_h55)
tanh_btn.bind("<Leave>",b_l55)






### Row 4 buttons 
btnrow4 = Frame(root)
btnrow4.pack(expand=False, fill=BOTH)

btn1 = Button(btnrow4, text="1", font="Arial 26", relief=RAISED, bd=2, command=btn1_clicked, fg="white", bg="#333333",width=3,height=1)
btn1.pack(side=LEFT, expand=False, fill=BOTH)
def b_h6(e6):
    btn1["bg"] = "darkgray"

def b_l6(e6):
    btn1["bg"] = "#333333"

btn1.bind("<Enter>",b_h6)
btn1.bind("<Leave>",b_l6)
btn2 = Button(btnrow4, text="2", font="Arial 26", relief=RAISED, bd=2,  command=btn2_clicked, fg="white", bg="#333333",width=3,height=1)
btn2.pack(side=LEFT, expand=False, fill=BOTH)
def b_h7(e7):
    btn2["bg"] = "darkgray"

def b_l7(e7):
    btn2["bg"] = "#333333"

btn2.bind("<Enter>",b_h7)
btn2.bind("<Leave>",b_l7)

btn3 = Button(btnrow4, text="3", font="Arial 26", relief=RAISED, bd=2, command=btn3_clicked, fg="white", bg="#333333",width=3,height=1)
btn3.pack(side=LEFT, expand=False, fill=BOTH)
def b_h8(e8):
    btn3["bg"] = "darkgray"

def b_l8(e8):
    btn3["bg"] = "#333333"

btn3.bind("<Enter>",b_h8)
btn3.bind("<Leave>",b_l8)

br_btn = Button(btnrow4, text=" ) ", font="Arial 26", relief=RAISED, bd=2, command=br_clicked, fg="lightgreen", bg="#333333",width=3,height=1)
br_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h22(e22):
    br_btn["bg"] = "darkgray"

def b_l22(e22):
    br_btn["bg"] = "#333333"

br_btn.bind("<Enter>",b_h22)
br_btn.bind("<Leave>",b_l22)
conv_btn = Button(btnrow4, text="Rad", font="Arial 26", relief=RAISED, bd=2, command=conv_clicked, fg="white", bg="#333333",width=4,height=1)
conv_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h12(e12):
    conv_btn["bg"] = "darkgray"

def b_l12(e12):
    conv_btn["bg"] = "#333333"

conv_btn.bind("<Enter>",b_h12)
conv_btn.bind("<Leave>",b_l12)

round_btn = Button(btnrow4, text="round", font="Arial 26", relief=RAISED, bd=2, command=round_clicked, fg="white", bg="#333333",width=4,height=1)
round_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h13(e13):
    round_btn["bg"] = "darkgray"

def b_l13(e13):
    round_btn["bg"] = "#333333"

round_btn.bind("<Enter>",b_h13)
round_btn.bind("<Leave>",b_l13)

ln_btn = Button(btnrow4, text="ln", font="Arial 26", relief=RAISED, bd=2, command=ln_clicked, fg="white", bg="#333333",width=4,height=1)
ln_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h14(e14):
    ln_btn["bg"] = "darkgray"

def b_l14(e14):
    ln_btn["bg"] = "#333333"

ln_btn.bind("<Enter>",b_h14)
ln_btn.bind("<Leave>",b_l14)
#####
# Row 5 Buttons
btnrow5 = Frame(root)
btnrow5.pack(expand=False, fill=BOTH)

btn0 = Button(btnrow5, text="0", font="Arial 26", relief=RAISED, bd=2, command=btn0_clicked, fg="white", bg="#333333",width=3,height=1)
btn0.pack(side=LEFT, expand=False, fill=BOTH)
def b_h26(e26):
    btn0["bg"] = "darkgray"

def b_l26(e26):
    btn0["bg"] = "#333333"

btn0.bind("<Enter>",b_h26)
btn0.bind("<Leave>",b_l26)

dot_btn = Button(btnrow5, text="•", font="Arial 26", relief=RAISED, bd=2, command=dot_clicked, fg="white", bg="#333333",width=3,height=1)
dot_btn.pack(side=LEFT, expand=False)
def b_h23(e23):
    dot_btn["bg"] = "darkgray"

def b_l23(e23):
    dot_btn["bg"] = "#333333"

dot_btn.bind("<Enter>",b_h23)
dot_btn.bind("<Leave>",b_l23)



btneq = Button(btnrow5, text="=", font="Arial 26", relief=RAISED, bd=2, command=btneq_clicked, fg="white", bg="#333333",width=3,height=1)
btneq.pack(side=LEFT, expand=False, fill=BOTH)
def b_h27(e27):
    btneq["bg"] = "green"

def b_l27(e27):
    btneq["bg"] = "#333333"

btneq.bind("<Enter>",b_h27)
btneq.bind("<Leave>",b_l27)


bl_btn = Button(btnrow5, text=" ( ", font="Arial 26", relief=RAISED, bd=2, command=bl_clicked, fg="lightgreen", bg="#333333",width=3,height=1)
bl_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h21(e21):
    bl_btn["bg"] = "darkgray"

def b_l21(e21):
    bl_btn["bg"] = "#333333"

bl_btn.bind("<Enter>",b_h21)
bl_btn.bind("<Leave>",b_l21)

pow_btn = Button(btnrow5, text="x^y", font="Arial 26", relief=RAISED, bd=2, command=pow_clicked, fg="white", bg="#333333",width=4,height=1)
pow_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h16(e16):
    pow_btn["bg"] = "darkgray"

def b_l16(e16):
    pow_btn["bg"] = "#333333"

pow_btn.bind("<Enter>",b_h16)
pow_btn.bind("<Leave>",b_l16)

logarithm_btn = Button(btnrow5, text="log", font="Arial 26", relief=RAISED, bd=2, command=logarithm_clicked, fg="white", bg="#333333",width=4,height=1)
logarithm_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h15(e15):
    logarithm_btn["bg"] = "darkgray"

def b_l15(e15):
    logarithm_btn["bg"] = "#333333"

logarithm_btn.bind("<Enter>",b_h15)
logarithm_btn.bind("<Leave>",b_l15)

e_btn = Button(btnrow5, text="e", font="Arial 26", relief=RAISED, bd=2, command=e_clicked, fg="white", bg="#333333",width=4,height=1)
e_btn.pack(side=LEFT, expand=False, fill=BOTH)
def b_h11(e11):
    e_btn["bg"] = "darkgray"
def b_l11(e11):
    e_btn["bg"] = "#333333"

e_btn.bind("<Enter>",b_h11)
e_btn.bind("<Leave>",b_l11)
##########
# menu
###### MENU ####
def iExit():
    iExit = tkinter.messagebox.askyesno("professional calculator","Exit" )
    if iExit >0:
        speak("exit , good bye")
        root.destroy()
        return
def science ():
    root.resizable(width= False , height= False)
    speak("professional")
    root.geometry("550x390")
def standard ():
    root.resizable(width= False , height= False)
    speak("standard")
    root.geometry("280x390")
    
##
def messageWindow():
    speak ("opening calculator browser")
    Button(root, webbrowser.open_new_tab("https://www.calculator.net/")) 
## open python file

def ruNprogram():
    speak("opening BMI calculator")
    subprocess.call(["python", "C:/Users/Tazmani/Desktop/BMI.py"])
 
##


menubar = Menu()

filemenu = Menu(menubar, tearoff= 0)
menubar.add_cascade(label = "menu" , menu=filemenu)
filemenu.add_command(label = "standard", command = standard)
filemenu.add_command(label = "professional", command = science)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

editmenu = Menu(menubar, tearoff= 1)
menubar.add_cascade(label = "Edit" , menu=editmenu)
editmenu.add_command(label = "cut")
editmenu.add_command(label = "copy")
editmenu.add_separator()
editmenu.add_command(label = "paste")

BMImenu = Menu(menubar,tearoff=2)
menubar.add_cascade(label="BMI",menu = BMImenu)
BMImenu.add_command(label="Run",command=ruNprogram)

helpmenu = Menu(menubar, tearoff= 3)
menubar.add_cascade(label = "help" , menu=helpmenu)
helpmenu.add_command(label = "serach",command=messageWindow)


root.config(menu=menubar)

root.mainloop()

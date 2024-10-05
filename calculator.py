import tkinter as tk
from tkinter import ttk
import math

r = tk.Tk()
r.title('Calculator')

###################################
#       Creating Display
###################################

disp = tk.Frame(r)
res_disp = tk.Label(disp,text='0',font=('Arial',25),anchor=tk.E,bg='white') # Result display
res_disp.pack(fill=tk.X)
eq_disp = tk.Label(disp,text='0',font=('Arial',11),anchor=tk.E,bg='white') # Equation display
eq_disp.pack(fill=tk.X)
disp.pack(fill=tk.X)

###################################
#       Creating Buttons
###################################

kb1 = tk.Frame(r,bg='black')    #Row 1
tk.Button(kb1,text='%',width=5,command=lambda: percent())     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb1,text='CE',width=5,command=lambda: rem_ce())    .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb1,text='C',width=5,command=lambda: rem_c())     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb1,text='⌫',width=5,command=lambda: backspace())     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
kb1.pack(fill=tk.BOTH,expand=True)
kb2 = tk.Frame(r,bg='black')    #Row 2
tk.Button(kb2,text='1/x',width=5,command=lambda: execute('1/'))   .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb2,text='x²',width=5,command=lambda: execute('²'))    .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb2,text='√x',width=5,command=lambda: execute('√'))    .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb2,text='÷',width=5,command=lambda: set_operator('÷'))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
kb2.pack(fill=tk.BOTH,expand=True)
kb3 = tk.Frame(r,bg='black')    #Row 3
tk.Button(kb3,text='7',width=5,command=lambda: num_pressed(7))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb3,text='8',width=5,command=lambda: num_pressed(8))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb3,text='9',width=5,command=lambda: num_pressed(9))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb3,text='×',width=5,command=lambda: set_operator('×'))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
kb3.pack(fill=tk.BOTH,expand=True)
kb4 = tk.Frame(r,bg='black')    #Row 4
tk.Button(kb4,text='4',width=5,command=lambda: num_pressed(4))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb4,text='5',width=5,command=lambda: num_pressed(5))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb4,text='6',width=5,command=lambda: num_pressed(6))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb4,text='-',width=5,command=lambda: set_operator('-'))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
kb4.pack(fill=tk.BOTH,expand=True)
kb5 = tk.Frame(r,bg='black')    #Row 5
tk.Button(kb5,text='1',width=5,command=lambda: num_pressed(1))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb5,text='2',width=5,command=lambda: num_pressed(2))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb5,text='3',width=5,command=lambda: num_pressed(3))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb5,text='+',width=5,command=lambda: set_operator('+'))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
kb5.pack(fill=tk.BOTH,expand=True)
kb6 = tk.Frame(r,bg='black')    #Row 6
tk.Button(kb6,text='±',width=5,command=lambda: execute('±'))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb6,text='0',width=5,command=lambda: num_pressed(0))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb6,text='.',width=5,command=lambda: num_pressed('.'))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
tk.Button(kb6,text='=',width=5,command=lambda: execute('='))     .pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
kb6.pack(fill=tk.BOTH,expand=True)

###################################
#     Binding Keyboard Keys
###################################

r.bind("0",lambda x: num_pressed(0))
r.bind("1",lambda x: num_pressed(1))
r.bind("2",lambda x: num_pressed(2))
r.bind("3",lambda x: num_pressed(3))
r.bind("4",lambda x: num_pressed(4))
r.bind("5",lambda x: num_pressed(5))
r.bind("6",lambda x: num_pressed(6))
r.bind("7",lambda x: num_pressed(7))
r.bind("8",lambda x: num_pressed(8))
r.bind("9",lambda x: num_pressed(9))
r.bind(".",lambda x: num_pressed('.'))
r.bind("+",lambda x: set_operator('+'))
r.bind("-",lambda x: set_operator('-'))
r.bind("*",lambda x: set_operator('×'))
r.bind("/",lambda x: set_operator('÷'))
r.bind("=",lambda x: execute('='))
r.bind("<Return>",lambda x: execute('='))

###################################
#          Operations
###################################

def num_pressed(number):
    global l_op,op,r_op
    if op == '':
        l_op += str(number)
    else:
        r_op += str(number)
    eq_disp['text'] = l_op + op + r_op

def set_operator(operator):
    global l_op,op,r_op
    if l_op == '':
        l_op = '0'
    if r_op != '':
        execute('=')
    op = operator
    eq_disp['text'] = l_op + op

def execute(operation):
    global l_op,op,r_op
    if operation == '=':
        if op == '+':
            l_op = str(float(l_op)+float(r_op))
            op = ''
            r_op = ''
        elif op == '-':
            l_op = str(float(l_op)-float(r_op))
            op = ''
            r_op = ''
        elif op == '×':
            l_op = str(float(l_op)*float(r_op))
            op = ''
            r_op = ''
        elif op == '÷':
            l_op = str(float(l_op)/float(r_op))
            op = ''
            r_op = ''
    elif operation == '1/':
        if op != '':
            execute('=')
        l_op = str(1/float(l_op))
    elif operation == '²':
        if op != '':
            execute('=')
        l_op = str(float(l_op)*float(l_op))
    elif operation == '√':
        if op != '':
            execute('=')
        l_op = str(math.sqrt(float(l_op)))
    elif operation == '±':
        if op != '':
            execute('=')
        l_op = str(-float(l_op))
    eq_disp['text'] = l_op
    res_disp['text'] = l_op

def backspace():
    global l_op,op,r_op
    if r_op != '':
        r_op = r_op[0:-1]
    elif op != '':
        op = ''
    elif l_op != '':
        l_op = l_op[0:-1]
    if l_op == '':
        eq_disp['text'] = '0'
    else:
        eq_disp['text'] = l_op + op + r_op
        
def rem_ce():
    global l_op,op,r_op
    if r_op != '':
        r_op = ''
        eq_disp['text'] = l_op + op
    else:
        l_op = op = ''
        eq_disp['text'] = '0'

def rem_c():
    global l_op,op,r_op
    l_op = ''
    op = ''
    r_op = ''
    eq_disp['text'] = '0'

def percent():
    global l_op,r_op
    if r_op != '':
        r_op = str(float(l_op)*float(r_op)/100)
        eq_disp['text'] = l_op + op + r_op
        
###################################
#           Variables
###################################

l_op = ''       #Left Operand
r_op = ''       #Right Operand
op = ''         #Operator

r.mainloop()


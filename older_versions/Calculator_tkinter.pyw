__author__ = 'pbatra'


# Very first working program of Paarth Batra
#version 2.0


import Tkinter as tk
import tkFont
import math

class StandardA(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)

def fetch():
    print ta.get()

def quit():
    pf.quit()
def insert(tx):
    ta.insert(tk.END,tx)

def sum():
    a = ta.get()
    #print 0 + int(a)
    fw=open('temp.txt','w')
    fw.write("+"+a)
    fw.close()
    ta.delete(0,tk.END)

def minus():
    a = ta.get()
    #print 0 + int(a)
    fw=open('temp.txt','w')
    fw.write("-"+a)
    fw.close()
    ta.delete(0,tk.END)

def multiply():
    a = ta.get()
    #print 0 + int(a)
    fw=open('temp.txt','w')
    fw.write("*"+a)
    fw.close()
    ta.delete(0,tk.END)

def divide():
    a = ta.get()
    #print 0 + int(a)
    fw=open('temp.txt','w')
    fw.write("/"+a)
    fw.close()
    ta.delete(0,tk.END)

def mod():
    a = ta.get()
    fw=open('temp.txt','w')
    fw.write("%"+a)
    fw.close()
    ta.delete(0,tk.END)

def squareroot():
    a = float(ta.get())
    result= math.sqrt(a)
    ta.delete(0,tk.END)
    ta.insert(0,result)

def square():
    a=float(ta.get())
    result = a*a
    ta.delete(0,tk.END)
    ta.insert(0,result)


def equal():
    a=ta.get()
    fr=open('temp.txt','r')
    b=fr.read()
    fr.close()
    if b[0] == '-':
        b=b[1:]
        print "Minus Operation will be performed"
        print "Old Number :",b
        print "New number :",a
        result=float(b) - float(a)
    elif b[0] == '+':
        b=b[1:]
        print "Old number was ",b
        print "new number is ",a
        result=float(a)+float(b)

    elif b[0] == '*':
        b=b[1:]
        print "Old number was ",b
        print "new number is ",a
        result=float(a)*float(b)

    elif b[0] == '/':
        b=b[1:]
        print "Old number was ",b
        print "new number is ",a
        result=float(b)/float(a)
        

    elif b[0] == '%':
        b=b[1:]
        print "Old number was ",b
        print "new number is ",a
        result=float(b)%float(a)

    print "Result is ",result
    ta.delete(0,tk.END)
    ta.insert(0,result)



def insertButton(self,*args):
    if len(args)==6:
        parent=args[0]
        t=args[1]
        r=args[2]
        c=args[3]
        s=args[4]
        cmd=args[5]
        tk.Button(parent,text=t,command=cmd).grid(row=r,column=c,sticky=s)
    elif len(args) == 5:
        parent=args[0]
        t=args[1]
        r=args[2]
        c=args[3]
        s=args[4]
        tk.Button(parent,text=t).grid(row=r,column=c,sticky=s)
    else:
        print "Minimum Number of arguments to Button should be 5(excludinf self), passed are ", len(args)+1

def clearlast():
    v=ta.get()
    ta.delete(0,tk.END)
    ta.insert(0,v[:-1])




sa=StandardA()
sa.master.title("Calculator")
sa.master.resizable(width=0, height=0)              # making the calculator resizable


f=tkFont.Font(family='Helvetica',size=25,weight='bold')

pf=tk.Frame(height=50,width=10,bg="black",relief='sunken')             #Colouring the top level frame
pf.grid(row=5,column=0,rowspan=5,columnspan=6,sticky=tk.E+tk.W+tk.N+tk.S)


ta=tk.Entry(pf,width=50,cursor='man',bg='cyan',bd=8,highlightbackground='red'\
    ,fg='red',insertbackground='red',font=f)               #Cursor will change to man shape when used this option
ta.grid(row=0,column=0,columnspan=6,sticky=tk.E+tk.W)



insertButton(sa,pf,"1",1,0,tk.W+tk.E,lambda:insert("1"))
insertButton(sa,pf,"2",1,1,tk.W+tk.E,lambda:insert("2"))
insertButton(sa,pf,"3",1,2,tk.W+tk.E,lambda:insert("3"))
insertButton(sa,pf,"4",1,3,tk.W+tk.E,lambda:insert("4"))
insertButton(sa,pf,"5",1,4,tk.W+tk.E,lambda:insert("5"))
insertButton(sa,pf,"6",1,5,tk.W+tk.E,lambda:insert("6"))
insertButton(sa,pf,"7",2,0,tk.W+tk.E,lambda:insert("7"))
insertButton(sa,pf,"8",2,1,tk.W+tk.E,lambda:insert("8"))
insertButton(sa,pf,"9",2,2,tk.W+tk.E,lambda:insert("9"))
insertButton(sa,pf,"0",2,3,tk.W+tk.E,lambda:insert("0"))
insertButton(sa,pf,".",2,4,tk.W+tk.E,lambda:insert("."))
insertButton(sa,pf,"00",2,5,tk.W+tk.E,lambda:insert("00"))
tk.Button(pf, text="Print",command=fetch,height=1,width=10,bg='red',relief='sunken').grid(row=3,column=1,sticky=tk.W)
tk.Button(pf, text="Quit",command=quit,height=1,width=10,bg='red',relief='raised').grid(row=3,column=4,sticky=tk.W)
tk.Button(pf, text="=",command=equal,height=1,width=10,bg='red',relief='raised').grid(row=3,column=3,sticky=tk.W)
tk.Button(pf, text="Clear",command=clearlast,height=1,width=10,bg='red',relief='raised').grid(row=3,column=2,sticky=tk.W)
tk.Button(pf, text="Clear All",command=lambda:ta.delete(0,tk.END),height=1,width=10,bg='red',relief='raised').grid(row=3,column=5,sticky=tk.W)
tk.Button(pf, text="+",command=sum,height=1,width=10,bg='red',relief='raised').grid(row=3,column=0,sticky=tk.W)
tk.Button(pf, text="-",command=minus,height=1,width=10,bg='red',relief='raised').grid(row=4,column=0,sticky=tk.W)
tk.Button(pf, text="*",command=multiply,height=1,width=10,bg='red',relief='raised').grid(row=4,column=1,sticky=tk.W)
tk.Button(pf, text="/",command=divide,height=1,width=10,bg='red',relief='raised').grid(row=4,column=2,sticky=tk.W)
tk.Button(pf, text="SqRoot",command=squareroot,height=1,width=10,bg='red',relief='raised').grid(row=4,column=3,sticky=tk.W)
tk.Button(pf, text="Square",command=square,height=1,width=10,bg='red',relief='raised').grid(row=4,column=4,sticky=tk.W)
tk.Button(pf, text="%",command=mod,height=1,width=10,bg='red',relief='raised').grid(row=4,column=5,sticky=tk.W)

sa.mainloop()

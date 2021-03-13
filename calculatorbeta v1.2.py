from tkinter import *

import math

global num1

global ans

root=Tk()

#value

main=Entry(root, width=35, borderwidth=5)
main.grid(row=0, column=0, columnspan=7,padx=30,pady=20,ipadx=65)
num1=0
ans=0
sign=""
times=0
mainnum=''
mode="rad"
degangle=0
inl=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','U','R','S','T','U','V','W','X','Y','Z']

#function

def numbers(num):
    global num1
    
    for i in main.get():
        
        if i in inl:
            root.destroy()
            break
        
        else:
            continue
    
    onscreen=main.get()
    main.delete(0,END)
    main.insert(0, onscreen + str(num))

def add():
    global num1
    global sign
    global ans
    global times
    for i in main.get():
        
        if i in inl:
            root.destroy()
            break
        
        else:
            continue
    
    if times<1:
        ans=int(main.get())
        sign="+"
        main.delete(0, END)

    else:
        if sign=="+":
            ans=ans+int(main.get())
            sign="+"

        elif sign=="-":
            ans=ans-int(main.get())
            sign="+"

        elif sign=="*":
            ans=ans*int(main.get())
            sign="+"

        elif sign=="/":
            ans=ans/int(main.get())
            sign="+"

        elif sign=="**":
            ans=ans**int(main.get())
            sign="+"
        
        elif sign=="%":
            ans=ans%int(main.get())
            sign="+"

        main.delete(0, END)
    
    times+=1

def sub():
    global num1
    global sign
    global ans
    global times
    
    for i in main.get():
        
        if i in inl:
            root.destroy()
            break
        
        else:
            continue
    
    if times<1:
        ans=int(main.get())
        sign="-"
        main.delete(0, END)

    else:
        if sign=="+":
            ans=ans+int(main.get())
            sign="-"

        elif sign=="-":
            ans=ans-int(main.get())
            sign="-"

        elif sign=="*":
            ans=ans*int(main.get())
            sign="-"

        elif sign=="/":
            ans=ans/int(main.get())
            sign="-"

        elif sign=="**":
            ans=ans**int(main.get())
            sign="-"

        elif sign=="%":
            ans=ans%int(main.get())
            sign="-"

        main.delete(0, END)

    times+=1

def mul():
    global num1
    global sign
    global ans
    global times
    
    for i in main.get():
        
        if i in inl:
            root.destroy()
            break
        
        else:
            continue
    
    if times<1:
        ans=int(main.get())
        sign="*"
        main.delete(0, END)
    
    else:
        if sign=="+":
            ans=ans+int(main.get())
            sign="*"

        elif sign=="-":
            ans=ans-int(main.get())
            sign="*"

        elif sign=="*":
            ans=ans*int(main.get())
            sign="*"

        elif sign=="/":
            ans=ans/int(main.get())
            sign="*"

        elif sign=="**":
            ans=ans**int(main.get())
            sign="*"
        
        elif sign=="%":
            ans=ans%int(main.get())
            sign="*"

        main.delete(0, END)

    times+=1

def div():
    global num1
    global sign
    global ans
    global times

    for i in main.get():
        
        if i in inl:
            root.destroy()
            break
        
        else:
            continue
    
    if times<1:    
        ans=int(main.get())
        sign="/"
        main.delete(0, END)

    else:
        if sign=="+":
            ans=ans+int(main.get())
            sign="/"

        elif sign=="-":
            ans=ans-int(main.get())
            sign="/"

        elif sign=="*":
            ans=ans*int(main.get())
            sign="/"

        elif sign=="/":
            ans=ans/int(main.get())
            sign="/"

        elif sign=="**":
            ans=ans**int(main.get())
            sign="/"
        
        elif sign=="%":
            ans=ans%int(main.get())
            sign="/"    
        main.delete(0, END)

    times+=1

def expo():
    global num1
    global sign
    global ans
    global times

    for i in main.get():
        
        if i in inl:
            root.destroy()
            break
        
        else:
            continue
    
    if times<1:    
        ans=int(main.get())
        sign="**"
        main.delete(0, END)

    else:
        if sign=="+":
            ans=ans+int(main.get())
            sign="**"

        elif sign=="-":
            ans=ans-int(main.get())
            sign="**"

        elif sign=="*":
            ans=ans*int(main.get())
            sign="**"

        elif sign=="/":
            ans=ans/int(main.get())
            sign="**"
        
        elif sign=="**":
            ans=ans**int(main.get())
            sign="**"

        elif sign=="%":
            ans=ans%int(main.get())
            sign="**"

        main.delete(0, END)

    times+=1

def r():
    global num1
    global sign
    global ans
    global times

    for i in main.get():
        
        if i in inl:
            root.destroy()
            break
        
        else:
            continue
    
    if times<1:    
        ans=int(main.get())
        sign="%"
        main.delete(0, END)

    else:
        if sign=="+":
            ans=ans+int(main.get())
            sign="%"

        elif sign=="-":
            ans=ans-int(main.get())
            sign="%"

        elif sign=="*":
            ans=ans*int(main.get())
            sign="%"

        elif sign=="/":
            ans=ans/int(main.get())
            sign="%"
        
        elif sign=="**":
            ans=ans**int(main.get())
            sign="%"

        elif sign=="%":
            ans=ans%int(main.get())
            sign="%"

        main.delete(0, END)

    times+=1

def sin():
    global ans
    global Mode
    global degangle

    for i in main.get():
        
        if i in inl:
            root.destroy()
            break
        
        else:
            continue
    
    if mode=="rad":
        ans=math.sin(int(main.get()))
    
        button1.config(state=DISABLED)
        button2.config(state=DISABLED)    
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)
        button0.config(state=DISABLED)

    elif mode=="deg":
        degangle=int(main.get())*0.01745329251994329576923690768489
        ans=math.sin(degangle)
    
        button1.config(state=DISABLED)
        button2.config(state=DISABLED)    
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)
        button0.config(state=DISABLED)
    
    main.insert(0, ans)

def cos():
    global ans
    global Mode
    global degangle
    
    for i in main.get():
        
        if i in inl:
            root.destroy()
            break
        
        else:
            continue
    
    if mode=="rad":
        ans=math.cos(int(main.get()))
    
        button1.config(state=DISABLED)
        button2.config(state=DISABLED)    
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)
        button0.config(state=DISABLED)

    elif mode=="deg":
        degangle=int(main.get())*0.01745329251994329576923690768489
        ans=math.cos(degangle)
    
        button1.config(state=DISABLED)
        button2.config(state=DISABLED)    
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)
        button0.config(state=DISABLED)
    
    main.insert(0, ans)

def tan():
    global ans
    global Mode
    global degangle
    
    for i in main.get():
        
        if i in inl:
            root.destroy()
            break
        
        else:
            continue
    
    if mode=="rad":
        ans=math.tan(int(main.get()))
    
        button1.config(state=DISABLED)
        button2.config(state=DISABLED)    
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)
        button0.config(state=DISABLED)

    elif mode=="deg":
        degangle=int(main.get())*0.01745329251994329576923690768489
        ans=math.tan(degangle)
    
        button1.config(state=DISABLED)
        button2.config(state=DISABLED)    
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)
        button0.config(state=DISABLED)
    
    main.insert(0, ans)

def equ():
    global sign
    global ans
        
    for i in main.get():
        
        if i in inl:
            root.destroy()
            break
        
        else:
            continue
    
    if sign=="+":
        ans=ans+int(main.get())
    
    elif sign=="-":
        ans=ans-int(main.get())
    
    elif sign=="*":
        ans=ans*int(main.get())
    
    elif sign=="/":
        ans=ans/int(main.get())
   
    elif sign=="**":
        ans=ans**int(main.get())

    elif sign=="%":
        ans=ans%int(main.get())
    
    main.delete(0,END)
    main.insert(0, int(ans))
    
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)    
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)
    button0.config(state=DISABLED)

def c():
    global ans
    global num
    global sign
    global times

    for i in main.get():
        
        if i in inl:
            root.destroy()
            break
        
        else:
            continue
    
    ans=0
    num=0
    sign=""
    times=0
    main.delete(0, END)

    button1.config(state=NORMAL)
    button2.config(state=NORMAL)    
    button3.config(state=NORMAL)
    button4.config(state=NORMAL)
    button5.config(state=NORMAL)
    button6.config(state=NORMAL)
    button7.config(state=NORMAL)
    button8.config(state=NORMAL)
    button9.config(state=NORMAL)
    button0.config(state=NORMAL)

def cor():
    global num

    for i in main.get():
        
        if i in inl:
            root.destroy()
            break
        
        else:
            continue
    
    main.delete(0, END)

def mod():
    global mode

    for i in main.get():
        
        if i in inl:
            root.destroy()
            break
        
        else:
            continue
    
    if mode=="rad":
        mode="deg"
        buttonmod.config(text="deg")
    
    elif mode=="deg":
        mode="rad"
        buttonmod.config(text="rad")

#things

button1=Button(root,text="1",command=lambda: numbers(1),padx=35,pady=20)
button2=Button(root,text="2",command=lambda: numbers(2),padx=35,pady=20)
button3=Button(root,text="3",command=lambda: numbers(3),padx=35,pady=20)
button4=Button(root,text="4",command=lambda: numbers(4),padx=35,pady=20)
button5=Button(root,text="5",command=lambda: numbers(5),padx=35,pady=20)
button6=Button(root,text="6",command=lambda: numbers(6),padx=35,pady=20)
button7=Button(root,text="7",command=lambda: numbers(7),padx=35,pady=20)
button8=Button(root,text="8",command=lambda: numbers(8),padx=35,pady=20)
button9=Button(root,text="9",command=lambda: numbers(9),padx=35,pady=20)
button0=Button(root,text="0",command=lambda: numbers(0),padx=35,pady=20)
buttona=Button(root,text="+",padx=35,pady=20,command=add)
buttons=Button(root,text="-",padx=35,pady=20,command=sub)
buttonm=Button(root,text="*",padx=35,pady=20,command=mul)
buttond=Button(root,text="/",padx=35,pady=20,command=div)
buttone=Button(root,text="=",padx=75,pady=20,command=equ)
buttonc=Button(root,text="C",padx=35,pady=20,command=cor)
buttonce=Button(root,text="CE",padx=75,pady=20,command=c)
buttonexo=Button(root,text="**",padx=38,pady=20,command=expo)
buttonr=Button(root,text="%",padx=38,pady=20,command=r)
buttonsin=Button(root,text="Sin\u03B8",padx=38,pady=20,command=sin)
buttontan=Button(root,text="Tan\u03B8",padx=38,pady=20,command=tan)
buttoncos=Button(root,text='Cos\u03B8',padx=38,pady=20,command=cos)
buttonmod=Button(root,text="rad",padx=30,pady=20,command=mod)

#placement

button1.grid(row="2",column=0)

button2.grid(row="2",column=1)

button3.grid(row="2",column=2)

button4.grid(row="3",column=0)

button5.grid(row="3",column=1)

button6.grid(row="3",column=2)

button7.grid(row="4",column=0)

button8.grid(row="4",column=1)

button9.grid(row="4",column=2)

button0.grid(row="5",column=0)

buttone.grid(row="5",column=1,columnspan=2)

buttona.grid(row="2",column=3)

buttons.grid(row="3",column=3)

buttonm.grid(row="4",column=3)

buttond.grid(row="5",column=3)

buttonc.grid(row="1",column=0,columnspan=1)

buttonce.grid(row="1",column=2,columnspan=2)

buttonexo.grid(row="1",column=4)

buttonr.grid(row="2",column="4")

buttonsin.grid(row="3",column=4)

buttonmod.grid(row=1,column=1)

buttoncos.grid(row=4,column=4)

buttontan.grid(row=5,column=4)

root.mainloop()
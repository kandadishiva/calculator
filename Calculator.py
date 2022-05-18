from tkinter import *
from PIL import ImageTk,Image
calc=Tk()
calc.title("Calculator")
e = Entry(calc,width=50,borderwidth=5)
e.grid(row=0 ,column=0 ,columnspan= 4)

def click(n):
    a=e.get()+n
    e.delete(0,END)
    e.insert(0,a)
    return

def click_ans():
    a=e.get()
    ans=''
    c=''
    res=''
    for i in range(0,len(a)):
        if c!='':
            if(i+1!=len(a)):
                if(a[i+1]=='+' or a[i+1]=='-' or a[i+1]=='/' or a[i+1]=='*' or a[i+1]=='%'):
                    res = res + a[i]
                    if c == '+':
                        ans = float(ans) + float(res)
                    elif c == '-':
                        ans = float(ans) - float(res)
                    elif c == '*':
                        ans = float(ans) * float(res)
                    elif c == '/':
                        ans = float(ans) / float(res)
                    elif c == '%':
                        ans = float(ans) % float(res)
                    res=''
                    c = ''
                else:
                    res=res+a[i]
            else:
                res=res+a[i]
                if c == '+':
                    ans = float(ans) + float(res)
                elif c == '-':
                    ans = float(ans) - float(res)
                elif c == '*':
                    ans = float(ans) * float(res)
                elif c == '/':
                    ans = float(ans) / float(res)
                elif c == '%':
                    ans = float(ans) % float(res)
                res=''
                c = ''
        elif a[i]=='+' or a[i]=='-' or a[i]=='*' or a[i]=='/' or a[i]=='%':
            c=a[i]
        else:
            ans=str(ans)+a[i]
    e.delete(0,END)
    e.insert(0,ans)

def click_clear():
    e.delete(0,END)

def click_back():
    ans=e.get()
    a=''
    for i in range(0,len(ans)-1):
        a=a+ans[i]
    e.delete(0,END)
    e.insert(0,a)


button_1=Button(calc,text="1",command=lambda: click("1"),padx=35,pady=25)
button_2=Button(calc,text="2",command=lambda: click("2"),padx=35,pady=25)
button_3=Button(calc,text="3",command=lambda: click("3"),padx=35,pady=25)
button_4=Button(calc,text="4",command=lambda: click("4"),padx=35,pady=25)
button_5=Button(calc,text="5",command=lambda: click("5"),padx=35,pady=25)
button_6=Button(calc,text="6",command=lambda: click("6"),padx=35,pady=25)
button_7=Button(calc,text="7",command=lambda: click("7"),padx=35,pady=25)
button_8=Button(calc,text="8",command=lambda: click("8"),padx=35,pady=25)
button_9=Button(calc,text="9",command=lambda: click("9"),padx=35,pady=25)
button_0=Button(calc,text="0",command=lambda: click("0"),padx=35,pady=25)
button_00=Button(calc,text="00",command=lambda: click("00"),padx=35,pady=25)
button_ans=Button(calc,text="=",command=click_ans,padx=75,pady=25)
button_plus=Button(calc,text="+",command=lambda: click("+"),padx=35,pady=25)
button_sub=Button(calc,text="-",command=lambda: click("-"),padx=35,pady=25)
button_mul=Button(calc,text="*",command=lambda: click("*"),padx=35,pady=25)
button_div=Button(calc,text="/",command=lambda: click("/"),padx=35,pady=25)
button_per=Button(calc,text="%",command=lambda: click("%"),padx=35,pady=25)
button_clear=Button(calc,text="C",command=click_clear,padx=35,pady=25)
button_back=Button(calc,text="<-",command=click_back,padx=35,pady=25)

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)


button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)

button_00.grid(row=5,column=0)
button_0.grid(row=5,column=1)

button_ans.grid(row=5,column=2,columnspan=2)
button_plus.grid(row=4,column=3)
button_sub.grid(row=3,column=3)
button_mul.grid(row=2,column=3)
button_div.grid(row=1,column=3)
button_per.grid(row=1,column=1)


button_clear.grid(row=1,column=0)
button_back.grid(row=1,column=2)


calc.mainloop()

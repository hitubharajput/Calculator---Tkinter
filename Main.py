from tkinter import *
import tkinter.messagebox as box 
from math import *
#-----------------------------------------------------------------------------------------------------------------
screen = Tk()
screen.geometry("450x650")
screen.title("Calculator")
screen.minsize(330,650)
screen.maxsize(330,650)
screen.configure(background="orange")
#-------------------------------------------------------------------------------------------------------------------
def funcuse(event) :
          global calscr
          text  = event.widget.cget("text")
          if text =="About us" :
                  box.showinfo("About us",'''Create By Hitesh Mori\nNirma university,Ahmedabad''')
          elif text =="Feed back" :
                a =  box.askquestion("Feedback","This calculator Good or not")
                if a=="yes" :
                        box.showinfo("Feedback","Thanks for positive feedback")
                elif a=="no" :
                        box.showinfo("Feedback","We will try to improve this calculator")
          elif text =="inverse of sin" :
                   
                   if calscr.get().isdigit() :
                            if int(calscr.get())>1 or int(calscr.get())<-1:
                                    box.showinfo("Domain error","sin function values between -1 and 1")
                            value = int(calscr.get())
                            calscr.set(asin(value)) 
                   else :
                           calscr.set(acos(float(calscr.get())))



          elif text =="inverse of cos" :
                   if calscr.get().isdigit() :
                            if int(calscr.get())>1 or int(calscr.get())<-1 :
                                    box.showinfo("Domain error","cos function values between -1 and 1")
                            value = int(calscr.get())
                            calscr.set(acos(value))
                   else :
                           calscr.set(acos(float(calscr.get())))
          elif text =="inverse of tan" :
                   if calscr.get().isdigit() :
                            value = int(calscr.get())
                            calscr.set(atan(value))   
                   else :
                           calscr.set(atan(float(calscr.get())))
          elif text =="tan" :
                  if calscr.get().isdigit() :
                            value = int(calscr.get())
                            calscr.set(tan(value))   
                  else :
                           calscr.set(tan(float(calscr.get())))
          elif text =="loge" :
                  
                  if calscr.get().isdigit() :
                            if (calscr.get()=='0') :
                                    box.showinfo("error","Math error")
                            value = int(calscr.get())
                            calscr.set(log(value))   
                  else :
                           calscr.set(log(float(calscr.get())))
          elif text =="log2" :
                  if calscr.get().isdigit() :
                            if (calscr.get()=='0') :
                                    box.showinfo("error","Math error")
                            value = int(calscr.get())
                            calscr.set(log2(value))   
                  else :
                           calscr.set(log2(float(calscr.get())))
          elif text =="log10" :
                  if calscr.get().isdigit() :
                            if (calscr.get()=='0') :
                                    box.showinfo("error","Math error")
                            value = int(calscr.get())
                            calscr.set(log10(value))   
                  else :
                           calscr.set(log10(float(calscr.get())))
          elif text =="Deg->Rad" :
                  if calscr.get().isdigit() :
                            value = int(calscr.get())
                            calscr.set(0.0174533*(value))   
                  else :
                           calscr.set(0.0174533*(float(calscr.get())))
          elif text =="Rad->Deg" :
                  if calscr.get().isdigit() :

                            value = int(calscr.get())
                            calscr.set(57.2958*(value))   
                  else :
                           calscr.set(57.2958*(float(calscr.get())))
          elif text =="sin" :
                  if calscr.get().isdigit() :
                            value = int(calscr.get())
                            calscr.set(sin(value))   
                  else :
                           calscr.set(sin(float(calscr.get())))
          elif text =="cos" :
                  if calscr.get().isdigit() :
                            value = int(calscr.get())
                            calscr.set(cos(value))   
                  else :
                           calscr.set(cos(float(calscr.get())))
          elif text =="Antiloge" :
                  if calscr.get().isdigit() :
                            value = int(calscr.get())
                            calscr.set(e**(value))   
                  else :
                           calscr.set(e**(float(calscr.get())))
          elif text =="Antilog10" :
                  if calscr.get().isdigit() :
                            value = int(calscr.get())
                            calscr.set(10**(value))   
                  else :
                           calscr.set(10**(float(calscr.get())))
          elif text =="Square " :
                  if calscr.get().isdigit() :
                            value = int(calscr.get())
                            calscr.set((value**2))   
                  else :
                           calscr.set((float(calscr.get())**2))
          elif text =="Inverse " :
                  if calscr.get().isdigit() :
                            value = int(calscr.get())
                            calscr.set(1/(value))   
                  else :
                           calscr.set((float(1/calscr.get())))
          elif text =="Pi" :
                   calscr.set("3.141592654")
          elif text =="n!" :
                  if calscr.get().isdigit() :
                            value = int(calscr.get())
                            calscr.set(factorial(value))   
                  else :
                          box.showinfo("error","Math error")
                           
          elif text =="e" :
                     calscr.set("2.718281828")
          elif text =="Squareroot" :
                  if calscr.get().isdigit() :
                            value = int(calscr.get())
                            calscr.set(sqrt(value))   
                  else :
                           calscr.set(sqrt(float(calscr.get())))
          
          elif text =="Answer" :
                  if calscr.get().isdigit() :
                            value = int(calscr.get())
                  else :
                          value = eval(calscr.get())
                  calscr.set(value)
          elif text == "Clear" :
                 calscr.set("")
                 ansscr.update()
          else : 
                  calscr.set(calscr.get()+text)
                  ansscr.update()
calscr = StringVar()
calscr.set("")

ansscr = Entry(screen,textvariable=calscr ,bg="white",fg="black",font = "lucida 30 bold",borderwidth=10,relief="sunken",)
ansscr.pack(padx = 23 ,pady =20)

#main frame
mf = Frame(screen,bg = "black")
# 1----------------------------------------------------------------------------
frame1 = Frame(mf,bg="orange")

Buttonp  = Button(frame1,text="Exit",font="lucida 12 bold")
Buttonp.pack(side=LEFT,padx=6,pady=4)
Buttonp.bind('<Button-1>',quit)

Buttonp  = Button(frame1,text="About us",font="lucida 12 bold")
Buttonp.pack(side=LEFT,padx=7,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame1,text="Feed back",font="lucida 12 bold")
Buttonp.pack(side=LEFT,padx=7,pady=4)
Buttonp.bind('<Button-1>',funcuse)

frame1.pack(pady=4)
#2------------------------------------------------------------------------------
frame2 = Frame(mf,bg="orange")

Buttonp  = Button(frame2,text="7",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=3,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame2,text="8",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=6,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame2,text="9",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=8,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame2,text="inverse of sin",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=6,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)
frame2.pack(pady=4)
#3------------------------------------------------------------------------------
frame3 = Frame(mf,bg="orange")

Buttonp  = Button(frame3,text="4",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=3,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame3,text="5",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=6,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame3,text="6",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=8,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame3,text="inverse of cos",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=6,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

frame3.pack(pady=4)
#4-----------------------------------------------------------------------------
frame4 = Frame(mf,bg="orange")

Buttonp  = Button(frame4,text="1",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=3,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame4,text="2",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=6,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame4,text="3",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=8,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame4,text="inverse of tan",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=6,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

frame4.pack(pady=4)
# 5-----------------------------------------------------------------------------
frame5 = Frame(mf,bg="orange")

Buttonp  = Button(frame5,text="tan",font="lucida 12 bold")
Buttonp.pack(side=LEFT ,ipadx=8,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame5,text="loge",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=5,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame5,text="log2",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=5,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame5,text="log10",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=4,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)


frame5.pack(pady=5)
#6---------------------------------------------------------------------------- 
frame6 = Frame(mf,bg="orange")

Buttonp  = Button(frame6,text="Deg->Rad",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=4,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame6,text="Rad->Deg",font="lucida 12 bold")
Buttonp.pack(side=LEFT ,ipadx=4,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame6,text="sin",font="lucida 12 bold")
Buttonp.pack(side=LEFT ,ipadx=4,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

frame6.pack(pady=5)
#7--------------------------------------------------------------------------- 
frame7 = Frame(mf,bg="orange")
Buttonp  = Button(frame7,text="cos",font="lucida 12 bold")
Buttonp.pack(side=LEFT ,ipadx=6,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)
Buttonp  = Button(frame7,text="Antiloge",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=5,padx=5,pady=4)
Buttonp.bind('<Button-1>',funcuse)
Buttonp  = Button(frame7,text="Antilog10",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=5,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

frame7.pack(pady=5)
#8---------------------------------------------------------------------------
frame8 = Frame(mf,bg="orange")
Buttonp  = Button(frame8,text="%",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=5,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)
Buttonp  = Button(frame8,text="Square ",font="lucida 12 bold")
Buttonp.pack(side=LEFT,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)
Buttonp  = Button(frame8,text="Inverse ",font="lucida 12 bold")
Buttonp.pack(side=LEFT,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)
Buttonp  = Button(frame8,text="Pi",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=8,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

frame8.pack(pady=5)
#9------------------------------------------------------------------------------
frame9 = Frame(mf,bg="orange")

Buttonp  = Button(frame9,text="n!",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=5,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame9,text="e",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=5,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame9,text="/",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=3,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame9,text="*",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=3,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame9,text="Squareroot",font="lucida 12 bold")
Buttonp.pack(side=LEFT,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

frame9.pack(pady=5)
#10------------------------------------------------------------------------
frame10 = Frame(mf,bg="orange")

Buttonp  = Button(frame10,text="0",font="lucida 12 bold")
Buttonp.pack(side=LEFT,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame10,text=".",font="lucida 12 bold")
Buttonp.pack(side=LEFT,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame10,text="-",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=2,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame10,text="+",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=2,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame10,text="Clear",font="lucida 12 bold")
Buttonp.pack(side=LEFT,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

Buttonp  = Button(frame10,text="Answer",font="lucida 12 bold")
Buttonp.pack(side=LEFT,ipadx=2,padx=4,pady=4)
Buttonp.bind('<Button-1>',funcuse)

frame10.pack(pady=  5)









mf.pack(padx =10 ,pady=5)


screen.mainloop()
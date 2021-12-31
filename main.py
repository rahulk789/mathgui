import matplotlib
from matplotlib import pyplot as po
matplotlib.use("TkAgg")
import math as mt
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg , NavigationToolbar2Tk
a=[]
LARGE_FONT=("Verdana",12)
class abcd(tk.Tk):
             def __init__(self,*args,**kwargs):
                            tk.Tk.__init__(self,*args,**kwargs)
                            tk.Tk.iconbitmap(self)
                            tk.Tk.wm_title(self,"Graph Plotter")
                            tk.Tk.configure(self,background="grey")
                            container=tk.Frame(self)
                            container.pack(side="top",fill="both",expand=True)
                            container.grid_rowconfigure(0,weight=1)
                            container.grid_columnconfigure(0,weight=1)
                            self.frames ={}
                            for F in (startpage,pagesin,pagecos,pagetan,pagecot,pagecosec,pagesec,pagelog):
                                         frame=F(container,self)
                                         self.frames[F] =frame
                                         frame.grid(row=0,column=0,sticky="nsew")
                            self.show_frame(startpage)
             def show_frame(self,cont):
                          frame=self.frames[cont]
                          frame.tkraise()
class startpage(tk.Frame):
                 def __init__(self,parent, controller):
                   tk.Frame.__init__(self,parent)
                   label =tk.Label(self,text="Graph Page!", font=LARGE_FONT)
                   tk.Tk.configure(self,background="blue")
                   label.pack(pady=10,padx=10)
                   button1 = ttk.Button(self, text="SIN(X)", command= lambda: controller.show_frame(pagesin))
                   button1.pack()
                   button2 = ttk.Button(self, text="C0SINE(X)", command= lambda: controller.show_frame(pagecos))
                   button2.pack()
                   button3 = ttk.Button(self, text="TANGENT(X)", command=lambda: controller.show_frame(pagetan))
                   button3.pack()
                   button4 = ttk.Button(self, text="COT(X)", command= lambda: controller.show_frame(pagecot))
                   button4.pack()                  
                   button5 = ttk.Button(self, text="SEC(X)", command= lambda: controller.show_frame(pagesec))
                   button5.pack()
                   button6 = ttk.Button(self, text="COSEC(X)", command=lambda: controller.show_frame(pagecosec))
                   button6.pack()
                   button7 = ttk.Button(self, text="LOG(X)", command=lambda: controller.show_frame(pagelog))
                   button7.pack()
                      
class pagesin(tk.Frame):
                 def __init__(self,parent, controller):
                   tk.Frame.__init__(self,parent)
                   label =tk.Label(self,text="Graph Page!", font=LARGE_FONT)
                   label.pack(pady=10,padx=10)
                   button1 = ttk.Button(self, text="SINE(X)", command=lambda: controller.show_frame(pagesin))
                   button1.pack()
                   button2= ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(startpage))
                   button2.pack()    
                   f = Figure (figsize=(5,5),  dpi=100)
                   x = f.add_subplot(111)
                   inputfunc=tk.Entry(self,text="sin(")
                   l=(np.arange(-30,30,0.01))
                   # a=np.array(l)
                   a=[]
                   for i in list(l):
                          m=mt.sin(i)
                          a.append(m)
                   #WRITING Y VALUES OF FUNCTION INTO YVALUES.TXT 
                   F=open("YVALUES.txt","+a")
                   F.write("\nSIN VALUES\n")
                   F.writelines(str(a))
                   F.close()
                   x.plot((np.arange(-30,30,0.01)),a,color="r",linewidth="3",linestyle="solid",label="graph 1")
                   x.plot([-30,30],[0,0],color="k",linewidth="3",linestyle="solid")
                   x.plot([0,0],[-3,3],color="k",linewidth="3",linestyle="solid")
                   x.plot([-30],[0],"k",marker="<")
                   x.plot([30],[0],"k",marker=">")
                   x.plot([0],[3],"k",marker="^")
                   x.plot([0],[-3],"k",marker="v")
                   canvas  = FigureCanvasTkAgg(f, self)
                   canvas.draw()
                   canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                   toolbar = NavigationToolbar2Tk(canvas, self)
                   toolbar.update()
                   canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
class pagecos(tk.Frame):
                 def __init__(self,parent, controller):
                   tk.Frame.__init__(self,parent)
                   label =tk.Label(self,text="Graph Page!", font=LARGE_FONT)
                   label.pack(pady=10,padx=10)
                   button1 = ttk.Button(self, text="COSINE(X)", command=lambda: controller.show_frame(pagecos))
                   button1.pack()
                   button2= ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(startpage))
                   button2.pack()
                   f = Figure (figsize=(5,5),  dpi=100)
                   x = f.add_subplot(111)
                   inputfunc=tk.Entry(self,text="sin(")
                   l=(np.arange(-30,30,0.01))
                   # a=np.array(l)
                   a=[]
                   for i in list(l):
                          m=mt.cos(i)
                          a.append(m)
                   #WRITING Y VALUES OF FUNCTION INTO YVALUES.TXT
                   F=open("YVALUES.txt","+a")
                   F.write("\nCOS VALUES\n")
                   F.writelines(str(a))
                   F.close()
                   x.plot((np.arange(-30,30,0.01)),a,color="r",linewidth="3",linestyle="solid",label="graph 1")
                   x.plot([-30,30],[0,0],color="k",linewidth="3",linestyle="solid")
                   x.plot([0,0],[-3,3],color="k",linewidth="3",linestyle="solid")
                   x.plot([-30],[0],"k",marker="<")
                   x.plot([30],[0],"k",marker=">")
                   x.plot([0],[3],"k",marker="^")
                   x.plot([0],[-3],"k",marker="v")
                   canvas  = FigureCanvasTkAgg(f, self)
                   canvas.draw()
                   canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                   toolbar = NavigationToolbar2Tk(canvas, self)
                   toolbar.update()
                   canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
class pagetan(tk.Frame):
                 def __init__(self,parent, controller):
                   tk.Frame.__init__(self,parent)
                   label =tk.Label(self,text="Graph Page!", font=LARGE_FONT)
                   label.pack(pady=10,padx=10)
                   button1 = ttk.Button(self, text="TANGENT(X)", command=lambda: controller.show_frame(pagetan))
                   button1.pack()
                   button2= ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(startpage))
                   button2.pack()
                   f = Figure (figsize=(5,5),  dpi=100)
                   x = f.add_subplot(111)
                   l=(np.arange(-30,30,0.01))
             # a=np.array(l)
                   a=[]
                   for i in list(l):
                     if mt.tan(i)<20 and mt.tan(i)>-20:
                           m=mt.tan(i)
                           a.append(m)
                     else:
                                       m=20
                                       a.append(m)
                   #WRITING Y VALUES OF FUNCTION INTO YVALUES.TXT
                   F=open("YVALUES.txt","+a")
                   F.write("\nTAN VALUES\n")
                   F.writelines(str(a))
                   F.close()
                   x.plot((np.arange(-30,30,0.01)),a,color="r",linewidth="3",linestyle="solid",label="graph 1")
                   x.plot([-30,30],[0,0],color="k",linewidth="3",linestyle="solid")
                   x.plot([0,0],[-28,28],color="k",linewidth="3",linestyle="solid")
                   x.plot([-30],[0],"k",marker="<")
                   x.plot([30],[0],"k",marker=">")
                   x.plot([0],[28],"k",marker="^")
                   x.plot([0],[-28],"k",marker="v")
                   canvas  = FigureCanvasTkAgg(f, self)
                   canvas.draw()
                   canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                   toolbar = NavigationToolbar2Tk(canvas, self)
                   toolbar.update()
                   canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
class pagecot(tk.Frame):
                 def __init__(self,parent, controller):
                   tk.Frame.__init__(self,parent)
                   label =tk.Label(self,text="Graph Page!", font=LARGE_FONT)
                   label.pack(pady=10,padx=10)
                   button1 = ttk.Button(self, text="COTANGENT(X)", command=lambda: controller.show_frame(pagecot))
                   button1.pack()
                   button2= ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(startpage))
                   button2.pack()
                   f = Figure (figsize=(5,5),  dpi=100)
                   x = f.add_subplot(111)
                   l=(np.arange(-30,30,0.01))
                   l=(np.arange(-30,30,0.01))
             # a=np.array(l)
                   a=[]
                   for i in list(l):
                     if mt.tan(i)>0.2 or mt.tan(i)<-0.2:
                           m=1/mt.tan(i)
                           a.append(m)
                     else:
                                       m=5
                                       a.append(m)
                   #WRITING Y VALUES OF FUNCTION INTO YVALUES.TXT
                   F=open("YVALUES.txt","+a")
                   F.write("\nCOT VALUES\n")
                   F.writelines(str(a))
                   F.close()
                   x.plot((np.arange(-30,30,0.01)),a,color="r",linewidth="3",linestyle="solid",label="graph 1")
                   x.plot([-30,30],[0,0],color="k",linewidth="3",linestyle="solid")
                   x.plot([0,0],[-3,3],color="k",linewidth="3",linestyle="solid")
                   x.plot([-30],[0],"k",marker="<")
                   x.plot([30],[0],"k",marker=">")
                   x.plot([0],[3],"k",marker="^")
                   x.plot([0],[-3],"k",marker="v")
                   canvas  = FigureCanvasTkAgg(f, self)
                   canvas.draw()
                   canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                   toolbar = NavigationToolbar2Tk(canvas, self)
                   toolbar.update()
                   canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
class pagesec(tk.Frame):
                 def __init__(self,parent, controller):
                   tk.Frame.__init__(self,parent)
                   label =tk.Label(self,text="Graph Page!", font=LARGE_FONT)
                   label.pack(pady=10,padx=10)
                   button1 = ttk.Button(self, text="SECANT(X)", command=lambda: controller.show_frame(pagesec))
                   button1.pack()
                   button2= ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(startpage))
                   button2.pack()
                   f = Figure (figsize=(5,5),  dpi=100)
                   x = f.add_subplot(111)
                   inputfunc=tk.Entry(self,text="sin(")
                   l=(np.arange(-20,20,0.01))
                   # a=np.array(l)
                   a=[]
                   for i in list(l):
                          if mt.cos(i)>0.2 or mt.cos(i)<-0.2:
                           m=1/mt.cos(i)
                           a.append(m)
                          else :
                                       m=5
                                       a.append(m)
                   #WRITING Y VALUES OF FUNCTION INTO YVALUES.TXT
                   F=open("YVALUES.txt","+a")
                   F.write("\nSEC VALUES\n")
                   F.writelines(str(a))
                   F.close()
                   x.plot((np.arange(-20,20,0.01)),a,color="r",linewidth="3",linestyle="solid",label="graph 1")
                   x.plot([-30,30],[0,0],color="k",linewidth="3",linestyle="solid")
                   x.plot([0,0],[-3,3],color="k",linewidth="3",linestyle="solid")
                   x.plot([-30],[0],"k",marker="<")
                   x.plot([30],[0],"k",marker=">")
                   x.plot([0],[3],"k",marker="^")
                   x.plot([0],[-3],"k",marker="v")
                   canvas  = FigureCanvasTkAgg(f, self)
                   canvas.draw()
                   canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                   toolbar = NavigationToolbar2Tk(canvas, self)
                   toolbar.update()
                   canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
class pagecosec(tk.Frame):
                 def __init__(self,parent, controller):
                   tk.Frame.__init__(self,parent)
                   label =tk.Label(self,text="Graph Page!", font=LARGE_FONT)
                   label.pack(pady=10,padx=10)
                   button1 = ttk.Button(self, text="COSECANT(X)", command=lambda: controller.show_frame(pagecosec))
                   button1.pack()
                   button2= ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(startpage))
                   button2.pack()
                   f = Figure (figsize=(25,5),  dpi=100)
                   x = f.add_subplot(111)
                   l=(np.arange(-30,30,0.01))
            # a=np.array(l)
                   a=[]
                   for i in list(l):
                          if mt.sin(i)>0.2 or mt.sin(i)<-0.2:
                           m=1/mt.sin(i)
                           a.append(m)
                          else :
                                       m=5
                                       a.append(m)
                   #WRITING Y VALUES OF FUNCTION INTO YVALUES.TXT
                   F=open("YVALUES.txt","+a")
                   F.write("\nCOSEC VALUES\n")
                   F.writelines(str(a))
                   F.close()
                   x.plot((np.arange(-30,30,0.01)),a,color="r",linewidth="3",linestyle="solid",label="graph 1")
                   x.plot([-30,30],[0,0],color="k",linewidth="3",linestyle="solid")
                   x.plot([0,0],[-3,3],color="k",linewidth="3",linestyle="solid")
                   x.plot([-20],[0],"k",marker="<")
                   x.plot([20],[0],"k",marker=">")
                   x.plot([0],[3],"k",marker="^")
                   x.plot([0],[-3],"k",marker="v")
                   canvas  = FigureCanvasTkAgg(f, self)
                   canvas.draw()
                   canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                   toolbar = NavigationToolbar2Tk(canvas, self)
                   toolbar.update()
                   canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
class pagelog(tk.Frame):
                 def __init__(self,parent, controller):
                   tk.Frame.__init__(self,parent)
                   label =tk.Label(self,text="Graph Page!", font=LARGE_FONT)
                   label.pack(pady=10,padx=10)
                   button1 = ttk.Button(self, text="LOG(X)", command=lambda: controller.show_frame(pagelog))
                   button1.pack()
                   button2= ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(startpage))
                   button2.pack()
                   f = Figure (figsize=(5,5),  dpi=100)
                   x = f.add_subplot(111)
                   l=(np.arange(0,30,0.01))
                   a=[]
                   for i in list(l):
                          if i!=0:
                           m=mt.log(i)
                           a.append(m)
                          if i==0:
                           m=mt.log(0.01)
                           a.append(m)
                   #WRITING Y VALUES OF FUNCTION INTO YVALUES.TXT
                   F=open("YVALUES.txt","+a")
                   F.write("\nLOG VALUES\n")
                   F.writelines(str(a))
                   F.close()
                   x.plot((np.arange(0,30,0.01)),a,color="r",linewidth="3",linestyle="solid",label="graph 1")
                   x.plot([-30,30],[0,0],color="k",linewidth="3",linestyle="solid")
                   x.plot([0,0],[-10,10],color="k",linewidth="3",linestyle="solid")
                   x.plot([-30],[0],"k",marker="<")
                   x.plot([30],[0],"k",marker=">")
                   x.plot([0],[10],"k",marker="^")
                   x.plot([0],[-10],"k",marker="v")
                   canvas  = FigureCanvasTkAgg(f, self)
                   canvas.draw()
                   canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                   toolbar = NavigationToolbar2Tk(canvas, self)
                   toolbar.update()
                   canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)



'''#MYSQL CONNECTIVITY
import mysql.connector as mysqlc
mydb=mysqlc.connect(host='localhost',user='root',passwd='user123',database='grade11')
mycursor=mydb.cursor()
mycursor.execute("Drop table trignometry")
mycursor.execute('create table trignometry (func char(10), domain varchar(50), rane char(50));')
#mycursor.execute("Drop table trignometry")
sql='insert into trignometry (func,domain,rane) values (%s,%s,%s)'
val=[
    ('sin','R','[-1,1]'),
    ('cos','R','[-1,1]'),
    ('tan','R-((2n+1))pi/2','R'),
    ('cot','R-(n)pi','R'),
    ('sec','R-((2n+1))pi/2','(-INF,-1] U [1,INF)'),
    ('cosec','R-(n)pi','(-INF,-1] U [1,INF)')
    ]
mycursor.executemany(sql,val)
def product():
    mycursor.execute('select domain,rane from trignometry where func="sin";')
    myresult=mycursor.fetchall()
    for x in myresult:
        l3["text"]=x
def addition():
    mycursor.execute('select domain,rane from trignometry where func="cos";')
    myresult=mycursor.fetchall()
    for x in myresult:
        l3["text"]=x

def subtraction():
    mycursor.execute('select domain,rane from trignometry where func="tan";')
    myresult=mycursor.fetchall()
    for x in myresult:
        l3["text"]=x

def division():
    mycursor.execute('select domain,rane from trignometry where func="cot";')
    myresult=mycursor.fetchall()
    for x in myresult:
        l3["text"]=x

def sec():
    mycursor.execute('select domain,rane from trignometry where func="sec";')
    myresult=mycursor.fetchall()
    for x in myresult:
        l3["text"]=x

def cosec():
    mycursor.execute('select domain,rane from trignometry where func="cosec";')
    myresult=mycursor.fetchall()
    for x in myresult:
        l3["text"]=x

top=tk.Tk()
top.title("domain and range of functions")
l1=tk.Label(top,fg="blue",text="Please enter the button")
l2=tk.Label(top,fg="blue",text="the output displayed is domain,range")

b1=tk.Button(top,text="sin",command=product)
b2=tk.Button(top,text="cos",command=addition)
b3=tk.Button(top,text="tan",command=subtraction)
b4=tk.Button(top,text="cot",command=division)
b5=tk.Button(top,text="sec",command=sec)
b6=tk.Button(top,text="cosec",command=cosec)
l3=tk.Label(top,fg="black")
l1.pack()
l2.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
l3.pack()
top.mainloop()
'''
#QUADRATIC ROOTS
import tkinter as tk
import math
def product():
    n1=int(e1.get())
    n2=int(e2.get())
    n3=int(e3.get())
    d=((n2**2)-(4*n1*n3))
    D=d**0.5
    x1=((-n2+D)/(2*n1))
    x2=((-n2-D)/(2*n1))
    display_str=str(float(x1))
    display_str1=str(float(x2))
    l6["text"]=display_str
    l5["text"]=display_str1

top=tk.Tk()
top.title("roots of equation")
l1=tk.Label(top,fg="blue",text="Please enter numbers in order of")
l2=tk.Label(top,fg="blue",text="coefficient of x^2")
l3=tk.Label(top,fg="blue",text="coefficient of x")
l4=tk.Label(top,fg="blue",text="coefficient of constant term")
e1=tk.Entry(top,fg="red")
e2=tk.Entry(top,fg="red")
e3=tk.Entry(top,fg="red")
b1=tk.Button(top,text="press button",command=product)
l6=tk.Label(top,fg="black")
l5=tk.Label(top,fg="black")
l1.pack()
l2.pack()
l3.pack()
l4.pack()
l5.pack()
l6.pack()
e1.pack()
e2.pack()
e3.pack()
b1.pack()
top.mainloop()


app=abcd()
app.mainloop()

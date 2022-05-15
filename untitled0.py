
from numpy import (sin, cos, tan, pi, exp, sqrt, arange, meshgrid, linspace)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import (clf, gcf, subplots_adjust, figure, show)
from tkinter.ttk import (Combobox, Button, Style, Scale)
from tkinter import (Label, Entry, Tk, S, N, E, W, SE, SW, NE, NW)
from sys import exit
import os
from tkinter import *



def onScale(tim):
    global time
    time = int(float(tim))
    time_label.configure(text=time)
    plotting()

def testVal(inStr, acttyp):
    if acttyp == '1':
        if not inStr.isdigit():
            return False
    return True

def EXIT():
    os.abort()

def get(entry):
    value = entry.get()
    try:
        return int(value)
    except ValueError:
        return None
 
h = 0.01

class TE():
    def Ex(x, y, z, kappaX, kappaY, kappa, w, hh, t):
        return ((-w*(kappaY/kappa**2)) * cos(kappaX * x) * sin(kappaY * y)*sin(w*t-h*z))#==0 if kappaY==0

    def Ey(x, y, z, kappaX, kappaY, kappa, w, hh, t):
        return ((w*kappaX/kappa**2) * sin((kappaX * x)) * cos(kappaY * y)*sin(w*t-h*z))#==0 if kappaX==0

    def Ez(x, y, z, kappaX, kappaY, kappa, w, hh, t):
        return 0
    
    def Hx(x, y, z, kappaX, kappaY, kappa, w, hh, t):
        return (-hh*kappaX/kappa**2) * sin(((kappaX * x)) * cos(kappaY * y)*sin(w*t-h*z))

    def Hy (x, y, z, kappaX, kappaY, kappa, w, hh, t):
        return ((-hh*kappaX/kappa**2) * cos((kappaX * x)) * sin(kappaY * y)*sin(w*t-h*z))
    
    def Hz(x, y, z, kappaX, kappaY, kappa, w, hh, t):
        return (cos((kappaX * x)) * cos(kappaY * y)*cos(w*t-h*z))
 #=====================================================================================================================   
   
    def Hy01(x, y, z, kappaX, kappaY, kappa, w, hh, t):
        return ((-hh*kappaY/kappa**2) * sin(kappaY * y)*sin(w*t-h*z))    
    def Ex01(x, y, z, kappaY, c, w, hh, t):
        return ((((-w*pi)/(c*kappaY)) * sin(kappaY * y)*sin(w*t-h*z)))
    def Ey01(x, y, z, kappaX, kappaY, kappa, w, hh, t):
        return 0

class TM():
    def Ex(x, y, z, kappaX, kappaY, kappa, w, hh, t):
        return (hh*((kappaX * x) /kappa**2) * cos((kappaX * x)) * sin(kappaY * y)*sin(w*t-h*z))

    def Ey(x, y, z, kappaX, kappaY, kappa, w, hh, t):
        return ((hh*kappaX/kappa**2) * sin((kappaX * x)) * cos(kappaY * y)*sin(w*t-h*z))

    def Ez(x, y, z, kappaX, kappaY, kappa, w, hh, t):
        return (sin((kappaX * x)) * sin(kappaY * y)*cos(w*t-h*z))
    
    def Hx(x, y, z, kappaX, kappaY, kappa, w, hh, t):
        return ((-w*kappaX/kappa**2) * sin((kappaX * x)) * cos(kappaY * y)*sin(w*t-h*z))

    def Hy(x, y, z, kappaX, kappaY, kappa, w, hh, t):
        return ((w*kappaX/kappa**2) * cos((kappaX * x)) * sin(kappaY * y)*sin(w*t-h*z))

    def Hz(x, y, z, kappaX, kappaY, kappa, w, hh, t):
        return 0

def plotting():
    global size_lines_entry
    global frequincy
    global moda_n
    global moda_m
    global label
    global f_kr
    clf()
    if (len(frequincy.get()) == 0) or (len(a_x_size_entry.get()) == 0) or (len(b_x_size_entry.get()) == 0) or (
            len(table_n.get()) == 0) or (len(table_m.get()) == 0):
        clf()
        label.configure(text="Заполните поля!", bg="DarkOrange3", fg="black")
        label.place(x=25,y=600)
        gcf().canvas.draw()
        return
    label.configure(text=" ")

    cc = 3e10
    ff = get(frequincy)
    f = ff * 1e9
    w = 2 * pi * f
    lyam = cc / f
    hh = w / cc
    n = get(table_n)
    m = get(table_m)
    a = get(a_x_size_entry)
    b = get(b_x_size_entry)
    tt = time
    t = tt / 1e12
    c = lyam
    k = get(size_lines_entry)
    kappa = sqrt(((pi * n / a) ** 2) + ((pi * m / b) ** 2))
    kappaX = pi * n / a
    kappaY = pi * m / b
    f_kr = (cc * kappa) / (2 * pi)
    lyam_kr = cc / f_kr

    def V_gr():
        return cc * sqrt(1 - pow(lyam / lyam_kr, 2))

    C1 = 0
    C2 = 0
    if n != 0 and m == 0:
        if (n % 2) != 0:
            C1 = a / 2
        else:
            C1 = a / (2 * n)
    elif n == 0 and m != 0:
        if (m % 2) != 0:
            C2 = b / 2
        else:
            C2 = b / (2 * m)

    # êîíåö
    # TE H
    def TE_H_XY(x, y):
        return ((abs(sin(kappaX * x))) / (abs(sin(kappaY * y)))) * cos(w * t + pi / 2)

    def TE_H_YZ(y, z):
        return (abs(sin(kappaY * y))) * cos(w * t - hh * z + pi / 2)

    def TE_H_XZ(x, z):
        return (abs(sin(kappaX * x))) * cos(w * t - hh * z + pi / 2)

    # E
    def TE_E_XY(x, y):
        return abs(cos(kappaY * y)) * abs(cos(kappaX * x)) * cos(w * t)

    # TE10
    # ==========================================================================================================
    def TE10_H_XY(x, y):
        return abs(sin(kappaX * x)) * exp(hh * tan(w * t) * y*2)
        
    def TE10_H_XZ(x, z):
        return abs(sin(kappaX * x)) * cos(w * t*2.3 - hh * z)

    def TE10_H_YZ(y, z):
        return exp(kappaX * (cos(kappaX * C1) / sin(kappaX * C1)) * y) * sin(w * t - hh * z)

    def TE10_E_XY(x, y):
        return (w/(kappaX*cc)) * abs(cos(kappaX*x)) * sin(w*t)

    def TE10_E_YZ_pos(y, z):
        return -(w / (kappaX * cc))*abs((sin(w * t - hh * y/2-8.55)))

    def TE10_E_YZ_neg(y, z):
       return (w / (kappaX * cc))*abs((sin(w * t - hh * y/2-22.8)))
    
    # ==========================================================================================================

    # TE01
    def TE01_H_XY(x, y):
        return abs(sin(kappaY * y)) * exp(hh * tan(w * t) * x)

    def TE01_H_XZ(x, z):
        return exp(kappaY * (cos(kappaY * C2) / sin(kappaY * C2)) * x) * cos(w * t - hh * z)

    def TE01_H_YZ(y, z):
        return abs(sin(kappaY * y)) * cos(w * t - hh * z)

    def TE01_E_XY(x, y):
        return (w / (kappaY * cc)) * abs(sin(kappaY * y) * cos(kappaY * y) * sin(kappaY * y))

    def TE01_E_XZ(x, z):
        return cos(w * t - hh * x)

    # TM H
    def TM_H_XY(x, y):
        return abs(sin(kappaX * x)) * abs(sin(kappaY * y)) * cos(w * t + pi / 2)

    # TM E
    def TM_E_XY(x, y):
        return (kappaX/kappaY)*(tan(kappaX * x)) * (1/tan(cos(kappaY * y))) * cos(w * t)
        

    def TM_E_XZ(x, z):
        return (abs(cos(kappaX * x))) * cos(w * t - hh * z)

    def TM_E_YZ(y, z):
        return (abs(cos(kappaY * y))) * cos(w * t*2 - hh * z+0.5)  
    

    def makeData(b1, b2):
        a1 = arange(0, b1, h)
        a2 = arange(0, b2, h)
        a1grid, a2grid = meshgrid(a1, a2)
        return a1grid, a2grid

    if f > f_kr:
        fig = figure(figsize=(9, 6), facecolor="#4e4e52", edgecolor="white")
        fig.set_figheight(10)
        fig.set_figwidth(6)
        XY = fig.add_subplot(3, 1, 1)
        YZ = fig.add_subplot(3, 1, 2)
        XZ = fig.add_subplot(3, 1, 3)

        x1, y1 = makeData(a, b)
        y2, z2 = makeData(b, c)
        x3, z3 = makeData(a, c)
        x=arange(0., a+h, h)      #
        y=arange(0., b+h, h)
        z = arange(0., 2*c+h, h)
        x, y, z = meshgrid(x, y, z)
        
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().place(relx=.7, rely=.53, anchor="c")

        if combobox.get() == "TE":
            if n != 0 and m != 0:
                XY.contour(x1, y1, TE_H_XY(x1, y1), linspace(-1, 1, k), colors='b')
            elif n != 0 and m == 0:
                XY.contour(x1, y1, TE10_H_XY(y1, 0), linspace(-1, 1, k), colors='b')
            elif n == 0 and m != 0:
       
                YZEx=TE.Ex01(x=x[0][1], y=y[:,1,:], z=z[:,1,:], kappaY=kappaY, c=c, w=w, hh=hh, t=t)
                YZEy=TE.Ey01(x=x[0][1], y=y[:,1,:], z=z[:,1,:], kappaX=kappaX, kappaY=kappaY, kappa=kappa, w=w, hh=hh, t=t)
                YZ.set_ylim(0,b+h)
                
                for i in range(0,len(y[:,0,0])-1,4):
                    for j in range(0,len(z[0,0,:]),5) :
                        if TE.Ex01(x=x[0,1,0], y=y[i,0,0], z=z[0,0,j], kappaY=kappaY, c=c, w=w, hh=hh, t=t)>0:
                            mark="o"
                        else:
                               mark="x"
                               s = 0.8*(abs(TE.Ex01(x=x[0,1,0], y=y[i,0,0], z=z[0,0,j], kappaY=kappaY, c=c, w=w, hh=hh, t=t)) / abs(YZEx).max())
                               YZ.scatter(z[0,0,j], y[i,0,0], s=s, c="r", marker=mark)
                 
                YZ.set_xlabel('Z')
                YZ.set_ylabel('У')
                
                YZHy=TE.Hy01(x=x[0][1], y=y[:,1,:], z=z[:,1,:], kappaX=kappaX, kappaY=kappaY, kappa=kappa, w=w, hh=hh, t=t)
                YZHz=TE.Hz(x=x[0][1], y=y[:,1,:], z=z[:,1,:], kappaX=kappaX, kappaY=kappaY, kappa=kappa, w=w, hh=hh, t=t)                

                XYEx=TE.Ex01(x=x[:,:,0], y=y[:,:,0], z=z[0][0][1], kappaY=kappaY, c=c, w=w, hh=hh, t=t)
                XYEy=TE.Ey(x=x[:,:,0], y=y[:,:,0], z=z[0][0][1], kappaX=kappaX, kappaY=kappaY, kappa=kappa, w=w, hh=hh, t=t)

                XYHx=TE.Hx(x=x[:,:,0], y=y[:,:,0], z=z[0][0][1], kappaX=kappaX, kappaY=kappaY, kappa=kappa, w=w, hh=hh, t=t)
                XYHy=TE.Hy01(x=x[:,:,0], y=y[:,:,0], z=z[0][0][1], kappaX=kappaX, kappaY=kappaY, kappa=kappa, w=w, hh=hh, t=t)

                XZEx=TE.Ex01(x=x[1,:,:], y=y[1,0,0], z=z[1,:,:], kappaY=kappaY, c=c, w=w, hh=hh, t=t)
                XZEz=0*XZEx
                XZ.set_ylim(0,a+h)

                lwxze=(XZEx**2+XZEz**2)**0.5/(abs(XZEx).max()**2+abs(XZEz).max()**2)**0.5                    
                XZ.streamplot(z[0,:,:],x[0,:,:],XZEz,XZEx,linewidth=lwxze)

                XZ.set_xlabel('Z')
                XZ.set_ylabel('X')

                lwxye=(XYEx**2+XYEy**2)**0.5/abs(XYEx).max()
                XY.streamplot(x[:,:,0],y[:,:,0],XYEx,XYEy,linewidth=lwxye)
                XY.set_xlabel('Х')
                XY.set_ylabel('У')
                
                lwxyh=((XYHx**2+XYHy**2)**0.5)/(abs(XYHy).max())
                print(XYHx)
                print(XYHy)
                XY.streamplot(x[:,:,0], y[:,:,0], XYHx, XYHy, linewidth=lwxyh)
                XY.set_xlabel('Х')
                XY.set_ylabel('У')
                
                YZ.streamplot(z[:,1,:],y[:,1,:],YZHz,YZHy,linewidth=1)
                YZ.set_xlabel('Z')
                YZ.set_ylabel('У')
                
            
            elif m==0 and n==0:
                raise Exception("m не может быть равным 0  одновременно с n равным 0")
            XY.set_xlabel('x')
            XY.set_ylabel('y')

            if n != 0 and m != 0:
                XY.contour(x1, y1, TE_E_XY(x1, y1), linspace(-1, 1, k), colors='r')
            elif n != 0 and m == 0:
                XY.contour(x1, y1, TE10_E_XY(x1, y1), linspace(-1, 2, k), colors='r')

            XY.set_xlabel('x')
            XY.set_ylabel('y')

            if n != 0 and m != 0:
                YZ.contour(z2, y2, TE_H_YZ(y2, z2), linspace(-1, 1, k), colors='b')
            elif n != 0 and m == 0:
                YZ.contour(z2, y2, TE10_H_XY(y2, 0), linspace(-1, 1, k), colors='b') #TE10_H_XY_neg(y1, 0)
                YZ.contour(z2, y2, TE10_E_YZ_pos(z2, y2), linspace(-1, 1, k), colors='r')
                YZ.contour(z2, y2, TE10_E_YZ_neg(z2, y2), linspace(-1, 1, k), colors='r')
                

            YZ.set_xlabel('z')
            YZ.set_ylabel('y')

            if n != 0 and m != 0:
                XZ.contour(z3, x3, TE_H_XZ(x3, z3), linspace(-1, 1, k), colors='b')
            elif n != 0 and m == 0:
                XZ.contour(z3, x3, TE10_H_XZ(x3, z3), linspace(-1, 1, k), colors='b')

            XZ.set_xlabel('z')
            XZ.set_ylabel('x')


        else:
            if n != 0 and m != 0:
                XY.contour(x1, y1, TM_H_XY(x1, y1), linspace(-1, 1, k), colors='b')
                XY.set_xlabel('x')
                XY.set_ylabel('y')
             
                XYEx=TM.Ex(x=x[:,:,0], y=y[:,:,0], z=z[0][0][1], kappaX=kappaX, kappaY=kappaY, kappa=kappa, w=w, hh=hh, t=t)
                XYEy=TM.Ey(x=x[:,:,0], y=y[:,:,0], z=z[0][0][1], kappaX=kappaX, kappaY=kappaY, kappa=kappa, w=w, hh=hh, t=t)
                lwxye=(XYEx**2+XYEy**2)**0.5/(abs(XYEx).max()**2+abs(XYEy).max()**2)**0.5
                XY.streamplot(x[:,:,0],y[:,:,0],XYEx,XYEy, linewidth=lwxye, color='r')                
                XY.set_xlabel('x')
                XY.set_ylabel('y')

                YZ.contour(z2, y2, TM_E_YZ(y2, z2), linspace(-1, 1, k), colors='r')
                YZ.contour(z2, y2, (-1)*TE10_E_YZ_neg(z2, y2), linspace(-1, 1, k), colors='b')
                YZ.contour(z2, y2, (-1)*TE10_E_YZ_pos(z2, y2), linspace(-1, 1, k), colors='b')
                YZ.set_xlabel('z')
                YZ.set_ylabel('y')

                
                XZ.contour(z3, x3, TE10_E_YZ_pos(z3, x3), linspace(-1, 1, k), colors='b')
                XZ.contour(z3, x3, TE10_E_YZ_neg(z3, x3), linspace(-1, 1, k), colors='b')
                XZ.set_xlabel('z')
                XZ.set_ylabel('x')
            else:
                label = Label(window, text="Не распространяется!!!", font= ("rany",16), bg="DarkOrange3", fg="black")
                label.place(x=25,y=600)
                gcf().canvas.draw()


    else:
        label = Label(window, text="Частота ниже критической!", font= ("rany",16), bg="DarkOrange3", fg="black")
        label.place(x=25,y=600)
    subplots_adjust(wspace=0.5, hspace=0.5)
    gcf().canvas.draw()
    w_label = Label(window, text="Критическая частота(ГГц): ", font= ("rany",16), bg="DarkOrange3", fg="black")
    w_label.place(x=25,y=550)
    wk_label = Label(window, text=f_kr / 1e9, font= ("rany",16), bg="DarkOrange3", fg="black")
    wk_label.place(x=300,y=550)


window = Tk()
window.title("Volnovod")
window.protocol("WM_DELETE", EXIT)
window.attributes("-alpha", 1)
window.state("normal")
window.resizable(width=True, height=True)
window['bg'] = 'DarkOrange3'
window.geometry('1200x600')




label_n = Label(window, text="Выберите тип волны:", font= ("rany",16), bg="DarkOrange3", fg="black")
label_n.place(x=25,y=25)

style = Style()
style.configure("BW.TLabel", font=("rany",16), foreground="black", background="DarkOrange3")
combobox = Combobox(value=["TE", "TM"], height=2, width=3, state="readonly", font=("rany",16), style="BW.TLabel")
combobox.set("TE")
combobox.place(x=400,y=25)
window.option_add("*TCombobox*Listbox*Background", 'DarkOrange3')
window.option_add("*TCombobox*Listbox*Foreground", 'black')

moda_label = Label(window, text="Выберите моду:", font=("rany",16), bg="DarkOrange3", fg="black")
moda_label.place(x=25,y=75)

label_m = Label(window, text="m: ", font=("rany",16), bg="DarkOrange3", fg="black")
label_m.place(x=375,y=125)
table_m = Entry(window, width=5, bg="DarkOrange3", selectbackground='DarkOrange3', font=("rany",16), fg="black", validate="key")
table_m['validatecommand'] = (table_m.register(testVal), '%P', '%d')
table_m.place(x=400,y=125)

label_n = Label(window, text="n: ", font=("rany",16), bg="DarkOrange3", fg="black")
label_n.place(x=375,y=75)
table_n = Entry(window, width=5, bg="DarkOrange3", selectbackground='DarkOrange3', font=("rany",16), fg="black", validate="key")
table_n['validatecommand'] = (table_n.register(testVal), '%P', '%d')
table_n.place(x=400,y=75)

label_m = Label(window, text="Введите частоту(ГГц): ", font=("rany",16), bg="DarkOrange3", fg="black")
label_m.place(x=25,y=175)
frequincy = Entry(window, width=5, bg="DarkOrange3", selectbackground='DarkOrange3', font=("rany",16), fg="black", validate="key")
frequincy['validatecommand'] = (frequincy.register(testVal), '%P', '%d')
frequincy.place(x=400,y=175)

waveguide_size = Label(window, text="Введите размер волновода (см):", font=("rany",16), bg="DarkOrange3", fg="black")
waveguide_size.place(x=25,y=225)

a_x_size = Label(window, text="a: ", font=("rany",16), bg="DarkOrange3", fg="black")
a_x_size.place(x=375,y=225)
a_x_size_entry = Entry(window, width=5, bg="DarkOrange3", selectbackground='DarkOrange3', font=("rany",16), fg="black", validate="key")
a_x_size_entry['validatecommand'] = (a_x_size_entry.register(testVal), '%P', '%d')
a_x_size_entry.place(x=400,y=225)

b_x_size = Label(window, text="b: ", font=("rany",16), bg="DarkOrange3", fg="black")
b_x_size.place(x=375,y=275)
b_x_size_entry = Entry(window, width=5, bg="DarkOrange3", selectbackground='DarkOrange3', font=("rany",16), fg="black", validate="key")
b_x_size_entry['validatecommand'] = (b_x_size_entry.register(testVal), '%P', '%d')
b_x_size_entry.place(x=400,y=275)

size_lines = Label(window, text="Количество линей уровня: ", font=("rany",16), bg="DarkOrange3", fg="black")
size_lines.place(x=25,y=325)
size_lines_entry = Entry(window, width=5, bg="DarkOrange3", selectbackground='DarkOrange3', font=("rany",16), fg="black", validate="key")
size_lines_entry['validatecommand'] = (size_lines_entry.register(testVal), '%P', '%d')
size_lines_entry.place(x=400,y=325)

label = Label(window, text=" ", font=("rany",16), bg="DarkOrange3")
label.place(x=25,y=550)
time = 0
label_time = Label(window, text="Время: ", font=("rany",16), bg="DarkOrange3", fg="black")
label_time.place(x=25,y=375)
time_label = Label(window, text=time, font=("rany",16), bg="DarkOrange3", fg="black")
time_label.place(x=400,y=375)

scale = Scale(window, orient="horizontal", from_=0, to=25,  font=("rany",16), bg="DarkOrange3", fg="black", command=onScale)
label_time_entry = scale
scale.place(x=315,y=400, anchor="c", height=50, width=300)

click = Button(window, text="Построить графики силовых линий", font=("rany",16), bg="DarkOrange3", fg="black", command=plotting)
click.place(x=240,y=500, anchor="c", height=50, width=450)

label_color = Label(window, text="H-синий, E-красный", anchor="n", font=("rany",16), bg="DarkOrange3", fg="black")
label_color.place(relx=.7, rely=.5, anchor="c", height=800, width=700, bordermode=OUTSIDE)

window.mainloop()

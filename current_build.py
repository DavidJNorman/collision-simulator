#Version for York University Raspberry Pi Challenge, created 29 Sept 2017

# imports the relevant libraries to enable functionality of the program
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from time import *

# creates the Tkinter GUI environment
master = Tk()

l_frame=Frame(master)
l_frame.grid(row=0)

r_frame=Frame(master)
r_frame.grid(row=0, column=1)

def updateGraph(graph,x_1,x_2,canvas):
        graph.clf()#Clear previous plots
        a = graph.add_subplot(111)#
        a.set_xlim([0,20])
        a.set_ylim([0,1])
        a.set_autoscale_on(False)
        a.plot([x_1],[0.5],"bo")
        a.plot([x_2],[0.5],"ro")
        canvas.show()
        master.update()#Update TKinter

# calculates terminal velocities, displays them, and animates the collision using a Matplotlib graph integrated into Tkinter
def calculate():
        try:
                m_1 = float(m1_e.get())
                u_1 = float(u1_e.get())
                m_2 = float(m2_e.get())
                u_2 = float(u2_e.get())
                e = float(e_e.get())

                if m_1<0 or m_2<0:
                        print("Error")

                else:
                        v_1 = (m_1*u_1 + m_2*u_2 - e*m_2*(u_1 - u_2))/(m_1 + m_2)
                        v_2 = (m_1*(u_1 - v_1))/m_2 + u_2
            
                        Label(l_frame, text=str(v_1)).grid(row=2, column=4, sticky=W)
                        Label(l_frame, text=str(v_2)).grid(row=5, column=4, sticky=W)
                        x_1=5 #starting values
                        x_2=15
            
                        f = Figure(figsize=(5,5), dpi=100)

                        canvas = FigureCanvasTkAgg(f, r_frame)
                        canvas.show()
                        canvas.get_tk_widget().grid(row=0)

                        startTime = time()

                        while x_1 < x_2:
                                dt = time() - startTime
                                x_1 += (u_1*dt)/100
                                x_2 += (u_2*dt)/100
                                updateGraph(f,x_1,x_2,canvas)

                        while x_1>0 and x_2<20 and (v_1!=0 or v_2!=0):
                                dt = time() - startTime
                                x_1 += (v_1*dt)/100
                                x_2 += (v_2*dt)/100
                                updateGraph(f,x_1,x_2,canvas)
                
        except:
                print("Error")

# specifies the graphical user interface using Tkinter  
Label(l_frame, text="Object 1").grid(row=0)
Label(l_frame, text="Numerical values only!").grid(row=0, column=1)
Label(l_frame, text="Valid values").grid(row=0, column=2)

Label(l_frame, text="Object 1").grid(row=0, column=3)

Label(l_frame, text="Mass: (kg)").grid(row=1, sticky=W)

m1_e = Entry(l_frame)
m1_e.grid(row=1, column=1)
Label(l_frame, text="+ve").grid(row=1, column=2, sticky=W)

Label(l_frame, text="Initial velocity: (m/s)").grid(row=2, sticky=W)

u1_e = Entry(l_frame)
u1_e.grid(row=2, column=1)


Label(l_frame, text="Terminal velocity: (m/s)").grid(row=2, column=3, sticky=W)
Label(l_frame, text="0").grid(row=2, column=4, sticky=W)

Label(l_frame, text="Object 2").grid(row=3)

Label(l_frame, text="Object 2").grid(row=3, column=3)

Label(l_frame, text="Mass: (kg)").grid(row=4, sticky=W)

m2_e = Entry(l_frame)
m2_e.grid(row=4, column=1)
Label(l_frame, text="+ve").grid(row=4, column=2, sticky=W)
                               
Label(l_frame, text="Initial velocity: (m/s)").grid(row=5, sticky=W)

u2_e = Entry(l_frame)
u2_e.grid(row=5, column=1)

Label(l_frame, text="Terminal velocity: (m/s)").grid(row=5, column=3, sticky=W)
Label(l_frame, text="0").grid(row=5, column=4, sticky=W)

Label(l_frame, text="Other").grid(row=6)

Label(l_frame, text="Coefficient of restitution:").grid(row=7, sticky=W)

e_e = Entry(l_frame)
e_e.grid(row=7, column=1)
Label(l_frame, text="0-1").grid(row=7, column=2, sticky=W)

calc_b = Button(l_frame, text="Simulate Collision", command=calculate)
calc_b.grid(row=8, sticky=W)

exit_b = Button(l_frame, text="Exit", command=master.destroy)
exit_b.grid(row=9, sticky=W)

mainloop()

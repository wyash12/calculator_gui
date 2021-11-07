from tkinter import *

r = Tk()
r.title("Calculator")

e = Entry(r, width=50,borderwidth=5)
e.grid(row=0,column =0, columnspan=3,padx=10,pady=10)


def button_add():
    return


button_1=Button(r,text="1", padx=40,pady=20,command=button_add)
button_2=Button(r,text="2", padx=40,pady=20,command=button_add)
button_3=Button(r,text="3", padx=40,pady=20,command=button_add)
button_4=Button(r,text="4", padx=40,pady=20,command=button_add)
button_5=Button(r,text="5", padx=40,pady=20,command=button_add)
button_6=Button(r,text="6", padx=40,pady=20,command=button_add)
button_7=Button(r,text="7", padx=40,pady=20,command=button_add)
button_8=Button(r,text="8", padx=40,pady=20,command=button_add)
button_9=Button(r,text="9", padx=40,pady=20,command=button_add)
button_0=Button(r,text="0", padx=40,pady=20,command=button_add)
button_add=Button(r,text="+",padx=39,pady=20,command=button_add)
button_equals=Button(r,text="=",padx=90,pady=20,command=button_add)
buttonc =Button(r,text="C",padx=90,pady=20,command=button_add)
button_decimal =Button(r,text=".",padx=40,pady=20,command=button_add)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2 ,column=0)
button_5.grid(row=2 ,column=1)
button_6.grid(row=2 ,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0, columnspan=1)
button_add.grid(row=5,column=0)
button_equals.grid(row=5,column=1,columnspan=2)
buttonc.grid(row=4,column=1,columnspan=2)

r.mainloop()

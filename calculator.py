from tkinter import *

root=Tk()
root.title("Calci")

e=Entry(root,width=55,borderwidth=5,bg="#000000",fg="#00ff00")
e.grid(row=0,column=0,columnspan=3,padx=20,pady=20)
#e.insert(0,"")

def button_click(num):
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(num))

def button_clear():
    e.delete(0,END)

'''def button_sum():
    first_num = int(e.get())
    global f_num 
    f_num=first_num
    e.delete(0,END)'''
    
def button_euqal():
    '''second_num = e.get()
    e.delete(0,END)
    e.insert(0,f_num + int(second_num))'''
    ans = e.get()
    e.delete(0,END)
    e.insert(0,eval(ans))

#define button
b_1=Button(root,text="1",padx=40,pady=20,command= lambda: button_click(1),bg="#000000",fg="#ffffff",activebackground="#00ff00")  
b_2=Button(root,text="2",padx=40,pady=20,command= lambda: button_click(2),bg="#000000",fg="#ffffff",activebackground="#00ff00")
b_3=Button(root,text="3",padx=40,pady=20,command= lambda: button_click(3),bg="#000000",fg="#ffffff",activebackground="#00ff00")
b_4=Button(root,text="4",padx=40,pady=20,command= lambda: button_click(4),bg="#000000",fg="#ffffff",activebackground="#00ff00")
b_5=Button(root,text="5",padx=40,pady=20,command= lambda: button_click(5),bg="#000000",fg="#ffffff",activebackground="#00ff00")
b_6=Button(root,text="6",padx=40,pady=20,command= lambda: button_click(6),bg="#000000",fg="#ffffff",activebackground="#00ff00")
b_7=Button(root,text="7",padx=40,pady=20,command= lambda: button_click(7),bg="#000000",fg="#ffffff",activebackground="#00ff00")
b_8=Button(root,text="8",padx=40,pady=20,command= lambda: button_click(8),bg="#000000",fg="#ffffff",activebackground="#00ff00")
b_9=Button(root,text="9",padx=40,pady=20,command= lambda: button_click(9),bg="#000000",fg="#ffffff",activebackground="#00ff00")
b_0=Button(root,text="0",padx=40,pady=20,command= lambda: button_click(0),bg="#000000",fg="#ffffff",activebackground="#00ff00")

b_sum=Button(root,text="+",padx=39,pady=20,command=lambda: button_click('+'),activebackground="#00ff00",bg="#b3b3b3")
b_sub=Button(root,text="-",padx=40,pady=20,command=lambda: button_click('-'),activebackground="#00ff00",bg="#b3b3b3")
b_division=Button(root,text="*",padx=39,pady=20,command=lambda: button_click('*'),activebackground="#00ff00",bg="#b3b3b3")
b_multi=Button(root,text="/",padx=39,pady=20,command=lambda: button_click('/'),activebackground="#00ff00",bg="#b3b3b3")
b_equal=Button(root,text="=",padx=100,pady=20,command=lambda: button_euqal(),activebackground="#00ff00",bg="#ffffff",fg="#000000")
b_clear=Button(root,text="cls",padx=97,pady=20,command=lambda: button_clear(),activebackground="#00ff00",bg="#ffffff",fg="#000000")





#show on the screen
b_7.grid(row=1,column=0)
b_8.grid(row=1,column=1)
b_9.grid(row=1,column=2)

b_4.grid(row=2,column=0)
b_5.grid(row=2,column=1)
b_6.grid(row=2,column=2)

b_3.grid(row=3,column=0)
b_2.grid(row=3,column=1)
b_1.grid(row=3,column=2)

b_0.grid(row=4,column=0)
b_sum.grid(row=5,column=0)
b_sub.grid(row=6,column=0)
b_division.grid(row=6,column=1)
b_multi.grid(row=6,column=2)


b_equal.grid(row=5,column=1,columnspan=2)
b_clear.grid(row=4,column=1,columnspan=2)


root.mainloop()
from tkinter import *
root=Tk()
root.geometry('250x150') 

lb_frame=LabelFrame(root,text="This is a Label")
lb_frame.pack()

btn1 = Button(lb_frame, text = 'Button 1') 
btn1.place(x = 30, y = 10) 
btn2 = Button(lb_frame, text = 'Button 2') 
btn2.place(x = 130, y = 10) 

chkbtn1 = Checkbutton(lb_frame, text = 'Checkbutton 1') 
chkbtn1.place(x = 30, y = 50) 
chkbtn2 = Checkbutton(lb_frame, text = 'Checkbutton 2') 
chkbtn2.place(x = 30, y = 80) 



button=Button(lb_frame,text="Click Here")
button.pack()

root.mainloop()
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askyesno
from PIL import ImageTk, Image


root = Tk()
root.geometry('1350x700+0+0')
root.title("Grocery")
root.config(bg='lightgreen')
def back():
    answer = askyesno(title='confirmation',
                    message='Are you sure that you want to go back?')
    if answer:
        root.destroy()
        import welcome
def quit():
    
    answer = askyesno(title='Confirmation',
                    message='Are you sure that you want to exit?')
    if answer:
        root.destroy()
def submit():
    answer = askyesno(title='Confirmation',
                    message='Are you sure that you want to submit?')
    if answer:
        root.destroy()
photo = tk.PhotoImage(file='./images/store.png')
image = Image.open('./images/store.png')

root.iconphoto(True, photo)
canvas= Canvas(root, width= 65, height= 65,bg="lightgreen")
canvas.place(x=50, y=10)

#Load an image in the script
img= (Image.open("food.png"))

#Resize the Image using resize method
resized_image= img.resize((50,50), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW ,image=new_image)
title = Label(root, text="XYZ HYPERMART", fg="red",font=("Arial",10,'bold'),bg="lightgreen")
title.place(x=32,y=80)

cat = Label(root, text="CATEGORIES", fg="black",font=("Times",32,'bold'),bg="lightgreen")
cat.place(x=500,y=20)

backbtn = Button(root,fg="green",relief="ridge",text="Go Back", command=lambda:back(),cursor="hand2",bg="white")
backbtn.place(x=1280,y=20)

frame = Frame(root, height="500", width="1250",bg="lightgreen",relief="ridge")
frame.place(x=50,y=100)
oil_btn = Button(frame, font = ("Times",22,"bold"),height=1,width=20,bg="green", relief=RIDGE,cursor="hand2", text="OILS",fg="white",command=lambda:oil())
oil_btn.place(x=60,y=60)
fruit_btn = Button(frame, font = ("Times",22,"bold"),height=1,width=20,bg="green", relief=RIDGE,cursor="hand2", text="FRUITS",fg="white",command=lambda:fruit())
fruit_btn.place(x=60,y=160)
veg_btn = Button(frame, font = ("Times",22,"bold"),height=1,width=20,bg="green", relief=RIDGE,cursor="hand2", text="VEGETABLES",fg="white",command=lambda:veg())
veg_btn.place(x=60,y=260)
pulse_btn = Button(frame, font = ("Times",22,"bold"),height=1,width=20,bg="green", relief=RIDGE,cursor="hand2", text="PULSES",fg="white",command=lambda:pulse())
pulse_btn.place(x=800,y=60)
reg_btn = Button(frame, font = ("Times",22,"bold"),height=1,width=20,bg="green", relief=RIDGE,cursor="hand2", text="STAPLES",fg="white",command=lambda:reg())
reg_btn.place(x=800,y=160)
care_btn = Button(frame, font = ("Times",22,"bold"),height=1,width=20,bg="green", relief=RIDGE,cursor="hand2", text="BODY CARE",fg="white",command=lambda:care())
care_btn.place(x=800,y=260)

exit_btn = Button(root,fg="green",relief="ridge",text="Exit", command=lambda:quit(),cursor="hand2",height=1,width=7,bg="white")
exit_btn.place(x=20,y=650)

submitbtn = Button(root,fg="white",relief="ridge",text="SUBMIT", command=lambda:submit(),cursor="hand2",height=1,width=10,bg="red",font=("Times",18,'bold'))
submitbtn.place(x=1150,y=630)

def oil():
    root.destroy()
    import oil
def fruit():
    root.destroy()
    import fruit
def veg():
    root.destroy()
    import veg
def pulse():
    root.destroy()
    import pulse
def reg():
    root.destroy()
    import reg
def care():
    root.destroy()
    import care

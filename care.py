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
        import categories
def quit():
    
    answer = askyesno(title='Confirmation',
                    message='Are you sure that you want to exit?')
    if answer:
        root.destroy()
def submit():
    answer = askyesno(title='Confirmation',
                    message='Are you sure that you want to save?')
    if answer:
        grocery = []
        for i in items:
            if i[1]!=0:
                grocery.append(i[0])

        root.destroy()
        import categories
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

cat = Label(root, text="BODY CARE", fg="black",font=("Times",32,'bold'),bg="lightgreen")
cat.place(x=550,y=20)

backbtn = Button(root,fg="green",relief="ridge",text="Go Back", command=lambda:back(),cursor="hand2")
backbtn.place(x=1280,y=20)

exit_btn = Button(root,fg="green",relief="ridge",text="Exit", command=lambda:quit(),cursor="hand2",height=1,width=7)
exit_btn.place(x=20,y=650)

submitbtn = Button(root,fg="white",relief="ridge",text="SAVE", command=lambda:submit(),cursor="hand2",height=1,width=10,bg="red",font=("Times",18,'bold'))
submitbtn.place(x=1150,y=630)

items = [["Beard Oil"], ["Body Wash"], ["Hair Oil"], ["Shampoo"], ["Hand Wash"],["Soap"],["Toothpaste"]]




checklist = tk.Text(root, width=20,bg="lightgreen",height=25)
checklist.place(x=580,y=180)

for i in items:
    var = tk.IntVar()
    i.append(var)
    checkbutton = tk.Checkbutton(checklist, text=i[0], variable=var,cursor="arrow",bg="green",fg="white",height=1)
    checklist.window_create("end", window=checkbutton)
    checklist.insert("end", "\n\n")



# disable the widget so users can't insert text into it
checklist.configure(state="disabled")

root.mainloop()

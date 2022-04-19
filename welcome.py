#welcome page

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

def start():
        root.destroy()

        import categories
def quit():
    
    answer = askyesno(title='Confirmation',
                    message='Are you sure that you want to exit?')
    if answer:
        root.destroy()
photo = tk.PhotoImage(file='./images/store.png')
image = Image.open('./images/store.png')

root.iconphoto(True, photo)
canvas= Canvas(root, width= 100, height= 100,bg="lightgreen")
canvas.place(x=620, y=50)

#Load an image in the script
img= (Image.open("food.png"))

#Resize the Image using resize method
resized_image= img.resize((90,100), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW ,image=new_image)
'''
frame = Frame(root,height='120',width='120', relief="groove",bg="lightgreen")
frame.pack()
logo = Label(frame,image=photo)
logo.place(x=600,y=100
        )
logo.pack()
'''
header = Label(root, text="WELCOME TO", fg="black",
               font=("Times New Roman",32),
               background="lightgreen")
header.place(x=530, y=180)
name = Label(root, text="XYZ HYPERMART", fg="red",
               font=("Arial",52,"bold"),
               background="lightgreen",relief="groove")
name.place(x=370,y=250)
start_btn = Button(root, text="Start", font = ("Arial",12), fg="white",command=lambda: start(),height=1,width=7,bg="green", relief=RIDGE,cursor="hand2")
start_btn.place(x=630,y=400)
quit_btn = Button(root, text="Exit", fg="white",command=lambda: quit(),font = ("Arial",12),height=1,width=7,bg="green", relief=RIDGE,cursor="hand2")
quit_btn.place(x=630,y=450)
root.mainloop()

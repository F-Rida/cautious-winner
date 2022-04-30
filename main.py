import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askyesno
from PIL import ImageTk, Image
from tkinter.scrolledtext import ScrolledText
import math

#creating tkinter window
root = Tk()
#dimensions for tkinter window
root.geometry('1350x700')
#title for tkinter window
root.title("Grocery")
#background colour for tkinter window
root.config(bg='lightgreen')
# icon for tkinter window
photo = tk.PhotoImage(file='./images/store.png')
root.iconphoto(True, photo)
import networkx as nx
import matplotlib.pyplot as plt
import random

#functions:
def quit():
    
    answer = askyesno(title='Confirmation',
                    message='Are you sure that you want to exit?')
    if answer:
        root.destroy()

#We used Binary search iteratively because recursion takes more space complexity as compared to iteration
def binary_search_iterative(lst, item):
    start = 0
    end = len(lst) - 1
    mid = math.ceil(len(lst) / 2)

    found = False
    index = 0

    while found != True:
        if lst[mid] == item:
            found = True
            index = mid
            break
        elif mid >= end:
            return -1
        elif lst[mid] > item:
            end = mid - 1
            mid = (end + start) // 2
        elif lst[mid] < item:
            start = mid + 1
            mid = ((end + start) // 2)
    # print (index)
    return index

#Merge Sort HELPER Function
def merge(lsta, lstb):
    lstc = []
    while len(lsta) > 0 and len(lstb) > 0:
        if (lsta[0] > lstb[0]):
            lstc.append(lstb[0])
            lstb.pop(0)
        else:
            lstc.append(lsta[0])
            lsta.pop(0)

    while len(lsta) > 0:
        lstc.append(lsta[0])
        lsta.pop(0)
    while len(lstb) > 0:
        lstc.append(lstb[0])
        lstb.pop(0)

    return lstc

#main mergeSort function
def mergeSort(category_lst):
    if len(category_lst) <= 1:
        return category_lst
    else:
        mid = (len(category_lst)) // 2
        left1 = mergeSort(category_lst[:mid])
        right1 = mergeSort(category_lst[mid:])
        return merge(left1, right1)

#Categories function that sorts the customer list that we fetch from tkinter user input
def categorize(item_list, stock):
    #items GRAPH stores the items into their particular categories
    items = {'Fruits': [],
           'Oils': [],
           'Pulses': [],
           'Regular Items': [],
           'Shampoo_body_care': [],
           'Vegetables': []}

    for item in item_list: #traversing the items list provided by user
        for category in stock: #taking each node in the stock shelves
            #for product in stock[category]: #checking each product whether it is present in that category
            if item in stock[category]:
                #We used binary search algoritm instead of linear search as it is more efficient and has less time complexity
                index = binary_search_iterative(stock[category], item)
                items[category].append(stock[category][index])  # appending into the ITEMS GRAPH
                break

    #SORTING INTO ALPHABETIC ORDER NEEDED TO BE DONE NOW
    #print(items)

    return_G = {'Fruits': [],
           'Oils': [],
           'Pulses': [],
           'Regular Items': [],
           'Shampoo_body_care': [],
           'Vegetables': []}
     # It will store the ordered dictionary

    #MERGE SORT IMPLEMENTED ON EACH CATEGORY AND THEN STORED
    for category in items:
        return_G[category] = mergeSort(items[category])

    #return return_G

    return_lst = [] #FINAL LIST THAT NEEDS TO BE RETURNED.
    for category in items:
        for product in return_G[category]:
            return_lst.append(product)

    return return_lst

##################################################################################################

def getNeighbours(G, node): #to find adjacent nodes/vertices
    neighbours=[]
    for i in G[node]:
        neighbours.append(i)
    return neighbours
    
def Enqueue(PriorityQ,d): # for enqueuing variable in priorityQ FIFO
  if d not in PriorityQ:
    for i in PriorityQ:
        if d[1]<i[1]: #Condition for deciding priority min to max distance
          PriorityQ.insert(PriorityQ.index(i), d)
          return PriorityQ
    PriorityQ.append(d)
    return PriorityQ
    
def Dequeue(PriorityQ): # for dequeing variable in this case a whole tuple from the PQ FIFO
  return PriorityQ.pop(0) 
  
def dictionary(g,para): # A dictionary to maintain distances
  d = {}
  for i in g:
    d[i]=para
  return d
  
def getShortestPath(graph, Source_Node, Destination_Node): #Dijkstra Implementation 
  destination = Destination_Node
  PriorityQ=[(Source_Node,0)]
  Dist = dictionary(graph, [math.inf,'']) #to first initialize distances to infinity 
  Dist[Source_Node]= [0,Source_Node]
  visited = []

  while len(PriorityQ)>0: #until and unless PQ is not empty compeltely loop over
    u = Dequeue(PriorityQ)
    visited.append(u[0])
    children = getNeighbours(graph, u[0])
    for child in children:
        if child not in visited:
            if (child[1]+Dist[u[0]][0])<Dist[child[0]][0]: #If distance of 1 is less than the other then swap (shortest path calculation)
                Dist[child[0]] = [(child[1]+Dist[u[0]][0]),u[0]] 
                Enqueue(PriorityQ,child)

  path = [Destination_Node]
  path1 =''
  while Source_Node not in path1:
    path.append(Dist[Destination_Node][1])
    Destination_Node = Dist[Destination_Node][1]
    path1+= Destination_Node
  return path[::-1], Dist[destination][0]

 # Main_call to call function GetShortestPath algo to traverse each changing node
 # This was used to takecare of the changing nodes i.e source node and destination node

def Main_call(ordered_list,g ):
    # lst has all the shortest paths for all the given items in the ordered list
    # path gets appended to lst, so yes! lst is nested list here.
    # ordered_list.insert(0,'Start')

    lst = []
    path= []
    for order in range(len(ordered_list)-1):
            Source_Node = ordered_list[order]
            Destination_Node = ordered_list[order+1]
            path = getShortestPath(g, Source_Node, Destination_Node)
            lst.append(path[0])

    return lst

#Weighted Graph for stock in the store, here weights are distances from start to item and between adjacent nodes/neighbours.
# This here, is used for function shortest path algo and in main call function

g = {'Start': [("Apple", 2),('Banana', 4), ('Coconut Oil', 12), ('Chickpeas', 22), ('Flour', 32), ('Beard Oil', 42),('Bottle Gourd', 52)],
     'Apple': [('Start', 2), ('Banana', 4), ('Coconut Oil', 14)],
     'Banana': [('Apple', 2), ('Grapes', 2)],
     'Grapes': [('Mustard Seed Oil', 7), ('Guava', 6)],
     'Guava': [('Olive Oil', 5), ('Peach', 1)],
     'Watermelon': [('Peach', 1), ('Soybean Oil', 10)],
     'Peach': [('Watermelon', 1), ('Guava', 1)],

     'Coconut Oil': [("Start", 12), ('Apple', 14), ('Desi Ghee', 2), ('Chickpeas', 14)],
     'Desi Ghee': [('Coconut Oil', 2), ('Mustard Seed Oil', 2)],
     'Mustard Seed Oil': [('Desi Ghee', 2), ('Grapes', 7), ('Daal Chana', 7), ('Olive Oil', 6)],
     'Olive Oil': [('Mustard Seed Oil', 6), ('Guava', 5), ('Sunflower Seed Oil', 1), ('Daal Kali Masoor', 5)],
     'Sunflower Seed Oil': [('Olive Oil', 1), ('Soybean Oil', 1)],
     'Soybean Oil': [('Sunflower Seed Oil', 1), ('Daal Mong', 10)],

     'Chickpeas': [('Start', 22), ('Coconut Oil', 14), ('Daal Arhar', 2), ('Flour', 14)],
     'Daal Arhar': [('Chickpeas', 2), ('Daal Chana', 2)],
     'Daal Chana': [('Daal Arhar', 2), ('Mustard Seed Oil', 7), ('Rice', 7), ('Daal Kali Masoor', 6)],
     'Daal Kali Masoor': [('Daal Chana', 6), ('Daal Maash', 1), ('Olive Oil', 5), ('Spices', 5)],
     'Daal Maash': [('Daal Kali Masoor', 1), ('Daal Mong', 1)],
     'Daal Mong': [('Daal Maash', 1), ('Tea', 10)],

     'Flour': [('Start', 32), ('Chickpeas', 14), ('Milk', 2), ('Beard Oil', 14)],
     'Milk': [('Flour', 2), ('Rice', 2)],
     'Rice': [('Milk', 2), ('Daal Chana', 7), ('Spices', 6), ('Hair Oil', 7)],
     'Spices': [('Daal Kali Masoor', 5), ('Rice', 6), ('Sugar', 1), ('Soap', 5)],
     'Sugar': [('Spices', 1), ('Tea', 1)],
     'Tea': [('Sugar', 1), ('Daal Mong', 10)],

     'Beard Oil': [('Start', 42), ('Flour', 14), ('Bottle Gourd', 14), ('Body Wash', 2)],
     'Body Wash': [('Beard Oil', 2), ('Hair Oil', 2)],
     'Hair Oil': [('Rice', 7), ('Green Chilli', 7), ('Soap', 6), ('Body Wash', 2)],
     'Soap': [('Hair Oil', 6), ('Spices', 5), ('Lemons', 5), ('Toothpaste', 1)],
     'Toothpaste': [('Soap', 1), ('Hand Wash', 1)],
     'Hand Wash': [('Toothpaste', 1), ('Red Chilli', 10)],

     'Bottle Gourd': [('Start', 52), ('Coriander', 2), ('Beard Oil', 14)],
     'Coriander': [('Bottle Gourd', 2), ('Green Chilli', 2)],
     'Green Chilli': [('Lemons', 6), ('Hair Oil', 7), ('Coriander', 2)],
     'Lemons': [('Green Chilli', 6), ('Soap', 5), ('Onions', 1)],
     'Onions': [('Lemons', 1), ('Red Chilli', 1)],
     'Red Chilli': [('Onions', 1), ('Hand Wash', 10)]}

# Unweighted graph used for sorting/ordering the list provided by customer as input
# A dictionary and a type of a tree that stores all items according
# the catogories of aisles they are kept in alphabetic order

Stock_G = {'Fruits': ['Apple', 'Banana', 'Grapes', 'Guava', 'Peach', 'Watermelon'],
           'Oils': ['Coconut Oil', 'Desi Ghee', 'Mustard Seed Oil', 'Olive Oil', 'Sunflower Seed Oil', 'Soybean Oil'],
           'Pulses': ['Chickpeas', 'Daal Arhar', 'Daal Chana', 'Daal Kali Masoor', 'Daal Maash', 'Daal Mong'],
           'Regular Items': ['Flour', 'Milk', 'Rice', 'Spices', 'Sugar', 'Tea'],
           'Shampoo_body_care': ['Beard Oil', 'Body Wash', 'Hair Oil', 'Soap', 'Toothpaste', 'Hand Wash'],
           'Vegetables': ['Bottle Gourd', 'Coriander', 'Green Chilli', 'Lemons', 'Onions', 'Red Chilli']}




#creating a frame for welcome page
welcome_page = Frame(root, height = 600, width = 1250, bg='lightgreen', bd=5, relief=RIDGE)
categories_page = Frame(root, height = 600, width = 1250, bg='lightgreen', bd=5, relief=RIDGE)
#logo for the mart--open image
img = Image.open('./images/store.png')
#canvas for the logo image
canvas= Canvas(welcome_page, width= 100, height= 100,bg="lightgreen")
canvas.place(x=570, y=20)
#resizing and formatting image to desired size
resized_img= img.resize((80,80), Image.ANTIALIAS)
#this method returns a warning that ANTIALIAS is deprecated and will be removed in Pillow 10 (2023-07-01)
# which means that the function would no longer work on the new pillow update that releases in 2023.

new= ImageTk.PhotoImage(resized_img)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW ,image=new)


#welcome page title labels
header = Label(welcome_page, text="WELCOME TO", fg="black",
               font=("Times New Roman",32,'bold'),
               background="lightgreen")
header.place(x=480, y=150)
name = Label(welcome_page, text="XYZ HYPERMART", fg="red",
               font=("Arial",52,"bold"),
               background="lightgreen",relief="groove")
name.place(x=330,y=220)
start_btn = Button(welcome_page, text="Start", font = ("Arial",12,'bold'), fg="white",command=lambda: categories_page.place(x=50,y=35),height=2,width=10,bg="green", relief=RIDGE,cursor="hand2")
start_btn.place(x=570,y=350)
quit_btn = Button(welcome_page, text="Exit", fg="white",command=lambda: quit(),font = ("Arial",12,'bold'),height=2,width=10,bg="green", relief=RIDGE,cursor="hand2")
quit_btn.place(x=570,y=420)

canvas= Canvas(categories_page, width= 55, height= 55,bg="lightgreen")
canvas.place(x=1140, y=10)

resize1 = img.resize((40,40), Image.ANTIALIAS)
new1 = ImageTk.PhotoImage(resize1)
#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW ,image=new1)
title = Label(categories_page, text="XYZ HYPERMART", fg="red",font=("Arial",10,'bold'),bg="lightgreen")
title.place(x=1110,y=70)

head = Label(categories_page, text="CATEGORIES", fg="black",font=("Times",32,'bold'),bg="lightgreen")
head.place(x=500,y=20)


exit_btn = Button(categories_page,fg="green",relief="ridge",text="Exit", command=lambda:quit(),cursor="hand2",height=1,width=7,bg="white")
exit_btn.place(x=20,y=550)



items = {'Fruits': [['Apple'], ['Banana'], ['Grapes'], ['Guava'], ['Peach'], ['Watermelon']],
           'Oils': [['Coconut Oil'], ['Desi Ghee'], ['Mustard Seed Oil'], ['Olive Oil'], ['Sunflower Seed Oil'], ['Soybean Oil']],
           'Pulses': [['Chickpeas'], ['Daal Arhar'], ['Daal Chana'], ['Daal Kali Masoor'], ['Daal Maash'], ['Daal Mong']],
           'Regular Items': [['Flour'], ['Milk'], ['Rice'], ['Spices'], ['Sugar'], ['Tea']],
           'Shampoo_body_care': [['Beard Oil'], ['Body Wash'], ['Hair Oil'], ['Soap'], ['Toothpaste'], ['Hand Wash']],
           'Vegetables': [['Bottle Gourd'], ['Coriander'], ['Green Chilli'], ['Lemons'], ['Onions'],[ 'Red Chilli']]}



stapless = Label(categories_page,text="FRUITS", foreground="white",background="green",
             borderwidth=2, justify=tk.CENTER,width=21, font=("Times",22,"bold"),
             relief="ridge")
stapless.place(x=20,y=100)
text = ScrolledText(categories_page, width=42, height=10)
text.place(x=20,y=140)
text.insert("end", "\n")

for i in items['Fruits']:
    var = IntVar()
    
    
    checkbutton = Checkbutton(text, text=i[0], variable=var,cursor="arrow",
                              bg='white', fg='black',height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n")
    i.append(var)


oil = Label(categories_page,text="OILS", foreground="white",
                background="green", borderwidth=2, justify=tk.CENTER,width=21,
                font=("Times",22,"bold"), relief="ridge")
oil.place(x=420,y=100)
text = ScrolledText(categories_page, width=42, height=10,bd=2)
text.place(x=420,y=140)
text.insert("end", "\n")

for i in items['Oils']:
    var = IntVar()
    
    
    checkbutton = Checkbutton(text, text=i[0], variable=var,cursor="arrow",
                              bg='white', fg='black',height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n")
    i.append(var)
# Make the widget inaccessible to users by preventing them from inserting text into it.
text['state']='disabled'


fruit = Label(categories_page,text="PULSES", foreground="white",background="green",
                borderwidth=2, justify=tk.CENTER,width=21, font=("Times",22,"bold"),
                relief="ridge")
fruit.place(x=820,y=100)
text = ScrolledText(categories_page, width=42, height=10)
text.place(x=820,y=140)
text.insert("end", "\n")

for i in items['Pulses']:
    var = IntVar()
    
    checkbutton = Checkbutton(text, text=i[0], variable=var,cursor="arrow",
                              bg='white', fg='black',height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n")
    i.append(var)
# Make the widget inaccessible to users by preventing them from inserting text into it.
text['state']='disabled'


vegs = Label(categories_page,text="STAPLES", foreground="white",background="green",
                borderwidth=2, justify=tk.CENTER,width=21, font=("Times",22,"bold"),
                relief="ridge")
vegs.place(x=20,y=330)
text = ScrolledText(categories_page, width=42, height=10)
text.place(x=20,y=370)
text.insert("end", "\n")

for i in items['Regular Items']:
    var = IntVar()
   
    checkbutton = Checkbutton(text, text=i[0],
                              variable=var,cursor="arrow",bg='white', fg='black',
                              height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n")
    i.append(var)
# Make the widget inaccessible to users by preventing them from inserting text intoit.
text['state']='disabled'




pulses = Label(categories_page,text="BODY CARE", foreground="white",background="green",
                borderwidth=2, justify=tk.CENTER,width=21, font=("Times",22,"bold"),
                relief="ridge")
pulses.place(x=420,y=330)
text = ScrolledText(categories_page, width=42, height=10)
text.place(x=420,y=370)
text.insert("end", "\n")

for i in items['Shampoo_body_care']:
    var = IntVar()
    
    checkbutton = Checkbutton(text, text=i[0],
                              variable=var,cursor="arrow",bg='white', fg='black',
                              height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n")
    i.append(var)
# Make the widget inaccessible to users by preventing them from inserting text into it.
text['state']='disabled'


body = Label(categories_page,text="VEGETABLES", foreground="white",
                background="green", borderwidth=2, justify=tk.CENTER,width=21,
                font=("Times",22,"bold"))
body.place(x=820,y=330)
text = ScrolledText(categories_page, width=42, height=10)
text.place(x=820,y=370)
text.insert("end", "\n")

for i in items['Vegetables']:
    var = IntVar()
   
    
    checkbutton = Checkbutton(text, text=i[0], variable=var,cursor="arrow",
                              bg='white', fg='black',height=2,anchor='w',font=("Arial",12),padx=20)
    text.window_create("end", window=checkbutton)
    text.insert("end", "\n")
    i.append(var)
# Make the widget inaccessible to users by preventing them from inserting text into it.
text['state']='disabled'
customer_list = []
ordered_list = []
output = []
def submit():
    for i in items.keys():
        for j in items[i]:
            if j[1].get()==1:
                customer_list.append(j[0])
    if len(customer_list)==0:
        messagebox.showerror("Item Selection","No Items Selected")
    else:
        #Ordered_list calls categorize function to sort customer list with the help of unweighted graph called Stock_G

        ordered_list = categorize(customer_list, Stock_G) #Stock GRAPH/TREE was passed to make life easier

        #calling main call after ordered list to use ordered list as a parameter along with g, the weighted graph
        output = Main_call(ordered_list,g)
        G=nx.Graph(name="buba")

        edges = []
        for r in output:
            route_edges = [(r[n],r[n+1]) for n in range(len(r)-1)]
            G.add_nodes_from(r)
            G.add_edges_from(route_edges)
            edges.append(route_edges)



        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G,pos=pos,node_color="lightgreen")
        nx.draw_networkx_labels(G,pos=pos,verticalalignment='top')
        colors = ['r', 'b', 'y']
        linewidths = [20,10,5]
        for ctr, edgelist in enumerate(edges):
            nx.draw_networkx_edges(G,pos=pos,edgelist=edgelist,edge_color = colors[2], width=linewidths[2])
        plt.savefig('map.png')

        messagebox.showinfo("PATH", "map.png saved in directory")        

submit_btn = Button(categories_page,fg="white",relief="ridge",text="SAVE", command=lambda:submit(),cursor="hand2",height=2,width=10,bg="red", font=("Arial",10,"bold"))
submit_btn.place(x=1130,y=540)


welcome_page.place(x=50, y=35)
root.mainloop()

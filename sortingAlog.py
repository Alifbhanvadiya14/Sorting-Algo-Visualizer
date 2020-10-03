from tkinter import *
from tkinter import ttk
import random
from BubbleSort import bubbleSort
from quickSort import quick_sort
from selectionSort import selectionSort
from InsertionSort import insertionSort
from MergeSort import mergeSort

root = Tk()
root.title('Sorting Alogrithm Visualization')

root.maxsize(900,600)
root.config(bg='black')

# variables
selected_Algo = StringVar()
data = []

def drawData(data, colorArray):
    canvas.delete('all')
    c_height = 380
    c_width = 900
    x_width = c_width / (len(data) + 3)
    offset = 10
    spacing = 10

    normalizedData = [ i /max(data) for i in data]

    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height -height * 340

        #bottom right
        x1 = (i+1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0,y0,x1,y1, fill = colorArray[i])
        canvas.create_text(x0, y0, anchor =S, text = str(data[i]))
    
    root.update_idletasks()

def Generate():
    global data
    size = int(sizeEntry.get())
    
    minValue = int(minEntry.get())
    maxValue = int(maxEntry.get())
    
    data = []
    for _ in range(size):
        data.append(random.randrange(minValue,maxValue+1))
    
    drawData(data, ['red' for x in range(len(data))])


def StartAlgorithm():
    global data

    scale = speedScale.get()
    if not data: return

    if algMenu.get()  == 'Quick Sort':
        quick_sort(data, 0, len(data) -1 , drawData, scale, )
        
    elif algMenu.get()  == 'Bubble Sort':
        bubbleSort(data,drawData,scale)
    elif algMenu.get() == 'Selection Sort':
        selectionSort(data, drawData, scale)
    elif algMenu.get() == 'Merge Sort':
        mergeSort(data, drawData, scale)
    elif algMenu.get() == 'Insertion Sort':
        insertionSort(data, drawData, scale)

    drawData(data, ['green' for x in range(len(data))])



# frame / base layout

UI_frame = Frame(root, width = 800, height = 200 , bg = 'grey')
UI_frame.grid(row = 0,column = 0,padx = 10,pady = 5)

canvas = Canvas(root, width = 900,height = 380,bg= 'white' )
canvas.grid(row=1, column = 0,padx = 10,pady = 5)

# User Interface Area

#row[0]
Label(UI_frame, text = "Algorithm", bg='grey').grid(row=0, column = 0, padx =5 ,pady = 5, sticky = W)
algMenu = ttk.Combobox(UI_frame, textvariable = selected_Algo, values = ['Bubble Sort','Merge Sort', 'Quick Sort', 'Selection Sort','Insertion Sort'])
algMenu.grid(row=0,column=1, padx =5, pady =5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_ =0.1, to=5.0, length=200, digits =2, resolution=0.2, orient = HORIZONTAL, label="Select Speed [S]")
speedScale.grid(row=0, column = 2,padx = 5, pady = 5) 
Button(UI_frame ,text = "Start", command =StartAlgorithm, bg = 'red').grid(row=0, column =3 , padx=5, pady=5)


#row[1]
sizeEntry = Scale(UI_frame, from_=3, to=60,resolution=1, orient = HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column = 0, padx =5 ,pady = 5)


minEntry = Scale(UI_frame, from_ =0, to=20,  resolution=1, orient = HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column = 1, padx =5 ,pady = 5)


maxEntry = Scale(UI_frame, from_ =20, to=200, resolution=1, orient = HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column = 2, padx =5 ,pady = 5)

Button(UI_frame ,text = "Generate", command =Generate, bg = 'white').grid(row=1, column = 3, padx=5, pady=5)


root.mainloop()
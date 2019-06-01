from tkinter import *
import tkinter.colorchooser
import json
from PIL import Image,ImageTk
import tkinter.ttk


class Paper(Frame):
    firstx = 0
    firsty = 0
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.canpaper = Canvas(self, bg='white')
        self.canpaper.pack(fill='both', expand=True)
        self.canpaper.bind('<Button-1>', self.canpaperb1)
        self.canpaper.bind('<B1-Motion>', self.canpaperbm)

    def canpaperb1(self, event):
        if Tools.tools == 'pen':
            Paper.firstx = event.x
            Paper.firsty = event.y
        elif Tools.tools == 'Text':
            self.vartx = StringVar()
            self.txtent = Entry(self, textvariable=self.vartx)
            self.txtent.place(x=event.x, y=event.y)
            self.canpaper.create_text(event.x, event.y, fill=Colour.fill, text=self.vartx.get)
        elif Tools.tools == 'eraser':
            Paper.firstx = event.x
            Paper.firsty = event.y
        elif Tools.tools == 'bucket':
            self.canpaper['bg'] = Colour.fill

    def canpaperbm(self, event):
        if Tools.tools == 'pen':
            self.canpaper.create_line(Paper.firstx, Paper.firsty, event.x, event.y, fill=Colour.fill, width=Size.width)
            Paper.firstx = event.x
            Paper.firsty = event.y
        elif Tools.tools == 'Text':
            pass
        elif Tools.tools == 'eraser':
            self.canpaper.create_line(Paper.firstx, Paper.firsty, event.x, event.y, fill='white', width=6)
            Paper.firstx = event.x
            Paper.firsty = event.y
        elif Tools.tools == 'bucket':
            pass


class Colour(Frame):
    colordict = {}
    fill = '#000000'

    def __init__(self, master=None):
        super().__init__(master)
        # self.pack()
        self.index = 0
        self.createwidget()

    def createwidget(self):
        self.load_color()
        self.btn1 = Button(self, width=3, relief='sunken', bg=Colour.colordict['1'], bd=1)
        self.btn2 = Button(self, width=3, relief='sunken', bg=Colour.colordict['2'], bd=1)
        self.btn3 = Button(self, width=3, relief='sunken', bg=Colour.colordict['3'], bd=1)
        self.btn4 = Button(self, width=3, relief='sunken', bg=Colour.colordict['4'], bd=1)
        self.btn5 = Button(self, width=3, relief='sunken', bg=Colour.colordict['5'], bd=1)
        self.btn6 = Button(self, width=3, relief='sunken', bg=Colour.colordict['6'], bd=1)
        self.btn7 = Button(self, width=3, relief='sunken', bg=Colour.colordict['7'], bd=1)
        self.btn8 = Button(self, width=3, relief='sunken', bg=Colour.colordict['8'], bd=1)
        self.btn9 = Button(self, width=3, relief='sunken', bg=Colour.colordict['9'], bd=1)
        self.btn10 = Button(self, width=3, relief='sunken', bg=Colour.colordict['10'], bd=1)
        self.btn11 = Button(self, width=3, relief='sunken', bg=Colour.colordict['11'], bd=1)
        self.btn12 = Button(self, width=3, relief='sunken', bg=Colour.colordict['12'], bd=1)
        self.btn13 = Button(self, width=3, relief='sunken', bg=Colour.colordict['13'], bd=1)
        self.btn14 = Button(self, width=3, relief='sunken', bg=Colour.colordict['14'], bd=1)
        self.btn15 = Button(self, width=3, relief='sunken', bg=Colour.colordict['15'], bd=1)
        self.btn16 = Button(self, width=3, relief='sunken', bg=Colour.colordict['16'], bd=1)
        self.img = PhotoImage(file="Webp.net-resizeimage.png")
        self.btnpallet = Button(self, image=self.img, height=50, width=50)

        self.btn1.grid(row=0, column=0)
        self.btn2.grid(row=0, column=1)
        self.btn3.grid(row=0, column=2)
        self.btn4.grid(row=0, column=3)
        self.btn5.grid(row=0, column=4)
        self.btn6.grid(row=0, column=5)
        self.btn7.grid(row=0, column=6)
        self.btn8.grid(row=0, column=7)
        self.btn9.grid(row=1, column=0)
        self.btn10.grid(row=1, column=1)
        self.btn11.grid(row=1, column=2)
        self.btn12.grid(row=1, column=3)
        self.btn13.grid(row=1, column=4)
        self.btn14.grid(row=1, column=5)
        self.btn15.grid(row=1, column=6)
        self.btn16.grid(row=1, column=7)
        self.btnpallet.grid(row=0, column=8, rowspan=3)

        self.btn1.bind("<Button-1>", self.btn1_button)
        self.btn2.bind("<Button-1>", self.btn2_button)
        self.btn3.bind("<Button-1>", self.btn3_button)
        self.btn4.bind("<Button-1>", self.btn4_button)
        self.btn5.bind("<Button-1>", self.btn5_button)
        self.btn6.bind("<Button-1>", self.btn6_button)
        self.btn7.bind("<Button-1>", self.btn7_button)
        self.btn8.bind("<Button-1>", self.btn8_button)
        self.btn9.bind("<Button-1>", self.btn9_button)
        self.btn10.bind("<Button-1>", self.btn10_button)
        self.btn11.bind("<Button-1>", self.btn11_button)
        self.btn12.bind("<Button-1>", self.btn12_button)
        self.btn13.bind("<Button-1>", self.btn13_button)
        self.btn14.bind("<Button-1>", self.btn14_button)
        self.btn15.bind("<Button-1>", self.btn15_button)
        self.btn16.bind("<Button-1>", self.btn16_button)
        self.btnpallet.bind("<Button-1>", self.btnpallet_button1)

    def btnpallet_button1(self, event):
        color = tkinter.colorchooser.askcolor()
        Colour.colordict[self.index] = color[1]
        Colour.fill = Colour.colordict[str(self.index)]
        self.save_color()
        self.load_color()
        if self.index == 1:
            self.btn1['bg'] = color[1]
            self.btn1['bd'] = 2
        elif self.index == 2:
            self.btn2['bg'] = color[1]
            self.btn2['bd'] = 2
        elif self.index == 3:
            self.btn3['bg'] = color[1]
            self.btn3['bd'] = 2
        elif self.index == 4:
            self.btn4['bg'] = color[1]
            self.btn4['bd'] = 2
        elif self.index == 5:
            self.btn5['bg'] = color[1]
            self.btn5['bd'] = 2
        elif self.index == 6:
            self.btn6['bg'] = color[1]
            self.btn6['bd'] = 2
        elif self.index == 7:
            self.btn7['bg'] = color[1]
            self.btn7['bd'] = 2
        elif self.index == 8:
            self.btn8['bg'] = color[1]
            self.btn8['bd'] = 2
        elif self.index == 9:
            self.btn9['bg'] = color[1]
            self.btn9['bd'] = 2
        elif self.index == 10:
            self.btn10['bg'] = color[1]
            self.btn10['bd'] = 2
        elif self.index == 11:
            self.btn11['bg'] = color[1]
            self.btn11['bd'] = 2
        elif self.index == 12:
            self.btn12['bg'] = color[1]
            self.btn12['bd'] = 2
        elif self.index == 13:
            self.btn13['bg'] = color[1]
            self.btn13['bd'] = 2
        elif self.index == 14:
            self.btn14['bg'] = color[1]
            self.btn14['bd'] = 2
        elif self.index == 15:
            self.btn15['bg'] = color[1]
            self.btn15['bd'] = 2
        elif self.index == 16:
            self.btn16['bg'] = color[1]
            self.btn16['bd'] = 2
        self.btnpallet['bd'] = 2

    def btn1_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 1
        self.btn1['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn2_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 2
        self.btn2['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn3_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 3
        self.btn3['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn4_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 4
        self.btn4['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn5_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 5
        self.btn5['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn6_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 6
        self.btn6['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn7_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 7
        self.btn7['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn8_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 8
        self.btn8['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn9_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 9
        self.btn9['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn10_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 10
        self.btn10['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn11_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 11
        self.btn11['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn12_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 12
        self.btn12['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn13_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 13
        self.btn13['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn14_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 14
        self.btn14['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn15_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 15
        self.btn15['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def btn16_button(self, event):
        if self.index != 0:
            self.index_check()
        self.index = 16
        self.btn16['bd'] = 2
        Colour.fill = Colour.colordict[str(self.index)]

    def index_check(self):
        if self.index == 1:
            self.btn1['bd'] = 1
        elif self.index == 2:
            self.btn2['bd'] = 1
        elif self.index == 3:
            self.btn3['bd'] = 1
        elif self.index == 4:
            self.btn4['bd'] = 1
        elif self.index == 5:
            self.btn5['bd'] = 1
        elif self.index == 6:
            self.btn6['bd'] = 1
        elif self.index == 7:
            self.btn7['bd'] = 1
        elif self.index == 8:
            self.btn8['bd'] = 1
        elif self.index == 9:
            self.btn9['bd'] = 1
        elif self.index == 10:
            self.btn10['bd'] = 1
        elif self.index == 11:
            self.btn11['bd'] = 1
        elif self.index == 12:
            self.btn12['bd'] = 1
        elif self.index == 13:
            self.btn13['bd'] = 1
        elif self.index == 14:
            self.btn14['bd'] = 1
        elif self.index == 15:
            self.btn15['bd'] = 1
        elif self.index == 16:
            self.btn16['bd'] = 1

    def save_color(self):
        f = open("color.txt", 'w')
        json.dump(Colour.colordict, f)

    def load_color(self):
        f = open("color.txt", 'r')
        Colour.colordict = json.load(f)

class Size(Frame):
    width = 1
    def __init__(self, master=None):
        super().__init__(master)
        # self.pack()
        self.create_widget()

    def create_widget(self):
        lst = [1,2,3,4,5,6,7]
        # self.img = ImageTk.PhotoImage(Image.open('Capture2.png'))
        self.cmbsize = tkinter.ttk.Combobox(self, values=lst, width=6)
        self.cmbsize.pack()
        self.cmbsize.bind("<<ComboboxSelected>>", self.cmbsize_select)

    def cmbsize_select(self,event):
        Size.width = self.cmbsize.get()


class Tools(Frame):
    tools = 'pen'
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widget()

    def create_widget(self):
        self.btnpen = Button(self, text='pen')
        self.btneraser = Button(self, text='eraser')
        self.btntext = Button(self, text='text')
        self.btnbucket = Button(self, text='bucket')

        self.btnpen.grid(row=0, column=0)
        self.btneraser.grid(row=1, column=0)
        self.btntext.grid(row=0, column=1)
        self.btnbucket.grid(row=1, column=1)

        self.btnpen.bind('<Button-1>', self.btnpen_click)
        self.btntext.bind('<Button-1>', self.btntext_click)
        self.btneraser.bind('<Button-1>', self.btneraser_click)
        self.btnbucket.bind('<Button-1>', self.btnbucket_click)

    def btnpen_click(self, event):
        Tools.tools = 'pen'

    def btntext_click(self, event):
        Tools.tools = 'text'

    def btneraser_click(self, event):
        Tools.tools = 'eraser'

    def btnbucket_click(self, event):
        Tools.tools = 'bucket'


class Home(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widget()

    def create_widget(self):
        self.lbltools = Label(self, text='Tools')
        self.tools = Tools(self)
        self.lblsize = Label(self, text='Size')
        self.size = Size(self)
        self.lblcolor = Label(self, text='Colour')
        self.color = Colour(self)

        self.lbltools.grid(row=0, column=0)
        self.tools.grid(row=1, column=0)
        self.lblsize.grid(row=0, column=1)
        self.size.grid(row=1, column=1)
        self.lblcolor.grid(row=0, column=2)
        self.color.grid(row=1, column=2)


root = Tk()
root.title("Paint")
root.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(Image.open('icon.ico')))
#root.iconbitmap("icon.ico")
Fr_home = Home(root)
Fr_pap = Paper(root)
root.mainloop()

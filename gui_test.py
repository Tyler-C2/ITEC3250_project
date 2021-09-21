
from tkinter import *
from tkinter import ttk

# Frame is a tkinter widget that groups widgets together  

class GUI(Frame):
    def __init__(self,*args,**kwargs):
        Frame.__init__(self,*args,**kwargs)
        self.tabControl = ttk.Notebook()
        self.createTabs()
        self.tabControl.pack()

    def createTabs(self):
        inputTab = InputTab(self.tabControl)
        classTab = ClassTab(self.tabControl) 
        studentTab = StudentTab(self.tabControl) 
        self.tabControl.add(inputTab,text="Input View")
        self.tabControl.add(classTab,text="Class View")
        self.tabControl.add(studentTab,text="Student View")

class InputTab(Frame):
    def __init__(self,*args,**kwargs):
        Frame.__init__(self)
        self.button = Button(self, text= "submit", command=self.addInput)
        self.button.pack()
    
    def addInput(self):
        print("this is class view button")

class ClassTab(Frame):
    def __init__(self,*args,**kwargs):
        Frame.__init__(self)
        self.button = Button(self, text= "submit", command=self.button_test)
        self.button.pack()

    def button_test(self):
        print("this is class view button")

class StudentTab(Frame):
    def __init__(self,*args,**kwargs):
        Frame.__init__(self)
        self.button = Button(self, text= "submit", command=self.button_test)
        self.button.pack()


    def button_test(self):

        new_label = Label(self, text= "this is student view button")
        new_label.pack()
        

new_gui = GUI()
new_gui.mainloop() 


from tkinter import *
from tkinter import ttk
import course_and_student as cs

# Frame is a tkinter widget that groups widgets together  

class GUI(Frame):
    def __init__(self,*args,**kwargs):
        Frame.__init__(self,*args,**kwargs)
        self.window = args[0]
        self.window.title("Course Calculator")
        self.window.geometry("400x400")
        self.course = cs.Course()
        self.tabControl = ttk.Notebook()
        self.createTabs()
        self.tabControl.pack(expand = 1, fill=BOTH)

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
        self.input_str = StringVar()

        self.input_instruction = Label(self, text="Please enter student information in the provided text box")
        self.input_instruction.place(relx=.5,rely=.3,anchor=CENTER)

        self.input = Entry(self, width=40,textvariable=self.input_str)
        self.input.place(relx=.5,rely=.4,anchor=CENTER)

        self.button = Button(self, text= "submit", command=self.addInput)
        self.button.place(relx=.5,rely=.5,anchor=CENTER)

        self.confirm_label = Label(self, text="")
        self.confirm_label.place(relx=.5,rely=.6,anchor=CENTER)

        #
        self.test_data = [1452,89,75,64,2563,99,56,32,8546,85,75,68]
        #
    
    def addInput(self):
        entered_str = self.input_str.get()
        
        if len(entered_str) == 0:
            self.confirm_label.config(text="No input detected. Please try again.")
        else:
            for i in range(len(entered_str)):
                if not entered_str[i].isdigit() and entered_str[i] != ",":
                    self.confirm_label.config(text="Bad CSV string: Only numbers and commas allowed.")
                    return
            
            temp_name = entered_str.split(',')
            # multiple of 4?
            if int(len(temp_name)) % 4 != 0:
                self.confirm_label.config(text="Bad CSV string: List isn't a multiple of 4.")
                return

            for i in range(len(temp_name)):
                temp_name[i] = int(temp_name[i])

            nums = temp_name # replace with the inputbox after it is made a lst 
            for i in range(0,len(nums),4):
                s_lst = [nums[i],nums[i+1],nums[i+2],nums[i+3]]
                new_gui.course.create_student(s_lst)

            self.confirm_label.config(text="Student information processed.")


class ClassTab(Frame):
    def __init__(self,*args,**kwargs):
        Frame.__init__(self)
        
        self.student_instruction = Label(self, text="Please select one of the below items.")
        self.student_instruction.place(relx=.5,rely=.1,anchor=CENTER)

        self.create_radio_btns()

        self.button = Button(self, text= "submit", command=self.button_test)
        self.button.place(relx=.5,rely=.7,anchor=CENTER)

        self.course_label = Label(self, text="")
        self.course_label.place(relx=.5,rely=.8,anchor=CENTER)

    def create_radio_btns(self):
        
        self.var = IntVar()
        
        self.radio_avg = Radiobutton(self, text = "Mean",variable=self.var,value = 1)
        self.radio_avg.place( relx=.5, rely=.3, anchor=CENTER)
        self.radio_median = Radiobutton(self, text = "Median",variable=self.var,value = 2)
        self.radio_median.place( relx=.5, rely=.4, anchor=CENTER)
        self.radio_mode = Radiobutton(self, text = "Mode",variable=self.var,value = 3)
        self.radio_mode.place( relx=.5, rely=.5, anchor=CENTER)
        
    def radio_selection(self):
        active = self.var.get()
        if active == 1:
           lst = new_gui.course.course_avg()
        elif active == 2:
            lst = new_gui.course.course_median()
        elif active ==3:
            lst = new_gui.course.course_mode()
        
        return lst

    def button_test(self):
        metric_out = self.radio_selection()

        self.course_label.config(text=f"exam 1 : {metric_out[0]}, exam 2 : {metric_out[1]}, exam 3 : {metric_out[2]}")

        # print(new_gui.course.course_avg())
        # print(new_gui.course.course_median())
        # print(new_gui.course.course_mode())

class StudentTab(Frame):
    def __init__(self,*args,**kwargs):
        Frame.__init__(self)
        self.id_input = StringVar()

        self.student_instruction = Label(self, text="Please enter one students ID in the provided text box.")
        self.student_instruction.place(relx=.5,rely=.3,anchor=CENTER)
        
        self.input = Entry(self, width=40,textvariable=self.id_input)
        self.input.place(relx=.5,rely=.4,anchor=CENTER)
        
        self.button = Button(self, text="submit", command=self.button_test)
        self.button.place(relx=.5,rely=.5,anchor=CENTER)

        self.student_out_label = Label(self, text="")
        self.student_out_label.place(relx=.5,rely=.6,anchor=CENTER)

    def button_test(self):
        entered_id = self.id_input.get()
        if len(entered_id) > 0:
            try:
                id_as_int = int(entered_id) 
                student_output = new_gui.course.student_avg(id_as_int)
                if student_output == "Student not found":
                    self.student_out_label.config(text=f"{student_output} with the ID of {id_as_int} please try again.")
                else:
                    self.student_out_label.config(text=f"The average for student {id_as_int} is {student_output}.")
            except:
                not_int = entered_id
                self.student_out_label.config(text=f"could not find {not_int} please try entering the ID again.")

        

if __name__ == "__main__":
    root = Tk()
    new_gui = GUI(root)
    root.mainloop()

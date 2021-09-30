from tkinter import *
from tkinter import ttk
from ph import phTest

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Farmer GUI")
        print
        #window.geometry('300x200-5+40')

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        phTest()

        self.ph_label = Label(master, text="ph: " + phTest().ph[0] )
        self.ph_label.pack()



        ph = StringVar()
        name = ttk.Entry(master, textvariable=ph)
        name.pack()

        self.submit_button = Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()
        
        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")
        
    def submit(self):
        print("Submitted")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

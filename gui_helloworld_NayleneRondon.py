#File name: gui_helloworld_NayleneRondon.py
#Naylene Rondon
#4/10/17
#This program displays a window

import tkinter

class MyGUI:

    def __init__(self):
        """Initalize"""

        #Create the main window widget
        self.main_window = tkinter.Tk()  #Root widget

        #Create a label widget with text
        self.label1 = tkinter.Label(self.main_window, \
                                    text="Hello World!")

        self.label2 = tkinter.Label(self.main_window, \
                                    text="My first GUI program!")

        #Call the label widget pack method
        self.label1.pack(side = "top")
        self.label2.pack(side = "bottom")
        
        #Enter tkinter main loop
        tkinter.mainloop()


#Create an instance
my_gui = MyGUI()



#File name: gui_button_P2_NayleneRondon.py
#Naylene Rondon
#4/10/17
#This program displays a button

import tkinter
import time

class MyGUI:

    def __init__(self):
        """Initalize"""

        #Create the main window widget
        self.main_window = tkinter.Tk()  #Root widget

        #Create a button widget 
        self.my_button = tkinter.Button(self.main_window, \
                                    text="Click Me!")

        self.quit_button = tkinter.Button(self.main_window, \
                                    text="Quit")

        
        #Call the label widget pack method
        self.my_button.pack(side = "top")
        self.quit_button.pack(side = "bottom")

        self.my_button["command"] = self.do_something
        self.quit_button["command"] = self.do_nothing
        
        #Enter tkinter main loop
        tkinter.mainloop()

    #For the button
    def do_something(self):
        tkinter.messagebox.showinfo("You clicked!", \
        "Thank you!")

    def do_nothing(self):
        tkinter.messagebox.showinfo(">(", \
        "Fine...")




#Create an instance
my_gui = MyGUI()



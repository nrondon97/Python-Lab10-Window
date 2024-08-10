#File name: gui_button_NayleneRondon.py
#Naylene Rondon
#4/10/17
#This program displays a button

import tkinter

class MyGUI:

    def __init__(self):
        """Initalize"""

        #Create the main window widget
        self.main_window = tkinter.Tk()  #Root widget

        #Create a button widget 
        self.my_button = tkinter.Button(self.main_window, \
                                    text="Click Me!")

        self.quit_button = tkinter.Button(self.main_window, \
                                    text="Quit", \
                                          command = self.main_window.destroy)

        
        #Call the label widget pack method
        self.my_button.pack(side = "top")
        self.quit_button.pack(side = "bottom")

        self.my_button["command"] = self.do_something
        
        #Enter tkinter main loop
        tkinter.mainloop()

    #For the button
    def do_something(self):
        tkinter.messagebox.showinfo("You clicked!", \
        "Thank you!")


#Create an instance
my_gui = MyGUI()



import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog as fd

#import AI_train


#import AI_train as ai

class App:
    def __init__(self, root):
        root.title("VisionVivid")
        width=640
        height=480
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_895=tk.Label(root)
        GLabel_895["anchor"] = "nw"
        GLabel_895["bg"] = "#ff4242"
        GLabel_895["disabledforeground"] = "#ff1515"
        ft = tkFont.Font(family='Arial',size=20, weight="bold")
        GLabel_895["font"] = ft
        GLabel_895["fg"] = "#ffffff"
        GLabel_895["justify"] = "left"
        GLabel_895["text"] = "VisionVivid"
        GLabel_895["relief"] = "sunken"
        GLabel_895.place(x=0,y=0,width=640,height=480)

        GButton_203=tk.Button(root)
        GLabel_895["activebackground"] = "#b30000"
        GLabel_895["disabledforeground"] = "#ff1515"
        GButton_203["bg"] = "#cc0000"
        ft = tkFont.Font(family='Arial',size=20, weight="bold")
        GButton_203["font"] = ft
        GButton_203["fg"] = "#ffffff"
        GButton_203["justify"] = "center"
        GButton_203["text"] = "Загрузите свое изображение"
        GButton_203["relief"] = "groove"
        GButton_203.place(x=90,y=60,width=474,height=349)
        GButton_203["command"] = self.GButton_203_command

    def GButton_203_command(self):
        name = fd.askopenfilename()
        print(name[::-1][0:4][::-1])

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

from customtkinter import *
from customtkinter import filedialog as Cfd

set_appearance_mode("System")
set_default_color_theme("blue")

app = CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
def callback():
    name= Cfd.askopenfilename()
    print(name)

errmsg = 'Error!'
a = CTkButton(app, text='Click to Open File', command=callback)
a.pack()
app.mainloop()

import tkinter as tk
from tkinter import ttk

large_font = ('Verdana', 12)
masterkey='islamic'

# app baseline for adding pages
class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default='0.ico')
        tk.Tk.wm_title(self, "Sea Of BTC client")

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}


        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
#         Enter master key to access app
#             Define all variables
        heading = ttk.Label(text='Are you authorised?:')
        label = ttk.Label(text='Enter master key:')
        self.master_key = ttk.Entry(takefocus=True)
        submit = ttk.Button(text='Get Access', command=lambda: self.verify(self.master_key.get()))


#         Packing all widgets
        heading.pack()
        label.pack()
        self.master_key.pack()
        submit.pack()


    def verify(self, key):
        print(key)


app = SeaofBTCapp()
app.mainloop()

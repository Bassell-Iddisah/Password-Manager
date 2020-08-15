import tkinter as tk
from tkinter import ttk

masterkey = 'islamic'


class PasswordManager(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default='0.ico')
        tk.Tk.wm_title(self, "Password Manager")

        container = ttk.Frame(self)
        container.pack(side='top', fill='both', expand=True, )
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = HomePage(container, self)
        self.frames[HomePage] = frame
        frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):
###################################    SET THE TKINTER WINDOW TO A FIXED DIMENSION ##############################
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Define all widgets
        # The get Service and list service buttons will be removed since all available services will be already listed
        addbutton = ttk.Button(self, text='Add')
        updatebutton = ttk.Button(self, text='Update')
        deletebutton = ttk.Button(self, text='Delete')

        # pack all widgets on screen
        addbutton.pack(side='left')
        updatebutton.pack(side='left')
        deletebutton.pack(side='left')


class Services(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        heading = tk.Label(text='Services')


pas = PasswordManager()
pas.mainloop()


# def validate(key):
#     if key == masterkey:
#         pas = PasswordManager()
#         pas.mainloop()


# root = tk.Tk()
#
# master_key = ttk.Entry(root,  show='*')
# heading = tk.Label(root, text='Master Key:')
# submit = ttk.Button(root, text='submit', command=validate(master_key))
# quits = ttk.Button(root, text='Quit', command=exit)
# heading.pack()
# master_key.pack()
#
# submit.pack(side='left')
# quits.pack(side='right')
#
#
# root.mainloop()

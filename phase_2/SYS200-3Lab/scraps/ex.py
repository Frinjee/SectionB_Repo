from tkinter import *
from tkinter import font
from tkinter import ttk

root = Tk()

root.title('SYS200-3 Converter')
root.geometry('400x500')

main_frame = ttk.Frame(root)

"""Styling for:
- font
- labels
"""
cmc_sans = font.Font(family='Comic Sans MS', size=13, weight='bold')
lbl_style = ttk.Style()
lbl_style.configure('pg.TLabel', padding='7p', relief='groove', background='#8B8B88', foreground='#FFFFEB',
                     width='95p', font=cmc_sans)

# Create & configure notebook -- \n -- enable tab traversal keybindings
nb = ttk.Notebook(root)
nb.enable_traversal()

# create & add tabs to frame
pg1 = ttk.Frame(nb)
pg2 = ttk.Frame(nb)
pg3 = ttk.Frame(nb)
pg4 = ttk.Frame(nb)
pg5 = ttk.Frame(nb)

nb.add(pg1, text='dec > bin')
nb.add(pg2, text='dec > oct')
nb.add(pg3, text='dec > hex')
nb.add(pg4, text='hex > dec')
nb.add(pg5, text='bin > dec')

nb.grid(column=0, row=0)


d2b_lbl = ttk.Label(pg1, text='Decimal to Binary Converter', style='pg.TLabel')
d2b_lbl.pack()

# create entry widget for user input
d2b_entry = Entry(pg1, width=11)
d2b_entry.focus_set()

# create d2b button to submit input
d2bConv_btn = ttk.Button(pg1, text='Convert', width=15)
d2bConv_btn.pack()

# remainder will be read from bottom to top


# decimal to octal, repeated division by 8 while recording remainder.
# remainder will be read from bottom to top


# decimal to hexadecimal, repeated division by 16 while recording remainder
# remainder will be read from bottom to top


root.mainloop()

######################
### Styling Scraps
#####################
"""

"""
# root.tk.call('source', '4rst-ttk-theme/forest-dark.tcl')
# ttk.Style().theme_use('forest-dark')  # disabled styling for labels
"""
nb_style = ttk.Style()
nb_style.theme_create('sys200-nb-style', parent='alt', settings={'TNotebook': {'configure':
                                                                {'tabmargins': [1, 3, 1, 0]}},
                                                                'TNotebook.Tab': {'configure': {'padding': [5, 5]}, }})
                                                                """
# nb_style.theme_use('sys200-nb-style')

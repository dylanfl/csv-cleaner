import csv, sys
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile

win = Tk()
win.geometry("600x250")

def open():
    file = filedialog.askopenfile(mode='a', filetypes=[('Microsoft Excel Comma Separated Values File','csv')])
    file = file.read()
    df = pd.read_csv(file, delim_whitespace=True)

label = Label(win, text="Billing", font=('Georgia 13'))
label.pack(pady=10)
ttk.Button(win, text="Browse", command=open).pack(pady=20)

win.mainloop()

filename = 'file'
with open(filename, newline='') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

df = pd.read_csv('TEST.csv', header = None)
for x in df.index:
  if df.loc[x, 2] > 1:
    df.drop(x, inplace = True)


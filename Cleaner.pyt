import pandas as pd
import numpy as np
import warnings
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog as fd
from tkinter.filedialog import askopenfile
#importing all the libraries needed

warnings.simplefilter(action='ignore', category=FutureWarning)

filetypes = (
       ('Excel Files', '*.CSV'),
       ('All files', '*.*')
  )

filename = fd.askopenfilename(
      title='Open a file',
      initialdir='/',
      filetypes=filetypes)
#this allows the user to pick the file from a popup box rather than inputting the file name

df = pd.read_csv(filename, header = None, prefix = 'Column ',engine='python',dtype=str)
df=df.applymap(str)
#opens the file and reads it as a string to avoid removing 0's from start of phone numbers

print(df.info())
#prints the initial info on the csv file

for x in df.index:
  if df.loc[x, "Column 2" and "Column 3"]  == 'nan':
    df.drop(x, inplace = True)
#removes the empty rows if column 2 and 3 are nan

df=df.astype(str).replace('nan',np.nan)
#removes nan fields

df.to_csv(filename, sep=',',index=False,header=False,quoting=1)
#saves the file again


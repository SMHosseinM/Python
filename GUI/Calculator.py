try:
    import tkinter
except ImportError: # python2
    import Tkintere as tkinter

mainWindow = tkinter.Tk()
mainWindow.title('Calculator')
mainWindow.geometry('640x480')
mainWindow.minsize(width=230, height=300)
mainWindow.maxsize(width=320, height=300)

# mainWindow.columnconfigure(0, weight=1)
# mainWindow.columnconfigure(1, weight=1)
#
# mainWindow.rowconfigure(0, weight=1)
# mainWindow.rowconfigure(1, weight=1)

mainWindow['padx'] = 10
mainWindow['pady'] = 10

# Entry for displaying the result
display = tkinter.Entry(mainWindow)
display.grid(row=0, column=0, sticky='nsew')

# Making a frame to put button widgets in it
myFrame = tkinter.Frame(mainWindow)
myFrame.grid(row=1, column=0, sticky='nsew')


# A list of symbols being used in the cal
symbols = [[('C', 1), ('CE', 1)],
           [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
           [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
           [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
           [('0', 1), ('=', 2)]]

# Putting all the buttons in myFrame
row = 1
for list_ in symbols:
    column = 0
    for tuple_ in list_:
        tkinter.Button(myFrame, text=tuple_[0], width=5, height=3, padx=3, pady=2).grid(row=row, column=column, sticky='nsew', columnspan=tuple_[1])
        column += 1
    row += 1

# adding '/' to the calculator
tkinter.Button(myFrame, text='/').grid(row=5, column=3, sticky='nsew')
mainWindow.mainloop()

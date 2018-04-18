import tkinter
import os

mainWindow = tkinter.Tk()

mainWindow.title('GUI DEMO')
mainWindow.geometry('640x480+8+200')
mainWindow['padx'] = 8
mainWindow['pady'] = 8

label1 = tkinter.Label(mainWindow, text='Tkinter grid demo')
label1.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nwes', rowspan=2)
fileList.config(border=2, relief='sunken')
for zone in os.listdir('/usr/bin'):
    fileList.insert(tkinter.END, zone)

scrollbar = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
scrollbar.grid(row=1, column=1, rowspan=2, sticky='nsw')
fileList['yscrollcommand'] = scrollbar.set

# frame for te radio buttons
frame = tkinter.LabelFrame(mainWindow, text='File Details')
frame.grid(row=1, column=2, sticky='n')

rbValue = tkinter.IntVar()
rbValue.set(1)
# Radio buttons
rbButton1 = tkinter.Radiobutton(frame, text='File Name', value=1, variable=rbValue)
rbButton2 = tkinter.Radiobutton(frame, text='Path', value=2, variable=rbValue)
rbButton3 = tkinter.Radiobutton(frame, text='Time Stamp', value=3, variable=rbValue)
rbButton1.grid(row=0, column=0, sticky='w')
rbButton2.grid(row=1, column=0, sticky='w')
rbButton3.grid(row=2, column=0, sticky='w')

# Widget to display the result
resultLabel = tkinter.Label(mainWindow, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')

entry = tkinter.Entry(mainWindow)
entry.grid(row=2, column=2, sticky='sw')

# Frame for the time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')
# Time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, value=tuple(range(0,24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.LabelFrame(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.LabelFrame(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
tkinter.LabelFrame(timeFrame, text=':').grid(row=0, column=5)
timeFrame['padx'] = 36

# frame for date spinners
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')

# Date Label
dayLabel = tkinter.Label(dateFrame, text='Day')
monthLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')
# Spinners for date
daySpin = tkinter.Spinbox(dateFrame, width=4, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=4, value=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
yearSpin = tkinter.Spinbox(dateFrame, width=4, from_=2000, to=2099)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)
dateFrame['padx'] = 30

# Button widgets
okButton = tkinter.Button(mainWindow, text='OK')
okButton.grid(row=4, column=3, sticky='e')
cancelButton = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.quit)
cancelButton.grid(row=4, column=4, sticky='w')
mainWindow.mainloop()

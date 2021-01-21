import datetime
from tkinter import *
#Made by HattsonAPK
print("""
 _   _    _  _____ _____ ____   ___  _   _    _    ____  _  __
| | | |  / \|_   _|_   _/ ___| / _ \| \ | |  / \  |  _ \| |/ /
| |_| | / _ \ | |   | | \___ \| | | |  \| | / _ \ | |_) | ' / 
|  _  |/ ___ \| |   | |  ___) | |_| | |\  |/ ___ \|  __/| . \ 
|_| |_/_/   \_\_|   |_| |____/ \___/|_| \_/_/   \_\_|   |_|\_\ 
""")
note_color = '#ff9e9e'
button_color = '#69ff66'
label_color = '#9cbdc9'
today = datetime.datetime.now()
today = today.date()
file = open(f"{today}", "a+")
main = Tk()
main.title("Dayle_Program")
main.config(background='gray')


def getting(entry):
    GetText = entry.get()
    if len(GetText) == 0:
        pass
    else:
        file.write(GetText)
        file.write('\n')
        print(GetText)


label0 = Label(main, bg=label_color, text="Germany : ")
label0.grid(row=0, column=0)
entry0 = Entry(main, bg="white")
entry0.grid(row=0, column=1)
button0 = Button(main, bg=button_color, text="save", height=2, width=10, command=lambda: getting(entry0))
button0.grid(row=0, column=2)

label1 = Label(main, bg=label_color, text="Networking : ")
label1.grid(row=1, column=0)
entry1 = Entry(main, bg="white")
entry1.grid(row=1, column=1)
button1 = Button(main, bg=button_color, text="save", height=2, width=10, command=lambda: getting(entry1))
button1.grid(row=1, column=2)

label2 = Label(main, bg=label_color, text="Uni_Stuff : ")
label2.grid(row=2, column=0)
entry2 = Entry(main, bg="white")
entry2.grid(row=2, column=1)
button2 = Button(main, bg=button_color, text="save", height=2, width=10, command=lambda: getting(entry2))
button2.grid(row=2, column=2)

label3 = Label(main, bg=label_color, text="English : ")
label3.grid(row=3, column=0)
entry3 = Entry(main, bg="white")
entry3.grid(row=3, column=1)
button3 = Button(main, bg=button_color, text="save", height=2, width=10, command=lambda: getting(entry3))
button3.grid(row=3, column=2)

label4 = Label(main, bg=label_color, text="Exercise : ")
label4.grid(row=4, column=0)
entry4 = Entry(main, bg="white")
entry4.grid(row=4, column=1)
button4 = Button(main, bg=button_color, text="save", height=2, width=10, command=lambda: getting(entry4))
button4.grid(row=4, column=2)

label5 = Label(main, bg=label_color, text="PHP : ")
label5.grid(row=5, column=0)
entry5 = Entry(main, bg="white")
entry5.grid(row=5, column=1)
button5 = Button(main, bg=button_color, text="save", height=2, width=10, command=lambda: getting(entry5))
button5.grid(row=5, column=2)

label6 = Label(main, bg=label_color, text="Game_Dev : ")
label6.grid(row=6, column=0)
entry6 = Entry(main, bg="white")
entry6.grid(row=6, column=1)
button6 = Button(main, bg=button_color, text="save", height=2, width=10, command=lambda: getting(entry6))
button6.grid(row=6, column=2)

label7 = Label(main, bg=label_color, text="Web_Designing : ")
label7.grid(row=7, column=0)
entry7 = Entry(main, bg="white")
entry7.grid(row=7, column=1)
button7 = Button(main, bg=button_color, text="save", height=2, width=10, command=lambda: getting(entry7))
button7.grid(row=7, column=2)


lst = [entry0, entry1, entry2, entry3, entry4, entry5, entry6, entry7]


def saveall():
    for i in lst:
        getting(i)


label_info = Label(main, bg=note_color, text="note : write the info in format (hour:minute) ")
label_info.grid(row=8, column=0)
button_save_all = Button(main, height=2, width=25, bg=button_color, text="Save All", command=saveall)
button_save_all.grid()
main.mainloop()
file.close()

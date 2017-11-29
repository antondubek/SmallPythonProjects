"""
A program that stores book information such as:
Title
Author
Year
ISBN

User Can:
View all records
Search an entry
Add entry
Update entry
Delete
Close Application
"""

from tkinter import *
from backendoop import Database

database = Database()

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    entry_Author.delete(0, END)
    entry_Author.insert(END, selected_tuple[1])
    entry_Title.delete(0, END)
    entry_Title.insert(END, selected_tuple[2])
    entry_Year.delete(0, END)
    entry_Year.insert(END, selected_tuple[3])
    entry_ISBN.delete(0, END)
    entry_ISBN.insert(END, selected_tuple[4])

def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()):
        list1.insert(END, row)

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())


window = Tk()
window.wm_title("Book Database")

##########################################################

label_Title = Label(window, text = "Title")
label_Title.grid(row = 0, column = 0)

label_Author = Label(window, text = "Author")
label_Author.grid(row = 0, column = 2)

label_Year = Label(window, text = "Year")
label_Year.grid(row = 1, column = 0)

label_ISBN = Label(window, text = "ISBN")
label_ISBN.grid(row = 1, column = 2)

##########################################################

title_text = StringVar()
entry_Title = Entry(window, textvariable = title_text)
entry_Title.grid(row = 0, column = 1)

author_text = StringVar()
entry_Author = Entry(window, textvariable = author_text)
entry_Author.grid(row = 0, column = 3)

year_text = StringVar()
entry_Year = Entry(window, textvariable = year_text)
entry_Year.grid(row = 1, column = 1)

ISBN_text = StringVar()
entry_ISBN = Entry(window, textvariable = ISBN_text)
entry_ISBN.grid(row = 1, column = 3)

##########################################################

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

scrollBar = Scrollbar(window)
scrollBar.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = scrollBar.set)
scrollBar.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

##########################################################

button_View = Button(window, text = "View All", width = 12, command = view_command)
button_View.grid(row = 2, column = 3)

button_Search = Button(window, text = "Search Entry", width = 12, command = search_command)
button_Search.grid(row = 3, column = 3)

button_Add = Button(window, text = "Add Entry", width = 12, command = add_command)
button_Add.grid(row = 4, column = 3)

button_Update = Button(window, text = "Update", width = 12, command = update_command)
button_Update.grid(row = 5, column = 3)

button_Delete = Button(window, text = "Delete", width = 12, command = delete_command)
button_Delete.grid(row = 6, column = 3)

button_Close = Button(window, text = "Close", width = 12, command = window.destroy)
button_Close.grid(row = 7, column = 3)

##########################################################


window.mainloop()

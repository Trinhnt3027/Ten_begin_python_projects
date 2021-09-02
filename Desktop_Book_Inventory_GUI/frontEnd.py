from tkinter import *
import backEnd

# Create window and database
window = Tk()
window.title("Book Store")
backEnd.createDB()

def showDataList(listItem):
    listBook.delete(0, END)
    for item in listItem:
        listBook.insert(END, item)

def clearDataList():
    listBook.delete(0, END)

def view_viewAll():
    dataRows = backEnd.viewAll()
    showDataList(dataRows)

def view_search():
    rowData = backEnd.searchData(titleText.get(), yearText.get(), authorText.get(), isbnText.get())
    showDataList(rowData)

def view_addItem():
    backEnd.insertItem(titleText.get(), yearText.get(), authorText.get(), isbnText.get())

def view_updateItem():
    curItem = listBook.curselection()
    if (len(curItem) > 0):
        indexSelected = listBook.curselection()[0]
        backEnd.updateData(listBook.get(indexSelected)[0], en1.get(), en2.get(), en3.get(), en4.get())
        view_viewAll()

def view_deleteItem():
    curItem = listBook.curselection()
    if (len(curItem) > 0):
        indexSelected = listBook.curselection()[0]
        itemId = listBook.get(indexSelected)[0]
        backEnd.deleteData(itemId)
        view_viewAll()
        updateDataToView("", "", "", "")

def updateDataToView(title, year, author, isbn):
    en1.delete(0, END)
    en1.insert(END, title)

    en2.delete(0, END)
    en2.insert(END, author)

    en3.delete(0, END)
    en3.insert(END, year)

    en4.delete(0, END)
    en4.insert(END, isbn)

def selectedItemOfList(event):
    updateBtnsStatus()
    curItem = listBook.curselection()
    if (len(curItem) > 0):
        indexSelected = curItem[0]
        itemSelected = listBook.get(indexSelected)
        updateDataToView(itemSelected[1], itemSelected[2], itemSelected[3], itemSelected[4])

def updateBtnsStatus(*args): 
    titleEn = bool(titleText.get().strip())
    authorEn = bool(authorText.get().strip())
    yearEn = yearText.get().isdigit()
    isbnEn = isbnText.get().isdigit()
    itemSelectedEn = len(listBook.curselection()) > 0

    if (titleEn or authorEn or yearEn or isbnEn): 
        btn_Search['state'] = NORMAL
    else:
        btn_Search['state'] = DISABLED
    
    if (titleEn and authorEn and yearEn and isbnEn): 
        btn_Add['state'] = NORMAL
    else:
        btn_Add['state'] = DISABLED

    if (itemSelectedEn and titleEn and authorEn and yearEn and isbnEn): 
        btn_Update['state'] = NORMAL
    else:
        btn_Update['state'] = DISABLED

    if (itemSelectedEn):
        btn_Delete['state'] = NORMAL
    else:
        btn_Delete['state'] = DISABLED

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

titleText = StringVar()
titleText.trace_add("write", callback=updateBtnsStatus)
en1 = Entry(window, textvariable=titleText)
en1.grid(row=0, column=1)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

authorText = StringVar()
authorText.trace_add("write", callback=updateBtnsStatus)
en2 = Entry(window, textvariable=authorText)
en2.grid(row=0, column=3)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

yearText = StringVar()
yearText.trace_add("write", callback=updateBtnsStatus)
en3 = Entry(window, textvariable=yearText)
en3.grid(row=1, column=1)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

isbnText = StringVar()
isbnText.trace_add("write", callback=updateBtnsStatus)
en4 = Entry(window, textvariable=isbnText)
en4.grid(row=1, column=3)

listBook = Listbox(window, height=9, width=35)
listBook.grid(row=2, column=0, rowspan=6, columnspan=2)
listBook.bind("<<ListboxSelect>>", selectedItemOfList)

scrollBook = Scrollbar(window)
scrollBook.grid(row=2, column=2, rowspan=6)

listBook.config(yscrollcommand=scrollBook.set)
scrollBook.config(command=listBook.yview)

btn_viewAll = Button(window, text="View All", width=12, command=view_viewAll)
btn_viewAll.grid(row=2, column=3)

btn_Search = Button(window, text="Search Entry", width=12, command=view_search)
btn_Search.grid(row=3, column=3)

btn_Add = Button(window, text="Add Entry", width=12, command=view_addItem)
btn_Add.grid(row=4, column=3)

btn_Update = Button(window, text="Update", width=12, command=view_updateItem)
btn_Update.grid(row=5, column=3)

btn_Delete = Button(window, text="Delete", width=12, command=view_deleteItem)
btn_Delete.grid(row=6, column=3)

btn_Close = Button(window, text="Clear", width=12, command=clearDataList)
btn_Close.grid(row=7, column=3)

if __name__ == "__main__":
    updateBtnsStatus()

    window.mainloop()
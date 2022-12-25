from tkinter import *


class MyTodoList:
    def __init__(self, master):
        master.title("To do")

        self.my_frame = Frame(master)
        self.my_frame.config(width=300, height=200, bg="#292626")
        self.my_frame.pack()

        self.todo_label = Label(self.my_frame, text="To do List", font=("Ariel", 14, "bold"),
                                fg="#e83f3f", bg="#292626")
        self.todo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=5, sticky="W")

        self.add_item_button = Button(self.my_frame, text=" + item", font=("Ariel", 11),
                                      bg="#ed3e3e", activebackground="#ed3e3e", command=self.add_item)
        # list of entries
        self.entries = []
        # list of all text entries
        self.text_entries = []
        # list of check buttons vars
        self.var_items = []
        # list of check buttons
        self.check_buttons = []
        # list of checked entries
        self.checked_entries = []

        # the text file were we save the todo_list items
        path = "C:\\Users\\urdan\\Desktop\\To do list.txt"

        # read from file
        # number of lines = number of item we will create
        file = open(path, "r")
        self.nr_items = len(file.readlines())

        if self.nr_items == 0:
            self.add_item_button.grid(row=1, column=0, padx=10, pady=10, sticky="W", columnspan=5)
        else:
            #  create 'nr_items' check buttons and entries
            for i in range(self.nr_items):
                # every time we create a checkbutton, we create a new var
                self.var = IntVar()

                self.from_list_checkbutton = Checkbutton(self.my_frame, variable=self.var,
                                                         command=self.check_from_file_item,
                                                         bg="#292626")
                self.from_list_checkbutton.grid(row=i + 1, column=0, padx=10, pady=10, sticky="W")

                # add each var for each checkbutton to list
                self.var_items.append(self.var)
                # add each checkbutton to list
                self.check_buttons.append(self.from_list_checkbutton)

                self.from_list_entry = Entry(self.my_frame, font=("Ariel", 11), width=40)
                self.from_list_entry.grid(row=i + 1, column=1, padx=10, pady=10, sticky="W")
                # add each entry to list
                self.entries.append(self.from_list_entry)

                # the row of "add button" will change, it will be placed after all entries and check buttons
                self.add_item_button.grid(row=i + 2, column=0, padx=10, pady=10, sticky="W", columnspan=4)

        # read from file,  each line = text of the entry
        # set the text for entries
        path = "C:\\Users\\urdan\\Desktop\\To do list.txt"
        file = open(path, "r")
        # read line by line
        lines = file.readlines()
        # list of all items , without "\n"
        todo_items = [line.strip() for line in lines]
        for i in range(len(todo_items)):
            for j in range(len(self.entries)):
                # set text, for entry1-item 1, entry2-item2...
                if i == j:
                    self.entries[j].insert(0, todo_items[i])

    # delete items (added from file) if checked
    # update the text file
    def check_from_file_item(self):
        for i in range(len(self.var_items)):
            for j in range(len(self.check_buttons)):
                for k in range(len(self.entries)):
                    # if an item is checked,  destroy corresponding checkbutton and entry
                    if self.var_items[i].get() == 1 and (i == j == k):
                        self.check_buttons[j].destroy()
                        self.entries[k].destroy()
                        self.entries.remove(self.entries[k])
                        
        # add to text file the remaining items
        # get the text from remained entries
        # write the text from the list in to the text file
        path = "C:\\Users\\urdan\\Desktop\\To do list.txt"
        for j in range(len(self.entries)):
            entry_text = self.entries[j].get()
            print(entry_text)
            if entry_text not in self.checked_entries:
                self.checked_entries.append(entry_text)
            else:
                # deleting all items we delete also the one who has checked
                self.checked_entries.clear()
                # add the remaining ones
                self.checked_entries.append(entry_text)

            # write into the text file remaining items
            with open(path, "w") as todo_file:
                for text in self.checked_entries:
                    todo_file.write(text)
                    todo_file.write("\n")

    # "add item" Button
    # add new items to todo_list
    # update the text file after new items added
    def add_item(self):

        # delete the new items if checked
        # update the text file after deleting items
        def check_new_item():
            # if an item is checked,  delete corresponding checkbutton and entry
            if v.get() == 1:
                new_checkbutton.destroy()
                new_entry.destroy()
                self.entries.remove(new_entry)

                # get the text from remained entries, add it to list
                # write the text from the list in to the text file
                path = "C:\\Users\\urdan\\Desktop\\To do list.txt"
                for j in range(len(self.entries)):
                    entry_text = self.entries[j].get()
                    if entry_text not in self.checked_entries:
                        self.checked_entries.append(entry_text)
                    else:
                        # deleting all items we delete also the one who has checked
                        self.checked_entries.clear()
                        # add the remaining ones to list
                        self.checked_entries.append(entry_text)

                    # write into the text file all items from the list in new lines
                    with open(path, "w") as todo_file:
                        for text in self.checked_entries:
                            todo_file.write(text)
                            todo_file.write("\n")

        v = IntVar()
        # every time we add an item, nr_items will change
        self.nr_items += 1

        # new entries and check buttons will be placed in next rows, under existing items
        new_checkbutton = Checkbutton(self.my_frame, variable=v, command=check_new_item, bg="#292626")
        new_checkbutton.grid(row=self.nr_items + 1, column=0, padx=10, pady=10, sticky="W")

        new_entry = Entry(self.my_frame, font=("Ariel", 11), width=40)
        new_entry.grid(row=self.nr_items + 1, column=1, padx=10, pady=10, sticky="W")

        # row of add_item_button will change, he will be after all entries
        self.add_item_button.grid(row=self.nr_items + 2, column=0, padx=10, pady=10, sticky="W")

        # add new entries created to list of entries
        # write to text file new items
        for i in range(self.nr_items):
            # to avoid adding again last entry when new entry is created
            if new_entry not in self.entries:
                self.entries.append(new_entry)

                # path of the text file
                path = "C:\\Users\\urdan\\Desktop\\To do list.txt"

                # get the text from each entry, add it to list "text_entries"
                # write the text from the list in to the text file
                for ind in range(len(self.entries) - 1):
                    entry_text = self.entries[ind].get()
                    # to avoid adding again last text_entry when new entry is created
                    if entry_text not in self.text_entries:
                        # add text entry to list
                        self.text_entries.append(entry_text)
                    # write into the text file all items from the list in new lines
                    with open(path, "w") as todo_file:
                        for text in self.text_entries:
                            todo_file.write(text)
                            todo_file.write("\n")


window = Tk()
todo_list = MyTodoList(window)
window.mainloop()

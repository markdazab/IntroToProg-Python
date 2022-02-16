# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog MDaza, 02.14.2022, Updated template Code
# RRoot,1.1.2030,Created started script
# MDaza, 02.14.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print(("Task"+"\t|\t"+"Priority"))
        for row in lstTable:
            print(row["Task"]+"\t|\t"+row["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        NewTask = input("Enter name of task: ")
        NewPriority = input("Enter priority of task: [1-5] - ")
        dicRow = {"Task": NewTask, "Priority": NewPriority}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        removeChoice = input("What task would you like to remove? ")
        for row in lstTable:
            if row["Task"].lower() == removeChoice.lower():
                lstTable.remove(row)
                print("Task removed")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row["Task"]+","+row["Priority"]+"\n")
        objFile.close()
        print("Changes saved!")
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        finalChoice = input("Would you like to save your changes? ['Y' or 'N'] - ")
        if finalChoice.lower() == "y":
            objFile = open(strFile, "w")
            for row in lstTable:
                objFile.write(row["Task"] + "," + row["Priority"] + "\n")
            objFile.close()
            print("Changes saved. Good Bye")
        elif finalChoice.lower() == "n":
            print("Changes not saved. Good Bye")
        break  # and Exit the program
    else:
        print("Please enter valid value")

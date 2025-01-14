tasks = []

def addTask():
    task=input("Enter a Task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list")

def delTask():
    listTask()
    try:
        task=int(input("Enter a Task to Delete: "))
        if task in tasks:
            tasks.pop(task)
            print(f"Task '{task}' Deleted")
        else:
            print(f"Task '{task}' not Found!")
    except:
        print("Invalid Input")

def listTask():
    if not tasks:
        print("List is EMPTY")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"\tTasks {index+1}. {task}")
            

if __name__=="__main__":
    print("Welcome to the To Do List app")

    while True:
        print("\n")
        print("Please select one of the Following options!")
        print("-------------------------------------------")
        print("1. Add a new Task")
        print("2. Delete a Task")
        print("3. List Task")
        print("4. Quit")

        choice=int(input("Enter Your choice: "))

        if choice==1:
            addTask()

        elif choice==2 :
            delTask()

        elif choice==3 :
            listTask()

        elif choice==4 :
            print("Good BYE! 👋👋 ")
            break

        else:
            print("Invalid Input! Please try again...")




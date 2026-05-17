import questionary



""" 
enter notes 
view notes 
complete
delete notes


"""




l = []
while True:

    choice = questionary.select(
    "what do you want to do:",
    choices = ["add task",
    "view task",
    "delete task",
    "update task",
    "mark done",
    "exit"]
    ).ask()
    

    match choice:

        case "add task":
           task =  input("enter your task:")
           l.append(task)
           continue
        
        case "view task":
            for row in l:
                print(str(l.index(row)+1)+"." + row + "\n")

            continue

        

        case "delete task":
            delt =  int(input("enter the task number you want to delete: "))
            
            del l[delt-1]
            
            print(f"deleted {delt} task, the remaining tasks are: \n")
            for row in l:
                print(str(l.index(row)+1)+"." + row + "\n")

            pass

        case "update task":
            upd = int(input("enter the task number you want to update: "))
            text = input("enter the updated task: ")
            l[upd-1] = text
            print("task updated \n")
            pass

        case "mark done":
            comp = int(input("enter the task number which you want to mark as complete: "))
            l[comp-1] = l[comp-1] + "✓"
            
            for row in l:
                print(row + "\n")
            
        case "exit":
            break










    


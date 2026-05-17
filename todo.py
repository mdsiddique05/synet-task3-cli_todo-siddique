import questionary
import os
import time




""" 
enter notes 
view notes 
complete
delete notes


"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')




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
           print("TASK ADDED SUCCESFULLY")
           time.sleep(0.5)
           clear_screen()
           continue
        
        case "view task":
            if not l:
                print("there are no tasks, add a task to view it!!")
                print("\n")

            else :
                for row in l:
                    print(str(l.index(row)+1)+"." + row)
                
                print("\n")

            continue

        

        case "delete task":
            if not l:
                print("there are no tasks, add a task to delete it!!")
                continue

            delt = questionary.select("select the task you want to delete:",choices = l).ask()
            # delt =  int(input("enter the task number you want to delete: "))
            l.remove(delt)
            print(f"deleted the task, the remaining tasks are: \n")
            for row in l:
                print(str(l.index(row)+1)+"." + row + "\n")

            clear_screen()
            

        case "update task":

            if not l:
                print("there are no tasks, add a task to update it!!")
                continue

            upd = questionary.select("select the tasks from below to update: ",choices =l).ask()

            text = input("enter the updated task:")
             
            for i,item in enumerate(l):
                if item == upd:
                    l[i] = text
                


            
            print("task updated \n")
            pass

        case "mark done":

            if not l:
                print("there are no tasks, add a task to mark it!!")
                continue

            comp = questionary.select("select the tasks from below to mark as completed: ",choices =l).ask()

            for i,item in enumerate(l):
                if item == comp:
                    l[i] = l[i] + "✓"

                    for row in l:
                        print(row)

                    del l[i]           
            
        case "exit":
            break










    


import questionary
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    with open("data.txt", "x") as file:
        file.read()
except FileExistsError:
    pass

def load(li):
    with open("data.txt", "a") as f:
            f.write(li + "\n")

def delt():
    with open("data.txt", "r",encoding="utf-8") as f:
        lines = f.read().splitlines()
        dele = questionary.select("select what you want to delete:", choices=lines).ask()
    
    lines.remove(dele)

    with open("data.txt", "w",encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def upd():
    with open("data.txt", "r",encoding="utf-8") as f:
        lines = f.read().splitlines()
        upd = questionary.select("select what you want to update:", choices=lines).ask()
    
        text = input("enter the updated task:")
        print(lines)
                
        for i,item in enumerate(lines):
            if item == upd:
                lines[i] = text
    

    with open("data.txt", "w",encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


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
           load(task)
           print("TASK ADDED SUCCESFULLY")
           time.sleep(0.5)
           clear_screen()
           continue
        
        case "view task":
            clear_screen()
            
            with open("data.txt", "r",encoding="utf-8") as f:
                for i,line in enumerate(f):
                    print(i+1,".",line.strip())

            continue

        

        case "delete task":
            delt()
            # if not l:
            #     print("there are no tasks, add a task to delete it!!")
            #     continue

            # delt = questionary.select("select the task you want to delete:",choices = l).ask()
            # # delt =  int(input("enter the task number you want to delete: "))
            # l.remove(delt)
            # print(f"deleted the task, the remaining tasks are: \n")
            # for row in l:
            #     print(str(l.index(row)+1)+"." + row + "\n")

            clear_screen()
            print("XXXXXXXXX-----TASK DELETED-----XXXXXXXXX")
            

        case "update task":
            

            upd()

            # if not l:
            #     print("there are no tasks, add a task to update it!!")
            #     continue

            # upd = questionary.select("select the tasks from below to update: ",choices =l).ask()

            # text = input("enter the updated task:")
             
            # for i,item in enumerate(l):
            #     if item == upd:
            #         l[i] = text
                


            
            print("task updated \n")
            pass

        case "mark done":

            # if not l:
            #     print("there are no tasks, add a task to mark it!!")
            #     continue

            with open("data.txt", "r",encoding="utf-8") as f:
                
                lines = f.read().splitlines()
                comp = questionary.select("select the tasks from below to mark as completed: ",choices = lines).ask()

            for i,item in enumerate(lines):
                if item == comp:
                    lines[i] = lines[i] + "✓"

            with open("data.txt","w",encoding="utf-8") as f:
                for line in lines:
                    f.write(line + "\n")
                         
            
        case "exit":
            break










    


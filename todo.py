""" 
enter notes 
view notes 
complete
delete notes


"""




l = []
while True:

    try:

        i = int(input('''
                    
                    
                    enter what you want to do: 
    1. add task
    2.view task
    3.delete task
    4. update task
    5. mark done
    6. break 
                    
                    
                    '''))
    
    except ValueError:
        print("enter the correct number.")
        continue
    
    match i:

        case 1:
           task =  input("enter your task:")
           l.append(task)
           continue
        
        case 2:
            for row in l:
                print(str(l.index(row)+1)+"." + row + "\n")

            continue

        

        case 3:
            delt =  int(input("enter the task number you want to delete: "))
            
            del l[delt-1]
            
            print(f"deleted {delt} task, the remaining tasks are: \n")
            for row in l:
                print(str(l.index(row)+1)+"." + row + "\n")

            pass

        case 4:
            upd = int(input("enter the task number you want to update: "))
            text = input("enter the updated task: ")
            l[upd-1] = text
            print("task updated \n")
            pass

        case 5:
            comp = int(input("enter the task number which you want to mark as complete: "))
            l[comp-1] = l[comp-1] + "✓"
            
            for row in l:
                print(row + "\n")
            
        case 6:
            break










    




to_do_list = ["paper"]

while(True):
    to_do = input("Enter your to-do list add, remove, view, or exit: ").lower()
    if to_do == "add":
        to_do_list.append(input("Enter the task you want to add: "))
        print(f"Task added successfully. {to_do_list}")
        
    elif to_do == "remove":
        if not to_do_list:
            print("Your to-do list is empty.")
        else:
            task_to_remove = input("Enter the task you want to remove: ")
            if task_to_remove in to_do_list:
                to_do_list.remove(task_to_remove)
                print(f"Task removed successfully. {to_do_list}")
            else:
                print("Task not found in the list.")

    elif to_do == "view":
        if not to_do_list:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for task in to_do_list:
                print(task)
            
    elif to_do == "exit":
        print("Exiting the program.")
        break

    else:
        print("Invalid input. Please enter 'add', 'remove', 'view', or 'exit'.")
        
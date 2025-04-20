def add_task(to_do_list):
    task_to_add = input("Enter the task you want to add: ")
    if task_to_add.strip() != "":  # التأكد من أن المستخدم لا يضيف مهمة فارغة
        to_do_list.append(task_to_add)
        print(f"Task '{task_to_add}' added successfully.")
    else:
        print("You cannot add an empty task.")

def remove_task(to_do_list):
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        task_to_remove = input("Enter the task you want to remove: ")
        if task_to_remove in to_do_list:
            to_do_list.remove(task_to_remove)
            print(f"Task '{task_to_remove}' removed successfully.")
        else:
            print(f"Task '{task_to_remove}' not found in the list.")

def view_tasks(to_do_list):
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for task in to_do_list:
            print(f"- {task}")

def main():
    to_do_list = ["paper"]

    while True:
        to_do = input("Enter your to-do list add, remove, view, or exit: ").lower()

        if to_do == "add":
            add_task(to_do_list)

        elif to_do == "remove":
            remove_task(to_do_list)

        elif to_do == "view":
            view_tasks(to_do_list)

        elif to_do == "exit":
            print("Exiting the program.")
            break

        else:
            print("Invalid input. Please enter 'add', 'remove', 'view', or 'exit'.")

# استدعاء الدالة الرئيسية
main()

#First Version

# todoList = []

# while True:
#     print("\nTo Do List")
#     print("\n(1) Add Task")
#     print("\n(2) View Tasks")
#     print("\n(3) Remove Task")
#     print("\n(4) Exit")

#     todo = input("Choose from 1 to 4: ")

#     if todo == '1':
#         addTask = input("Enter the task you want to add!: ")
#         todoList.append(addTask)

#     elif todo == '2':
#         print(todoList)

#     elif todo == '3':
#         if todoList:
#             removeTask = input("Enter the task you want to delete")
#             if removeTask in todoList:
#                 todoList.pop(removeTask)
#                 print(f"Task remove: {removeTask}")

#     elif todo == '4':
#         print("Thanks you for using this app!")
#         break

#     else: 
#         print("You can only enter number from 1 to 4")


#Second version
todoList = []

while True:
    print("\n🔹 To-Do List 🔹")
    print("(1) Add Task")
    print("(2) View Tasks")
    print("(3) Remove Task")
    print("(4) Exit")

    todo = input("Choose from 1 to 4: ")

    if todo == '1':  # Add task
        addTask = input("Enter the task you want to add: ")
        todoList.append(addTask)
        print(f"✅ Task added: {addTask}")

    elif todo == '2':  # View tasks
        if todoList:
            print("\n📝 Your Tasks:")
            for i, task in enumerate(todoList, 1):
                print(f"{i}. {task}")
        else:
            print("📌 No tasks added yet!")

    elif todo == '3':  # Remove task
        if todoList:
            print("\n 📃 Your Tasks: ")
            for i, task in enumerate(todoList, 1):
                print(f"{i}. {task}")

        try:
            removeTask = int(input("Enter the number you want to remove:"))
            if 1 <= removeTask <= len(todoList):
                remove_task = todoList.pop(removeTask - 1)
                print(f"❌ Task removed: {removeTask}")
            else:
                print("⚠️ Invalid task number!")
        except ValueError:        
            print("⚠️ Please enter a valid number!")
        else:
            print("📌 No tasks to remove!")

    elif todo == '4':  # Exit
        print("✅ Thank you for using the To-Do List! Goodbye! 😊")
        break

    else:
        print("❌ Invalid choice! Please enter a number between 1 and 4.")

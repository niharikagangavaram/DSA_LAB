stack = []
max_size = int(input("Enter stack size: "))

def push():
    if len(stack) == max_size:
        print("Stack Overflow")
    else:
        element = int(input("Enter element: "))
        stack.append(element)
        print("Element pushed successfully")

def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print("Popped element:", stack.pop())

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:", stack[::-1])

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")

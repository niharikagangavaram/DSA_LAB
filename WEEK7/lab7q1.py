queue = []
max_size = int(input("Enter queue size: "))

while True:
    print("menu")
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(queue) == max_size:
            print("Queue Overflow")
        else:
            data = int(input("Enter element: "))
            queue.append(data)
            print("Element inserted")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue Underflow")
        else:
            print("Deleted element:", queue.pop(0))

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", queue[0])

    elif choice == 4:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Queue:", queue)

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")

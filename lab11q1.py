size = 10

# Separate Chaining
def separate_chaining(keys):
    table = [[] for i in range(size)]

    for key in keys:
        index = key % size
        table[index].append(key)

    print("Separate Chaining:")
    for i in range(size):
        print(i, ":", table[i])


# Linear Probing
def linear_probing(keys):
    table = [None] * size

    for key in keys:
        index = key % size

        while table[index] is not None:
            index = (index + 1) % size

        table[index] = key

    print("Linear Probing:")
    print(table)


# Quadratic Probing
def quadratic_probing(keys):
    table = [None] * size

    for key in keys:
        index = key % size
        i = 0

        while i < size and table[(index + i*i) % size] is not None:
            i += 1

        if i < size:
            table[(index + i*i) % size] = key
        else:
            print("Hash table is full for", key)

    print("Quadratic Probing:")
    print(table)


while True:
    print("\n1. Separate Chaining")
    print("2. Linear Probing")
    print("3. Quadratic Probing")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        break

    n = int(input("Enter number of elements: "))
    keys = []

    for i in range(n):
        keys.append(int(input("Enter element: ")))

    if choice == 1:
        separate_chaining(keys)
    elif choice == 2:
        linear_probing(keys)
    elif choice == 3:
        quadratic_probing(keys)
    else:
        print("Invalid choice")

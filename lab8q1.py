
class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    def insert(self, value, index=0):
        if index >= self.size:
            print("Tree is full")
            return

        if self.tree[index] is None:
            self.tree[index] = value
            print("Node inserted")
        else:
            print("Position already occupied")

    def delete(self, value):
        if value in self.tree:
            index = self.tree.index(value)
            self.tree[index] = None
            print("Node deleted")
        else:
            print("Node not found")

    def display(self):
        print("Binary Tree:", self.tree)

    def inorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.inorder(2 * i + 1)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 2)

    def preorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    def postorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.postorder(2 * i + 1)
            self.postorder(2 * i + 2)
            print(self.tree[i], end=" ")


# Main Program
bt = BinaryTree(10)

while True:
    print("\n1.Insert")
    print("2.Delete")
    print("3.Display")
    print("4.Inorder")
    print("5.Preorder")
    print("6.Postorder")
    print("7.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        value = int(input("Enter value: "))
        bt.insert(value)

    elif ch == 2:
        value = int(input("Enter value to delete: "))
        bt.delete(value)

    elif ch == 3:
        bt.display()

    elif ch == 4:
        bt.inorder()
        print()

    elif ch == 5:
        bt.preorder()
        print()

    elif ch == 6:
        bt.postorder()
        print()

    elif ch == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice")

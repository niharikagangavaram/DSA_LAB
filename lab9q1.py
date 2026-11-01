class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    def search(self, root, key):
        if root is None or root.data == key:
            return root

        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, key):
        if root is None:
            return None

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root


bst = BST()

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Inorder")
    print("5. Preorder")
    print("6. Postorder")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter element: "))
        bst.root = bst.insert(bst.root, data)

    elif choice == 2:
        key = int(input("Enter element to search: "))
        if bst.search(bst.root, key):
            print("Element found")
        else:
            print("Element not found")

    elif choice == 3:
        key = int(input("Enter element to delete: "))
        bst.root = bst.delete(bst.root, key)
        print("Deletion completed")

    elif choice == 4:
        bst.inorder(bst.root)
        print()

    elif choice == 5:
        bst.preorder(bst.root)
        print()

    elif choice == 6:
        bst.postorder(bst.root)
        print()

    elif choice == 7:
        break

    else:
        print("Invalid choice")

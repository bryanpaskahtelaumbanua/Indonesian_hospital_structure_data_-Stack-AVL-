import pandas as pd

data = pd.read_csv(
    'C://Users//Bryan//OneDrive - Institut Teknologi Sumatera//TUBES_STRUKDAT//Hospital_Indonesia_Cleaned.csv'
)

class HospitalNode:
    def __init__(self, hospital_data):
        self.key = hospital_data['hospital_id']
        self.data = hospital_data

        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, root):
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, hospital_data):
        key = hospital_data['hospital_id']

        if root is None:
            return HospitalNode(hospital_data)

        if key < root.key:
            root.left = self.insert(root.left, hospital_data)
        elif key > root.key:
            root.right = self.insert(root.right, hospital_data)
        else:
            print(f"Hospital ID {key} sudah ada.")
            return root

        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right)
        )

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, hospital_id):
        if root is None:
            return None

        if hospital_id == root.key:
            return root.data

        if hospital_id < root.key:
            return self.search(root.left, hospital_id)

        return self.search(root.right, hospital_id)

    def get_min_value_node(self, root):
        current = root

        while current.left is not None:
            current = current.left

        return current


    def delete(self, root, hospital_id):
        if root is None:
            return root

        if hospital_id < root.key:
            root.left = self.delete(root.left, hospital_id)

        elif hospital_id > root.key:
            root.right = self.delete(root.right, hospital_id)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.get_min_value_node(root.right)

            root.key = temp.key
            root.data = temp.data

            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right)
        )

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def update(self, root, hospital_id, updated_data):
        node_data = self.search(root, hospital_id)

        if node_data is None:
            return False

        updated_data['hospital_id'] = hospital_id
        node_data.update(updated_data)

        return True

    def inorder(self, root, result=None):
        if result is None:
            result = []

        if root:
            self.inorder(root.left, result)
            result.append(root.data)
            self.inorder(root.right, result)

        return result

    def postorder(self, root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.key, end=" ")   

    def preorder(self, root):
        if root is None:
            return

        print(root.key, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def print_tree(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.key))
            self.print_tree(root.left, level + 1, "L--- ")
            self.print_tree(root.right, level + 1, "R--- ")

avl = AVLTree()
root = None

for _, row in data.iterrows():
    hospital_data = row.to_dict()
    root = avl.insert(root, hospital_data)

print("\nAVL Tree berhasil dibangun!")
print("Jumlah data:", len(data))
print("Root AVL:", root.key)
print("Tinggi AVL:", root.height)

def search_by_name(data, keyword):
    result = data[
        data['hospital_name']
        .str.contains(keyword, case=False, na=False)
    ]

    return result


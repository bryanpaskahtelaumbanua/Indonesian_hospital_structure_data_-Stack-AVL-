# =========================================
# STACK HISTORY UNTUK UNDO AVL TREE
# =========================================

class Stack:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.items = []

    # =====================================
    # CHECK EMPTY
    # =====================================
    def is_empty(self):
        return len(self.items) == 0

    # =====================================
    # CHECK FULL
    # =====================================
    def is_full(self):
        return len(self.items) == self.capacity

    # =====================================
    # PUSH
    # =====================================
    def push(self, item):
        if self.is_full():
            raise OverflowError("Stack is full")

        self.items.append(item)

    # =====================================
    # POP
    # =====================================
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")

        return self.items.pop()

    # =====================================
    # PEEK
    # =====================================
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")

        return self.items[-1]

    # =====================================
    # SIZE
    # =====================================
    def size(self):
        return len(self.items)

    # =====================================
    # DISPLAY STACK
    # =====================================
    def display(self):
        if self.is_empty():
            print("Stack kosong")
            return

        print("\nIsi Stack (Top -> Bottom):")

        for item in reversed(self.items):
            print(item)

if __name__ == "__main__":

    history_stack = Stack(10)

    # PUSH OPERATION
    history_stack.push({
        "operation": "INSERT",
        "hospital_id": 1110053
    })

    history_stack.push({
        "operation": "DELETE",
        "hospital_id": 1106014
    })

    # DISPLAY
    history_stack.display()

    # PEEK
    print("\nTop Stack:")
    print(history_stack.peek())

    # POP
    last_operation = history_stack.pop()

    print("\nData yang di-pop:")
    print(last_operation)

    print("\nIsi stack setelah pop:")
    history_stack.display()
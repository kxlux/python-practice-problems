from typing import Optional

class Empty:

    def __init__(self):
        # nothing to do!
        pass

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())
    
    def inorder(self) -> list[int]:
        if self.is_empty():
            return []
        return self.left.inorder() + [self.value] + self.right.inorder()
    
    def min_item(self) -> Optional[int]:
        if self.is_empty():
            return None
        if self.left.is_empty():
            return self.value
        return self.left.min_item()
    
    def max_item(self) -> Optional[int]:
        if self.is_empty():
            return None
        if self.right.is_empty():
            return self.value
        return self.right.max_item()
    
    def balance_factor(self) -> Optional[int]:
        if self.is_empty():
            return None
        return self.right.height() - self.left.height()
    
    def balanced_everywhere(self) -> bool:
        if self.is_empty():
            return True
        if -1 <= self.balance_factor() <= 1:
            return (self.left.balanced_everywhere() and 
                    self.right.balanced_everywhere())
        return False
    
    def add_to_all(self, n: int):
        if self.is_empty():
            return Empty()
        return Node(self.value + n, self.left.add_to_all(n),
                    self.right.add_to_all(n))
    
    def path_to(self, n: int) -> Optional[int]:
        if self.is_empty():
            return None
        path = [self.value]
        if self.value == n:
            return path
        elif n < self.value:
            if self.left.path_to(n) is not None:
                return path.append(self.left.path_to(n))
        else:
            if self.right.path_to(n) is not None:
                return path.append(self.right.path_to(n))
    
    def __str__(self) -> str:
        return "Empty"


class Node:

    def __init__(self, n, left, right):
        self.value = n
        self.left = left
        self.right = right

    def is_empty(self):
        return False

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty()

    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def contains(self, n):
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def insert(self, n):
        if n < self.value:
            return Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return Node(self.value, self.left, self.right.insert(n))
        else:
            return self

    def inorder(self) -> list[int]:
        if self.is_empty():
            return []
        return self.left.inorder() + [self.value] + self.right.inorder()
    
    def min_item(self) -> Optional[int]:
        if self.is_empty():
            return None
        if self.left.is_empty():
            return self.value
        return self.left.min_item()
    
    def max_item(self) -> Optional[int]:
        if self.is_empty():
            return None
        if self.right.is_empty():
            return self.value
        return self.right.max_item()
    
    def balance_factor(self) -> Optional[int]:
        if self.is_empty():
            return None
        return self.right.height() - self.left.height()
    
    def balanced_everywhere(self) -> bool:
        if self.is_empty():
            return True
        if -1 <= self.balance_factor() <= 1:
            return (self.left.balanced_everywhere() and 
                    self.right.balanced_everywhere())
        return False
    
    def add_to_all(self, n: int):
        if self.is_empty():
            return Empty()
        return Node(self.value + n, self.left.add_to_all(n),
                    self.right.add_to_all(n))
    
    def path_to(self, n: int) -> Optional[int]:
        if self.is_empty():
            return None
        path = [self.value]
        if self.value == n:
            return path
        elif n < self.value:
            if self.left.path_to(n) is not None:
                path += self.left.path_to(n)
                return path
        else:
            if self.right.path_to(n) is not None:
                path += self.right.path_to(n)
                return path
    
    def __str__(self) -> str:
        return f"({str(self.left)}) {self.value} ({str(self.right)})"

if __name__ == "__main__":
    bst = Empty().insert(3).insert(2).insert(1).insert(0).insert(4).insert(5)

    print(f"The number of nodes is {bst.num_nodes()}")
    print(f"The height is {bst.height()}")
    print(f"Items in order is {bst.inorder()}")
    print(f"min item is {bst.min_item()}")
    print(f"max item is {bst.max_item()}")
    print(f"BF is {bst.balance_factor()}")
    print(f"BST is balanced everywhere: {bst.balanced_everywhere()}")
    print(f"add one to all {bst.add_to_all(1)}")
    print(f"bst:\n{bst}")
    print(f"path to 0: {bst.path_to(0)}")
    print(f"path to 8: {bst.path_to(8)}")

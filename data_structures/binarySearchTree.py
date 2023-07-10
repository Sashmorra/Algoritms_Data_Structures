class Tree:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = self.right = None

    def insert(self, data):
        if self.data > data:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.insert(data)

    def getMax(self):
        if self.right is None:
            return self.data
        return self.right.getMax()

    def getMin(self):
        if self.left is None:
            return self.data
        return self.left.getMin()


if __name__ == "__main__":
    test = Tree(5)
    test.insert(10)
    test.insert(2)
    test.insert(15)
    test.insert(3)
    print(test.getMax())
    print(test.getMin())

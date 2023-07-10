class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = Node()

    def top(self):
        return self.top.data

    def size(self):
        count = 0
        node = self.top
        while node != None:
            count += 1
            node = node.next
        print(count)
        return count

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        self.top = self.top.next

    def display(self):
        answer = []
        node = self.top
        while node.data != None:
            answer.append(node.data)
            node = node.next
        print(answer)


if __name__ == "__main__":
    test = Stack()
    test.push(1)
    test.push(2)
    test.push(3)
    test.display()
    test.pop()
    test.size()
    test.display()

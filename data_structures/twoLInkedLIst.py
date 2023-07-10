class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        self.prev = None


class OneLinkedList:
    def __init__(self) -> None:
        self.head = self.tail = Node()

    def push_back(self, data):
        node = Node(data)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        if self.head.data == None:
            self.head = node

    def push_front(self, data):
        node = Node(data)
        self.head.prev = node
        node.next = self.head
        self.head = node
        self.head.prev = None

    def pop_front(self):
        node = self.head.next
        node.prev = None
        self.head = self.head.next
        self.head = node

    def pop_back(self):
        node = self.tail.prev
        node.next = None
        self.tail = node

    def display(self):
        answer = []
        node = self.head
        while node != None:
            answer.append(node.data)
            node = node.next
        print(answer)


if __name__ == "__main__":
    test = OneLinkedList()
    test.push_back(1)
    test.push_back(2)
    test.push_back(3)
    test.display()
    test.push_front(6)
    test.display()
    test.pop_back()
    test.display()
    test.pop_front()
    test.display()

class Node {
  constructor(data = null) {
    this.data = data;
    this.next = null;
  }
}
class OneLInkedList {
  constructor() {
    this.head = this.tail = new Node();
  }
  push_back(data) {
    let node = new Node(data);
    this.tail.next = node;
    this.tail = node;
    if (this.head.data === null) {
      this.head = node;
    }
  }
  push_front(data) {
    let node = new Node(data);
    node.next = this.head;
    this.head = node;
  }
  pop_back() {
    let node = this.head;
    while (node.next !== this.tail) {
      node = node.next;
    }
    this.tail = node;
    this.tail.next = null;
  }
  pop_front() {
    this.head = this.head.next;
  }
  display() {
    let answer = [];
    let node = this.head;
    while (node !== null) {
      answer.push(node.data);
      node = node.next;
    }
    console.log(answer);
  }
}

test = new OneLInkedList();
test.push_back(1);
test.push_back(2);
test.push_back(3);
test.display();
test.push_front(6);
test.display();
test.pop_back();
test.display();
test.pop_front();
test.display();

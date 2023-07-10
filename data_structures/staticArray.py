class Static_Array:
    def __init__(self, number_of_elements, elemens_type: type) -> None:
        self.value = [0] * number_of_elements
        self.elemens_type = elemens_type
        self.k = 0
        # k - actual value counter

    def push_back(self, data):
        if type(data) is self.elemens_type:
            if self.value[-1] == 0:
                self.value[self.k] = data
                self.k += 1
            else:
                print("Memory is over")
        else:
            print("Data of unspecified type")

    def push_front(self, data):
        if type(data) is self.elemens_type:
            if self.value[-1] == 0:
                first_null = self.value.index(0)
                data_from_array = self.value[:first_null]
                lenght_array = len(self.value)
                self.value = [0] + data_from_array + [0] * \
                    (lenght_array - 1 - len(data_from_array))
                self.value[0] = data
                self.k += 1
            else:
                print("Memory is over")
        else:
            print("Data of unspecified type")

    def pop_front(self):
        self.value[self.k-1] = 0
        self.k -= 1

    def pop_back(self):
        data_from_array = self.value[1:]
        lenght_array = len(self.value)
        self.value = data_from_array + [0] * \
            (lenght_array - len(data_from_array))
        self.k -= 1

    def display(self) -> str:
        print(self.value)
        return self.value

    def read(self, index):
        print(self.value[index])
        return self.value[index]


if __name__ == "__main__":
    test = Static_Array(6, int)
    test.push_back(1)
    test.display()
    test.push_front(2)
    test.display()
    test.read(1)
    test.pop_back()
    test.display()
    test.pop_front()
    test.display()

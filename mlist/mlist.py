class MLista:

    def __init__(self, capacity):
        self._capacity = capacity
        self._list = []

    def write(self):
        print("Rozmiar listy: ", self.get_length())
        print("Pojemnosc listy: ", self.get_capacity())
        print("Elementy: ", self._list)

    def add_element(self, element):
        if len(self._list) < self._capacity:
            self._list.append(element)
            return True
        return False

    def get_index(self, element):
        for my_element in self._list:
            if my_element == element:
                return self._list.index(element)
        return -1

    def get_element(self, index):
        if index < 0 or index > len(self._list) - 1:
            return -1
        return self._list[index]

    def get_length(self):
        return len(self._list)

    def get_capacity(self):
        return self._capacity

    def remove_duplicates(self, element):
        count = 0
        new_list = []
        for my_element in self._list:
            if my_element == element:
                if count == 0:
                    new_list.append(my_element)
                    count += 1
            else:
                new_list.append(my_element)
        self._list = new_list
        return self._list

    def reverse(self):
        self._list = list(reversed(self._list))
        return self._list

    def increase_capacity(self, value):
        if value > 0:
            self._capacity += value
            return True
        return False

    def reduce_capacity(self, value):
        if value > 0 and self._capacity - value >= len(self._list):
            self._capacity -= value
            return True
        return False

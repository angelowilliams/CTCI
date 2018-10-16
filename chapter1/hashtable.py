class HashTable():
    def __init__(self, size):
        self.amount_of_lists = size
        self.keys = [[] for i in range(self.amount_of_lists)]
        self.values = [[] for i in range(self.amount_of_lists)]

    def hash_function(self, key):
        sumOfChars = 0
        for char in key:
            sumOfChars += ord(char)
        return sumOfChars % self.amount_of_lists

    def put(self, key, value):
        index = self.hash_function(key)
        self.keys[index].append(key)
        self.values[index].append(value)
        return

    def get(self, key):
        index = self.hash_function(key)
        print(self.keys[index])
        try:
            sublist_index = self.keys[index].index(key)
        except ValueError:
            sublist_index = -1
        if sublist_index == -1:
            return False
        else:
            return self.values[index][sublist_index]

    def size(self):
        sum = 0
        for list in self.keys:
            for item in list:
                sum += 1
        return sum

    def is_empty(self):
        return self.size() == 0

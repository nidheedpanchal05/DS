## Practical 3(A)
'''
Perform stack operations using
Array implementation
'''

class ArrayStack:
    
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        if self.__len__() == 0:
            return True
        else:
            return False

    def push(self,value):
        self._data.append(value)

    def pop(self):
        if self.__len__() == 0:
            return 'Empty list'
        self._data.pop()

    def top(self):
        if self.__len__() == 0:
            return 'Empty list'
        return self._data[0]


obj = ArrayStack()
print("List: ",obj._data)
print("Size: ",obj.__len__())
print("Top: ",obj.top())
print("List is Empty: ",obj.is_empty())
print("\n-------Push 5 elements--------")
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
print("List: ",obj._data)
print("Size: ",obj.__len__())
print("Top: ",obj.top())
print("List is Empty: ",obj.is_empty())
print("\n-------Pop 3 elements--------")
obj.pop()
obj.pop()
obj.pop()
print("List: ",obj._data)
print("Size: ",obj.__len__())
print("Top: ",obj.top())
print("List is Empty: ",obj.is_empty())











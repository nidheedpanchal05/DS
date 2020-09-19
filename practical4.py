## Practical 4
'''
Queue operations using circular array implementation
-Circular array
-Replace removed element by None
-Then add new ones at the beginning and replace None
'''

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def len(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1)%(len(self._data))
        self._size -= 1
        return answer

    def enqueue(self,value):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = value
        self._size += 1


    def _resize(self,cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk)%len(old)
        self._front = 0
            

list_obj = ArrayQueue()
print("Size: ",list_obj.len())
print("List is empty: ",list_obj.is_empty())
print("\n--------------Enqueue------------------")
list_obj.enqueue(1)
list_obj.enqueue(2)
list_obj.enqueue(3)
list_obj.enqueue(4)
list_obj.enqueue(5)
list_obj.enqueue(6)
list_obj.enqueue(7)
list_obj.enqueue(8)
list_obj.enqueue(9)
list_obj.enqueue(10)
print(list_obj._data)
print("\n--------------Denqueue------------------")
list_obj.dequeue()
list_obj.dequeue()
list_obj.dequeue()
print(list_obj._data)
print("\n--------------Enqueue------------------")
list_obj.enqueue(11)
list_obj.enqueue(12)
list_obj.enqueue(13)
print(list_obj._data)
print("\nSize: ",list_obj.len())
print("List is empty: ",list_obj.is_empty())






        
    
    

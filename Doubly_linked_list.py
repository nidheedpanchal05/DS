class Node():
    def __init__(self, data, Next = None, Previous = None):
        self.data = data
        self.next = Next
        self.previous = Previous
    def display(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_head(self, data):
        newNode = Node(data)
        if self.head:
            self.head.setPrevious(newNode)
        newNode.setNext(self.head)
        self.head = newNode
        self.size = self.size+1

    def add_tail(self, data):
        newNode = Node(data)
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(newNode)
        newNode.setPrevious(current)
        self.size = self.size+1

    def remove_head(self):
        if self.is_empty():
            print("Empty Singly linked list")
        else:
            print("Removing")
            self.head = self.head.next
            self.head.previous = None
            self.size -= 1
        
    def get_tail(self):
        last_object = self.head
        while (last_object.next != None):
            last_object = last_object.next
        return last_object

    def get_node_at(self,index):
        element_node = self.head
        counter = 0
        if index > self.size-1:
            print("Index out of bound")
            return None
        while(counter < index):
            element_node = element_node.next
            counter += 1
        return element_node

    def get_prev_node(self,pos):
        if pos == 0:
            print('No previous elements')
        return self.get_node_at(pos).previous
        

    def remove_between_list(self,position):
        if position > self.size-1:
            print("Index out of bound")
        elif position == self.size-1:
            self.remove_tail()
        elif position == 0:
            self.remove_head()
        else:
            prev_node = self.get_node_at(position-1)
            next_node = self.get_node_at(position+1)
            prev_node.next = next_node
            self.size -= 1

    def display_all(self):
        if self.size == 0:
            print("No element")
            return False
        first = self.head
        print(first.data)
        first = first.next
        while first:
            
            print(first.data)
            first = first.next

    

    def find_second_last_element(self):
        #second_last_element = None
        if self.size >= 2:
            first = self.head 
            temp_counter = self.size-2
            while temp_counter > 0:
                first = first.next 
                temp_counter -= 1 
            return first
        
        
        else:
            print("Size not sufficient")

    def remove_tail(self):
        if self.is_empty():
            print("Empty Singly linked list")
        elif self.size == 1:
            self.head == None
            self.size -= 1
        else: 
            Node = self.find_second_last_element()
            if Node:
                Node.next = None
                self.size -= 1

    def add_between_list(self,position,element):
        element_node = Node(element)
        if position > self.size:
            print("Index out of bound")
        elif position == self.size:
            self.add_tail(element)
        elif position == 0:
            self.add_head(element)
        else:
            prev_node = self.get_node_at(position-1)
            current_node = self.get_node_at(position)
            prev_node.next = element_node
            element_node.previous = prev_node
            element_node.next = current_node
            self.size += 1

    def search(self,search_value):
        index = 0 
        while (index < self.size):
            value = self.get_node_at(index)
            print("Searching at " + str(index) + " and value is " + str(value.data))
            if value.data == search_value:
                print("Found value at " + str(index) + " location")
                return True
            index += 1
        print("Not Found")
        return False
    
    def merge(self,linkedlist_value):
        if self.size > 0:
            last_node = self.get_node_at(self.size-1)
            last_node.next = linkedlist_value.head
            self.size = self.size + linkedlist_value.size
            
        else:
            self.head = linkedlist_value.head
            self.size = linkedlist_value.size


            
    
def pattern(list_name):
    for i in range(5):
        for j in range(13):
            if(i==0 or i==4 or j==0 or j==12):
                print('****', end="**")
            else:
                if j==6 and i==2:
                    print(list_name, end="  ")
                else:
                    print('    ', end="  ")
        print()

pattern('lst1')
print()
lst1 = DoublyLinkedList()
print("List is empty => ",lst1.is_empty())
print("---------------add head--------------")
lst1.add_head("a")
lst1.add_head("b")
lst1.add_head("c")
print("---------------add tail--------------")
lst1.add_tail("d")
lst1.add_tail("e")
lst1.add_tail("f")
lst1.add_tail("g")
lst1.display_all()
print("\n------------remove head------------")
lst1.remove_head()
lst1.display_all()
print("List is empty => ",lst1.is_empty())
print("Size => ",lst1.size)
print("Head => ",lst1.head.display())
print("Tail => ",lst1.get_tail().display())
print("Second last => ",lst1.find_second_last_element().display())
print("\n------------remove tail------------")
lst1.remove_tail()
lst1.display_all()
print("\nget node at pos 2 => ",lst1.get_node_at(2).display())
print("get previous node at pos 1 => ",lst1.get_prev_node(1).display())
print("get previous node at pos 3 => ",lst1.get_prev_node(3).display())
print("\n---remove between list atIndex 2---")
lst1.remove_between_list(2)
print("\n-----add between list atIndex 2----")
lst1.add_between_list(2,"h")
lst1.display_all()
print("\n-----------search value------------")
lst1.search("h")


print()
pattern('lst2')
print()

lst2 = DoublyLinkedList()
print("List is empty => ",lst2.is_empty())
print("---------------add head--------------")
lst2.add_head(1)
lst2.add_head(2)
lst2.add_head(3)
lst2.add_head(4)
print("---------------add tail--------------")
lst2.add_tail(5)
lst2.add_tail(6)
lst2.display_all()
print("\n------------remove head------------")
lst2.remove_head()
lst2.display_all()
print("List is empty => ",lst2.is_empty())
print("Size => ",lst2.size)
print("Head => ",lst2.head.display())
print("Tail => ",lst2.get_tail().display())
print("Second last => ",lst2.find_second_last_element().display())
print("\n------------remove tail------------")
lst2.remove_tail()
lst2.display_all()
print("\nget previous node at pos 1 => ",lst2.get_prev_node(1).display())
print("\nget previous node at pos 3 => ",lst2.get_prev_node(3).display())
print("\nget node at pos 2 => ",lst2.get_node_at(2).display())
print("\n---remove between list atIndex 2---")
lst2.remove_between_list(2)
print("\n-----add between list atIndex 2----")
lst2.add_between_list(2,0)
lst2.display_all()
print("\n-----------search value------------")
lst2.search(1)

print("\n---------lst1.merge(lst2)----------\n")
lst1.merge(lst2)
lst1.display_all()
print("List is empty => ",lst1.is_empty())
print("Size => ",lst1.size)
print("Head => ",lst1.head.display())
print("Tail => ",lst1.get_tail().display())


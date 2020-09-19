class Node: 

    def __init__(self, element, next = None ):
        self.element = element
        self.next = next
    def display(self):
        print(self.element)

class SinglyLinkedList:
        
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
    
    
    def is_empty(self):
        return self.size == 0 
    
    def display(self):
        if self.size == 0:
            print("No element")
            return False
        first = self.head
        print(first.element)
        first = first.next
        while first:
            
            print(first.element)
            first = first.next
    
    
    def add_head(self,e):
        temp = self.head 
        self.head = Node(e) 
        self.head.next = temp
        self.size += 1 
        
    def get_tail(self):
        last_object = self.head
        while (last_object.next != None):
            last_object = last_object.next
        return last_object
        
    
    def remove_head(self):
        if self.is_empty():
            print("Empty Singly linked list")
        else:
            print("Removing")
            self.head = self.head.next
            self.size -= 1
            
    def add_tail(self,e):
        new_value = Node(e)
        self.get_tail().next = new_value
        self.size += 1
        
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
            
        return None

        
        
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
                
    def get_node_at(self,index):
        element_node = self.head
        counter = 0
        if index > self.size-1:
            return None
        while(counter < index):
            element_node = element_node.next
            counter += 1
        return element_node
  
        
                
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
            element_node.next = current_node
            self.size -= 1
        
    def search (self,search_value):
        index = 0 
        while (index < self.size):
            value = self.get_node_at(index)
            print("Searching at " + str(index) + " and value is " + str(value.element))
            if value.element == search_value:
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


print("--------Polynomial 1----------")   
poly1 = SinglyLinkedList()

order1 = int(input("Enter order for polynomial 1: \n"))
for i in reversed(range(order1+1)):
    poly1.add_head(int(input(f"Enter coefficient of power {i} : ")))

poly1.display()

print("--------Polynomial 2----------")
poly2 = SinglyLinkedList()

order2 = int(input("Enter order for polynomial 2: \n"))
for j in reversed(range(order2+1)):
    poly2.add_head(int(input(f"Enter coefficient of power {j} : ")))

poly2.display()


answer = []
index = 0
while index <= order1 or index <= order2:
    if (poly1.get_node_at(index) == None) or (poly2.get_node_at(index) == None):
        if poly1.get_node_at(index) == None:
            push_coeff_of2 = poly2.get_node_at(index).element
            answer.append(push_coeff_of2)
        elif poly2.get_node_at(index) == None:
            push_coeff_of1 = poly1.get_node_at(index).element
            answer.append(push_coeff_of1)
        else:
            pass
            break
    else:
        temp = (poly1.get_node_at(index).element + poly2.get_node_at(index).element)
        answer.append(temp)
    index += 1


print("\nAdded coefficients of Polynomial 1 and 2\n")
for deg in reversed(range(len(answer))):
    print("Degree ",deg," coefficient: ",answer[deg])










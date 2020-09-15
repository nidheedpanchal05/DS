## Practical 1(a)
'''
 Program to store the elements in 1-D array
 and provide operations like
 searching, sorting, merging, reversing the elements
'''

def search_element(my_list,element_to_srch):
    index = 0
    while index < len(my_list):
        print("Searching at index",index,"found",my_list[index])
        if my_list[index] == element_to_srch:
            print("Element",element_to_srch,"FOUND at index",index)
            return False
        index+=1
    print("Element",element_to_srch,"NOT FOUND")

## Bubble Sort
def sort_list(my_list):
    for i in range(len(my_list)-1):
        for j in range((len(my_list)-1)):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list
        
def merge(list1, list2):
    for i in range(len(list2)):
        list1.append(list2[i])
    return list1

def reverse_list(my_list):
    my_list = my_list[::-1]
    return my_list
    
array1 = [1,4,2,-1,-5,33,27]
array2 = ['p','b','z','e','a']
print("array1:  ",array1)
print("array2:  ",array2,"\n")

search_element(array1,-5)
print()
search_element(array1,5)
print()
search_element(array2,'z')
print()
sort_list(array1)
sort_list(array2)
print("Sorted array1:  ",array1)
print("Sorted array2:  ",array2)
print("Reverse array1:  ",reverse_list(array1))
merge(array1,array2)
print("Merge array1 and array2: ",array1)
print("Reverse:  ",reverse_list(array1))


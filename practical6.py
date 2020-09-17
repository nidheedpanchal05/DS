## Practical 6
'''
Program to sort list elements
Give user option to perform sorting using
    Insertion sort
    Bubble sort
    Selection sort
'''

print("-----------------Sorting algorithms----------------\n")
list_type = input('Enter 1 for sting values 2 for integer: ')
user_input = input('Enter list values seperated by space: ')
lst = user_input.split()
if list_type == '2':
    for element in range(len(lst)):
        lst[element] = int(lst[element])
    
print(lst)
print("\n  SELECT OPTION : \n  1 => Bubble sort\n  2 => Selection sort\n  3 => Insertion sort\n  Y => Exit")
    
def run_program(lst):
    def bubble_sort(lst):
        for i in range(len(lst)-1):
            for j in range((len(lst)-1)):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1],lst[j]

        return lst

    def selection_sort(lst):
        for i in range(len(lst)):
            smallest = i
            for j in range(i+1, len(lst)):
                if lst[smallest] > lst[j]:
                    smallest = j
            lst[i], lst[smallest] = lst[smallest], lst[i]
        return lst

    def insertion_sort(lst):
        for i in range (1, len(lst)):
            val = lst[i]
            j = i-1
            while j >= 0 and val < lst[j]:
                lst[j+1] = lst[j]
                j -= 1
            lst[j+1] = val
        return lst
    
    
    choice = input("\nEnter choice:  ")
    if choice == '1':
        print("BUBBLE SORT:  ",bubble_sort(lst))
        run_program(lst)
    elif choice == '2':
        print("SELECTION SORT:  ",selection_sort(lst))
        run_program(lst)
    elif choice == '3':
        print("INSERTION SORT: ",insertion_sort(lst))
        run_program(lst)
    elif choice == 'y' or choice == 'Y':
        print("---------------program ends----------------")
    else:
        print("!! INVALID CHOICE !!")
        run_program(lst)

run_program(lst)





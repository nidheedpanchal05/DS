## Practical 5
'''
Program to search an element from a list\
Give user the option to perform
    Linear or Binary Search
'''

print("\n  SELECT OPTION : \n  1 => BINARY SEARCH\n  2 => LINEAR SEARCH\n  Y => Exit")
print()
lst = [1,3,-8,5,0,33,12]
lst = sorted(lst)
print(lst)

def run_program(lst):
    def linear_search(lst,n):
        index = 0
        size = len(lst)
        while index < size:
            temp = lst[index]
            if temp == n:
                return index
            index += 1
        return -1

    ##def binary_search(list_val, search_element):
    ##    if search_element < list_val[0] or search_element > list_val[-1]:
    ##        return -1
    ##    mid = 0
    ##    start = 0
    ##    end = len(list_val)
    ##    step = 0
    ##    while (start <= end):
    ##        step += 1
    ##        mid = (start+end)//2
    ##        if search_element == list_val[mid]:
    ##            return mid
    ##        if search_element < list_val[mid]:
    ##            end = mid-1
    ##        else:
    ##            end = mid+1
    ##    return -1


    def binary_search(lst,search,start,end):
        lst = sorted(lst)
        if search > lst[-1]:
            return -1
        if start > end:
            return -1
        mid = (start+end)//2
        if lst[mid] == search:
            return mid
        if search < lst[mid]:
            return binary_search(lst,search,start,mid-1)
        else:
            return binary_search(lst,search,mid+1,end)
    choice = input("\nEnter choice:  ")
    if choice == '1':
        print("Binary search: ",binary_search(lst,search,0,len(lst)))
        run_program(lst)
    elif choice == '2':
        print("linear search: ",linear_search(lst,search))
        run_program(lst)
    else:
        print("!! INVALID CHOICE !!\n Program ends")
        
search = int(input('\nEnter value to search from the list: '))
run_program(lst)









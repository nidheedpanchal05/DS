##Program demonstating double ended queue

##create an empty list 'queue'
queue = []

def add_first(e):
	queue.insert(0,e)
	
def add_last(e):
	queue.append(e)
	
def delete_first():
	queue.pop(0)

def delete_last():
	queue.pop()

def first():
	return queue[0]

def last():
	return queue[-1]
	
def is_empty():
	return len(queue)==0
        #if it returns True then the queue is empty
        #if it returns False then the queue is having elements
	
def len_of():
	return len(queue)


print('---------Initially queue is empty---------')
print('is_empty   ', is_empty())
print('length of queue ', len_of())

print('\n')
add_first('A')
print('add_first => "A" ')
add_first('B')
print('add_first => "B" ')
print(queue)

print('\n')
add_last('C')
print('add_last => "C" ')
add_last('D')
print('add_last => "D" ')
print(queue)

print('\n')
delete_first()
print('delete_first  ', queue)
delete_last()
print('delete_last  ', queue)
print('')
add_first('E')
print('add_first => "E" ')
print(queue)
print('')
print('return first  ',first())
print('return last  ', last())

print('\n')
print('is_empty   ', is_empty())
print('length of queue ', len_of() )
print(queue)



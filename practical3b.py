## Practical 3(B)
## Tower of Hanoi
'''
Puzzle
    -Tower of hanoi consists of 3 towers
     and more than one rings
    -Rings are stacked in ascending order of their size
     smaller at the top and larger at the bottom
     
Rules
    -Only one disk can be moved among the towers
     at any given time
    -Only the "top" disk can be removed
    -No large disk can sit over a small disk
    
Minimum Steps to solve the puzzle
    2^n - 1
    Example:
    for '2 disks' minimum steps are,
    2^2 -1 = 3
    for '3 disks' minimum steps are,
    2^3 -1 = 7
'''
#Assumptions
'''
disks = Number of disks in the puzzle
source = 1st tower containing disks
destin = 2nd tower in which disks are to be arranged
temp = 3rd tower to just to place disks temporarily
'''

def towerOfHanoi(n_disks, source, destin, temp):
    if n_disks == 1:
        print ("Move disk 1 from rod",source,"to rod",destin)
        return
    towerOfHanoi(n_disks-1, source, temp, destin)
    print ("Move disk",n_disks,"from rod",source,"to rod",destin)
    towerOfHanoi(n_disks-1, temp, destin, source)

n_disks = 3
towerOfHanoi(n_disks, 'A', 'C', 'B')
# A, B, C are the towers/rods















                   

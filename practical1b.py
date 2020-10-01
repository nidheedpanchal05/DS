## Practical 1(b)
'''
Program to perform the following
Matrix Addition
Matrix Multiplication
Transpose of matrix

'''

def sum_of_AB(A, B):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])        
        output.append(row)
    return output

def multiplication(A, B):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def transpose(matrix):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result


A = [[1, 5, 1],
     [2, 4, 0],
     [1, 2,-3]]

B = [[0, 1, 2],
     [3, 4, 0],
     [2, 3, 5]]

print("A:  ",A)
print("B:  ",B)

add = sum_of_AB(A,B)
print("\nAddition of matrix A and B:\n",add)
multi = multiplication(A, B)
print("\nMultiplication of A and B:\n",multi)

A_transpose = transpose(A)
print("\nTranspose of matrix A:\n",A_transpose)

B_transpose = transpose(B)
print("\nTranspose of matrix B:\n",B_transpose)










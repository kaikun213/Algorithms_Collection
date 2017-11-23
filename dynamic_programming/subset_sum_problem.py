# The subset sum problem is: Given a set of n positive integers,
# S = {x 1 , x 2 , . . . , x n } and an integer W determine whether there is a subset
# S_0 subset of S, such that the sum of the elements in S 0 is equal to W .


# Solution: We construct a NxW sized array for keeping track if a subset is possible
# By building this array from the bottom up we can use the previous calculated values
# when calculating result_matrix[i,j], e.g. result_matrix[i-1,j] is already in the table.
def subset_sum(w, int_array):
    n = len(int_array)
    w = w+1                                 # Index+1 to iterate until 0-w, starting at zero
    result_matrix = matrix(n,w)
    for i in range(0,n):                    # Iterate to n, because subset must exist in values from 0..n
        for j in range(0,w):                # Iterate over w, because in an optimal solution where an item X_i is included the rest amount w-X_i would be checked
                if j == 0:                       # If given Integer is zero there always exists a subset
                    result_matrix[i][j] = True
                elif i > 0 and int_array[i] > j: # If the item is greater j it can't be part of subset but probably subset for prev. items exists
                    result_matrix[i][j] = result_matrix[i-1][j]
                elif i > 0:
                    # Recurrence: (1) item is included, amount reducted and checked for Int-Rest (2) not included, check smaller i.
                    result_matrix[i][j] = result_matrix[i-1][j-int_array[i]] or result_matrix[i-1][j]
                else:                           # If only one item, check if its equal the rest j
                    result_matrix[i][j] = j-int_array[i] == 0
    print("result", n-1, w-1)
    return result_matrix[n-1][w-1]

# Creates a x*y matrix with initializes False variables
def matrix(rows,columns):
    result = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(False)
        result.append(row)
    return result

print(subset_sum(12,[10,33,2]))

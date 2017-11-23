# Problem: Find the shortest path for all pairs of nodes in a graph G.
import sys

# Simple function to print a matrix more nicely
def print_matrix(matrix):
    n = len(matrix)
    for i in range(0,n):
        print "%s" % (matrix[i])
    print("\n")

# Solution: We calculate the matrix entries: d_ij^(k) = min{d_ij^(k-1), d_ik^(k-1)+d_kj^(k-1)}
# Analysis: O(n^3) , Space needed only one matrix stored
def floid_warshall(weight_matrix):
    n = len(weight_matrix)
    d_matrix = weight_matrix    # k-1 matrix -> k matrix
    for k in range(0,n):    # Bottom-Up: Calculate matrix for all subsets of k=0..n
        for i in range(0,n):
            for j in range(0,n):
                if (d_matrix[i][j] > d_matrix[i][k]+d_matrix[k][j]): # found new minimum
                    d_matrix[i][j] = d_matrix[i][k]+d_matrix[k][j]
        print_matrix(d_matrix)
    return d_matrix

w = [
[0,8,10,sys.maxint,sys.maxint,3],
[6,0,sys.maxint,3,sys.maxint,sys.maxint],
[sys.maxint,sys.maxint,0,sys.maxint,sys.maxint,1],
[sys.maxint,sys.maxint,sys.maxint,0,sys.maxint,2],
[sys.maxint,sys.maxint,5,1,0,sys.maxint],
[sys.maxint,2,sys.maxint,sys.maxint,1,0]
]

floid_warshall(w)

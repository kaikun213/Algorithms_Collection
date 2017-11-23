# Problem: Find the shortest path for all pairs of nodes in a graph G.
import sys

# Simple function to print a matrix more nicely
def print_matrix(matrix):
    n = len(matrix)
    for i in range(0,n):
        print "%s" % (matrix[i])
    print("\n")

# Solution: constantly squaring until we read n: D^(2), D^(4), D^(8), ... , D^([2^log (n) ]) => D^(n-1)
# We calculate the matrix entries: d_ij^(2s) = min_1=<k=<n{d_ik^(s) + d_kj^(s)}
def all_pair_shortest_path_matrix(weight_matrix):
    n = len(weight_matrix)
    d_matrix = weight_matrix
    s = 1
    while (s < n):  # squaring until n reached
        d2_matrix = d_matrix    # construct new matrix
        s = s*2                 # sqaure D^(2s) index
        for i in range(0,n):
            for j in range(0,n):
                min_k = d_matrix[i][j]
                for k in range(0,n):    # find minimum 1=<k=<n
                    if (min_k > d_matrix[i][k]+d_matrix[k][j]): # found new minimum
                        min_k = d_matrix[i][k]+d_matrix[k][j]
                d2_matrix[i][j] = min_k
        d_matrix = d2_matrix    # newly calculated matrix
        print_matrix(d2_matrix)
    return d2_matrix

w = [
[0,8,10,sys.maxint,sys.maxint,3],
[6,0,sys.maxint,3,sys.maxint,sys.maxint],
[sys.maxint,sys.maxint,0,sys.maxint,sys.maxint,1],
[sys.maxint,sys.maxint,sys.maxint,0,sys.maxint,2],
[sys.maxint,sys.maxint,5,1,0,sys.maxint],
[sys.maxint,2,sys.maxint,sys.maxint,1,0]
]

all_pair_shortest_path_matrix(w)

# Unfinished(!): Easily done by using numpy.roots(polynomial) function.

# Fast fourier transformation algorithm for convolution/multiplication of polynomials.
# We can get an O(n log n) algorithm instead of O(n^2) by using the properties of roots of unity.

# Solution O(n log n):
# 1.) Evaluate 2n-1 points for A(x) and B(x) polynomials: O(n log n)
# 2.) Do pointwise multiplication of the 2n-1 points from A(x) and B(x) to generate 2n-1 C(x) points. O(n)
# 3.) Interpolate the 2n-1 points to the unique C(x) 2n-polynomial: O(n log n)

# Note: N-Polynomial is given as array with length n and saved coefficients. (Zero if non existent)
#       All x are given as complex numbers with the in-built complex(n,)

import numpy as np

# Given a polynomial return 2n-1 points in O(n log n) time
def evaluate(poly1, number_of_points):
    result_points_array = []
    for j in range(0,number_of_points):
        root_of_unity = np.roots([j])
        result_points_array.append(evaluate_complex(poly1, root_of_unity))

def evaluate_complex(poly, complex_x):
    # A(x) = A_0(x^2) + x*A_1(x^2)
    a_zero = []
    a_one = []
    for i in range(0,len(poly1),1):
        if (i % 2 == 0):    # For all even A_0(x) = a_0 + a_2x + a_4x^2 + ...
            a_zero.append(poly1[i])
        else:               # For all odd A_1(x) = a_1 + a_3x + a_5x^2 + ...
            a_one.append(poly1[i])

    return evaluate_complex(a_zero, complex_x) + x*evaluate_complex(a_one, complex_x)

# Given two arrays of n points return an array with n multiplications of such
def pointwise_multiply(points1, points2):
    # return array of points

# Given an array of n-1 points return the unique matching n-polynomial
def interpolate(points_array):
    # return polynomial (points_array length)

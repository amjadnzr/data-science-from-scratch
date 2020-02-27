"""
===================VECTORS==========================

@author: amjad.n

Linear Algebra

Notes:-

*Abstractly, vectors are objects that can be added together to form new vectors 
 and that can be multiplied by scalars (i.e., numbers), also to form new 
 vectors.
 
*Concretely (for us), vectors are points in some finite-dimensional space.
 Although you might not think of your data as vectors, they are often a useful
 way to represent numeric data.
"""

"""
Zip functions pairs elements of one list with the respective element of the other array
arr1 = [4,5,6]
arr2 = [1,2,3]
zipped = list(zip(arr1,arr2))  # [(4,1),(5,2),(6,3)]
"""

"""
1.Vector * Scaler 
[1,2,3] * 2 = [2,4,6]

2.Vector + Vector 
[1,2,3] + [4,5,6] = [5,7,9] 

3.Vector - Vector 
[1,2,3] - [4,5,6] = [-3,-3,-3] 

4.Dot product(vector * vector) Output -> Scaler
[1,2,3] * [4,5,6] = (1 * 4) + (2 * 5) + (3 * 6) = 4 + 10 + 18 = 32
"""
from typing import List

Vector = List[float]

height_weight_age = [70,  # inches,
                     170, # pounds,
                     40 ] # years

grades = [95,   # exam1
          80,   # exam2
          75,   # exam3
          62 ]  # exam4

# Addition of two vectors :
def add(v: Vector, w: Vector) -> Vector:    
    assert len(v) == len(w), "vectors must be the same length"    
    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

#Subraction of two vectors :
def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

# Get the sum of multiple vectors 
def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    # Check that vectors is not empty
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

# Multiply a vector by a scaler
def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

# mean of vectors:
"""In here vector_sum() will take the responsibily of asserting the vector sizes """
def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

# Dot Product of two vectors : 
def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6
 

""" 
Considering a vector which maginitude is 1 and considering another vector w =[0,1]
* We can say that the dot product of v and w is v
Simply, length of the vector you’d get if you projected v onto w

concept : Imagine a traingle, If you want the length of the adjacent side then we take 
hypethenous*the angle between (h cos(teta)) 
"""

def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14  # 1 * 1 + 2 * 2 + 3 * 3

# Magnitude of an vector
""" 
To get the magnitude of a vector we can use pythogores theory
considering vector v =[3,4] 
x coordinate is 3 from orgin 
y coordinate is 4 from orgin
Thereby length of the vector is sqrt(3^2 + 4^2)
"""

import math

def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))   # math.sqrt is square root function

assert magnitude([3, 4]) == 5

# Distance between two vectors
""" 
Consider vector V and W
distance = sqrt((V1-W1)^2 ......(Vn-Wn)^2 )
"""
def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    """Computes the distance between v and w"""
    return math.sqrt(squared_distance(v, w))


"""
=====================MATRIX=================================== 

# Another type alias
Matrix = List[List[float]]

A = [[1, 2, 3],  # A has 2 rows and 3 columns
     [4, 5, 6]]

B = [[1, 2],     # B has 3 rows and 2 columns
     [3, 4],
     [5, 6]]
"""

from typing import Tuple

def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0   # number of elements in first row
    # num_rows and num_cols are returned as tuple
    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 rows, 3 columns

"""
Matrix with n rows and m column could be called as n * m ordered Matrix

If a matrix has only one row or only one column it is called a vector. 
A matrix having only one row is called a row vector. is a row vector, 
because it has only one row. A matrix having only one column is called a column vector.
"""

def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]             # A[i] is already the ith row

#traverse each element in the list and pick the fisrt element to form the column vector
def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return [A_i[j]          # jth element of row A_i
            for A_i in A]   # for each row A_i


from typing import Callable

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rows x num_cols matrix
    whose (i,j)-th entry is entry_fn(i, j)
    """
    return [[entry_fn(i, j)             # given i, create a list
             for j in range(num_cols)]  #   [entry_fn(i, 0), ... ]
            for i in range(num_rows)]   # create one list for each i

# Create an identity matrix 
def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]

"""
Use of matrices in Data Science 
1. we can use a matrix to represent a dataset consisting of multiple vectors.

2. we’ll see later, we can use an n × k matrix to represent a linear 
   function that maps k-dimensional vectors to n-dimensional vectors.
   
3. matrices can be used to represent binary relationships.(if relationship 
   exsist 1 and if not 0)
"""
# only need to look at one row
friends_of_five = [i
                   for i, is_friend in enumerate(friend_matrix[5])
                   if is_friend]
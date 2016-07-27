# -*- coding:utf-8 -*-


def convert(input_matrix):

    '''
    given nxn 2D matrix, reverse the matrix
    eg.
    given: [[1,2],[3,4]]
    expected: [[3,1], [4,2]]
    '''

    if not input_matrix:
        return
    elif len(input_matrix) == 1:
        return input_matrix
    m = len(input_matrix)
    n = len(input_matrix[0])
    output_array = []
    _output_array = [[0 for i in range(m)] for i in range(n)]
    for i in range(0, m):
        for j in range(0, n):
            _output_array[j][i] = input_matrix[i][j]
    for x in range(0, n):
        output_array.append(_output_array[x][::-1])

    return output_array


def partitionArray(nums):
    '''
    Partition an integers array into odd number first and even number second.
    eg.
    input [2, 3, 4, 5]
    output [3, 5, 2, 4]
    '''
    '''
    :param nums:
    :return:
    '''
    evenList = []
    oddList = []
    for i in nums:
        if i % 2 == 0:
            evenList.append(i)
        else:
            oddList.append(i)
    return sorted(oddList) + sorted(evenList)

def getNumPosition(l, query):
    '''
    Give you an integer array (index from 0 to n-1,
    where n is the size of this array, value from 0 to 10000)
    and an query list. For each query, give you an integer,
    return the number of element in the array that are
    smaller than the given integer.
    eg.
    For array [1,2,7,8,5],
    and queries [1,8,5], return [0,4,2]
    '''
    position = []
    for q in query:
        position.append(l.index(q))
    return position

if __name__ == '__main__':
    print convert([[1, 2, 3], [4, 5, 6]])
    print convert([[1,2], [3,4]])
    print convert([])

    print partitionArray([2, 3, 4, 5])

    print getNumPosition([1,2,7,8,5], [1, 8, 5] )
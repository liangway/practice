'''
given nxn 2D matrix, reverse the matrix
eg.
given: [[1,2],[3,4]]
expected: [[3,1], [4,2]]
'''


def convert(input_matrix):
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


if __name__ == '__main__':
    print convert([[1, 2, 3], [4, 5, 6]])
    print convert([[1,2], [3,4]])
    print convert([])
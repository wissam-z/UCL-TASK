def mat_to_list(adj_mat):
    """ Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)


    Returns:
    --------
     adj_list: `list[list[int]]`
        The adjacency list of the graph

    """

    isSquareMatrix = checkDimension(adj_mat)

    if len(adj_mat) == 0 or not isSquareMatrix:
        return []

    



    adjacencyList = []
    
    for currentRow in adj_mat:

        destinationVerticies = []

        for idx, value in enumerate(currentRow):
            if value == 1:
                destinationVerticies.append(idx)

        adjacencyList.append(destinationVerticies)



    return adjacencyList


def checkDimension(matrix):
    rowDim = len(matrix)

    for row in matrix:
        if len(row) != rowDim:
            return False
    return True

assert mat_to_list( [[0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0]]) == [[1, 3], [2], [0], [4], [3], []]


assert mat_to_list([[0, 1, 0, 0, 1], [0, 1, 0]]) == []

assert mat_to_list([[], []]) == []


def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """

    initialNodeExists = True if start_node in range(len(adj_list)) else False
    

    if not initialNodeExists or len(adj_list) == 0:
        return {}




    return reachableHelper(adj_list, start_node, {start_node})


    


def reachableHelper(adjList, startNode, reachableNodes):
    destinationVerticies = adjList[startNode]

    for vertex in destinationVerticies:
        vertexIsVisited = vertex in reachableNodes
        if not vertexIsVisited:
            reachableNodes.add(vertex)
            reachableHelper(adjList, vertex, reachableNodes)
    return reachableNodes


 
assert reachable([[1, 3], [2], [0], [4], [3], []], -1) == {}
assert reachable([[[]]], -31324234) == {}
assert reachable([[1, 3], [2], [0], [4], [3], []], -1) == {}


assert reachable([], 234234) == {}
assert reachable([[1, 3], [2], [0], [4], [3], []], 234234) == {}


assert reachable([[1, 3], [2], [0], [4], [3], []], 0) == {0, 1, 2, 3, 4}
assert reachable([[1, 3], [2], [0], [4], [3], []], 3) == {3, 4}
assert reachable([[1, 3], [2], [0], [4], [3], []], 3) == {3, 4}



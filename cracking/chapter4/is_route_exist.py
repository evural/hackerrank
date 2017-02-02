import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from queue import Queue
from dag import generate_random_graph


def is_route_exist(graph, node1, node2):
    return check_route(graph, node1, node2) or check_route(graph, node2, node1) 

def check_route(graph, s_node, d_node):
    size = len(graph.nodes)
    q = Queue(size*size)
    q.enqueue(s_node)
    graph.iteration += 1
    return bfs(s_node, d_node, q, graph.iteration)

def bfs(s_node, node, q, iteration):
    if q.is_empty():
        return []
    curr_node = q.dequeue()
    if curr_node.iteration >= iteration:
        return bfs(s_node, node, q, iteration)
    curr_node.iteration = iteration
    if curr_node == node:
        it_node = curr_node
        result_arr = []
        while(it_node != None and it_node != s_node):
            result_arr.append(it_node.data)
            it_node = it_node.parent
        result_arr.append(s_node.data)
        return result_arr
    for neighbor in curr_node.neighbors:
        neighbor.parent = curr_node
        q.enqueue(neighbor)
    return bfs(s_node, node, q, iteration)

if __name__ == "__main__":
    size = 10
    index1 = 0
    index2 = 5
    graph = generate_random_graph(size, 0.2)
    print(graph)
    node1 = graph.nodes[index1]
    node2 = graph.nodes[index2]
    print node1.data
    print node2.data
    reversed_path = is_route_exist(graph, node1, node2)
    if reversed_path == []:
        print ("No path is available")
    else:
        for i in reversed(reversed_path):
            sys.stdout.write(str(i))
            sys.stdout.write(" ")
        sys.stdout.write("\n")
        

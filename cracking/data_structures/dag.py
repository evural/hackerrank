import random
import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from queue import Queue


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.iteration = 0

    def __str__(self):
        for node in self.nodes:
            sys.stdout.write(str(node.data))
            sys.stdout.write("--->")
            for neighbor in node.neighbors:
                sys.stdout.write(str(neighbor.data))
                sys.stdout.write(" ")
            sys.stdout.write("\n")
        return ""


class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.visited = False
        self.iteration = 0
        self.parent = None

    def __str__(self):
        return str(self.data)

def generate_random_graph(size, density):
    g = Graph()
    for i in range(0, size):
        node = Node(i)
        g.nodes.append(node)
    max_number_of_edges = size * (size-1)
    edge_count = int(max_number_of_edges * density)
    for i in range(0, edge_count):
        successful = False
        while not successful:
            random_number1 = random.randint(0, size-1)
            random_number2 = random.choice(range(0, random_number1+1) + range(random_number1+1, size))
            if random_number1 == random_number2:
                continue
            s_node = g.nodes[random_number1]
            d_node = g.nodes[random_number2]
            if (s_node, d_node) in g.edges:
                continue
            g.edges.append((s_node, d_node))
            if topological_sort(g) == False:
                del g.edges[-1] 
                continue
            s_node.neighbors.append(d_node)
            successful = True
    return g

def topological_sort(graph):
    edges = []
    for edge in graph.edges:
        edges.append(edge)
    nodes = []
    for node in graph.nodes:
        parents_of_node = [edge[0] for edge in edges if edge[1] == node]
        if parents_of_node == []:
            nodes.append(node)
    sorted_nodes = []
    while nodes != []:
        node = nodes[0]
        del nodes[0]
        sorted_nodes.append(node)
        neighbors = [edge[1] for edge in edges if edge[0] == node]
        for neighbor in neighbors:
            edges.remove((node, neighbor))
            parents_of_neighbor = [edge[0] for edge in edges if edge[1] == neighbor]
            if parents_of_neighbor == []:
                nodes.append(neighbor)
    if edges != []:
        return False
    return True        
    
def check_route(s_node, d_node, size):
    q = Queue(size)
    q.enqueue(s_node)
    return bfs(d_node, q)

def bfs(node, q):
    if q.is_empty():
        return False
    curr_node = q.dequeue()
    if curr_node.visited == True:
        return bfs(node, q)
    curr_node.visited = True
    if curr_node == node:
        return True
    for c in curr_node.neighbors:
        q.enqueue(c)
    return bfs(node, q)
    

if __name__ == "__main__":
    graph = generate_random_graph(5, 0.5)
    print(graph)
    

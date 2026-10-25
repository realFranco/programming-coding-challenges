# Two classes will belong in this file as we could be in constant interaction with new algorithm.

from collections import deque
from typing import Dict, List


class Node:

    value: str  # This could be `any`.

    def __init__(self, value: str):
        self.value = value


class Graph:
    adjacency_list: Dict[str, (list[Node])]
    in_degree_count: Dict[str, int]

    def __init__(self):
        self.in_degree_count = {}
        self.adjacency_list = {}

    def insert_node(v: Node):
        pass

    def insert_edge(self, v: str, w: str) -> bool:
        inserted: bool = False

        if v in self.adjacency_list:
            self.adjacency_list[v].append( Node(w) )
            inserted = True
        else:
            self.adjacency_list[v] = [ Node(w) ]
            inserted = True

        return inserted

    def remove_node():
        pass

    def remove_edge():
        pass

    def get_in_degrees(self) -> Dict[str, int]:
        out: Dict[str, int] = {}

        for edge, targets in self.adjacency_list.items():
            if edge not in out:
                out[edge] = 0

            for target in targets:
                if target.value not in out:
                    out[target.value] = 0
                
                out[target.value] += 1

        return out

    def get_outbound_nodes(self, v: str) -> List[ Node ]:
        # Given a vertex `v` return his adjacency list.
        return self.adjacency_list[v] if v in self.adjacency_list else []

    def get_adjacency_list(self) -> Dict[str, List[str]]:
        out: Dict[str, List[str]] = {}

        for edge, targets in self.adjacency_list.items():
            out[edge] = [target.value for target in targets]

        return out


def topologicalSort(graph: Graph) -> List[str]:
    # We could make a new version using a grid instead of an adjacency list.
    zero_in_degree: deque = deque()
    in_degree_nodes: Dict[str, int] = {}
    path: deque = deque()

    for edge, in_degree in graph.get_in_degrees().items():
        if in_degree == 0:
            zero_in_degree.append(edge)
        else:
            in_degree_nodes[edge] = in_degree

    while zero_in_degree:
        current_root: str = zero_in_degree.popleft()

        if current_root in path:
            continue
        
        path.append(current_root)
        for v in graph.get_outbound_nodes(current_root):
            # Simulate the removal of the Node as we "processed"
            in_degree_nodes[v.value] -= 1

            if in_degree_nodes[v.value] == 0:
                zero_in_degree.append(v.value)


    # Transform the output.
    out: List[str] = []
    while path:
        out.append(path.popleft())

    return out


tests: List = [
    [
        ['a', 'b'],
        ['d', 'f'],
        ['e', 'f'],
        ['b', 'c'],
        ['b', 'h'],
        ['f', 'h'],
        ['g', 'h'],
    ],

    # New set of edges here.
]

g = Graph()
for edges in tests:
    for edge in edges:
        g.insert_edge(v=edge[0], w=edge[1])

print('adjacency list', g.get_adjacency_list())

out: Dict[str, int] = g.get_in_degrees()
print('get in degrees', out)

topological_sort_path: List[str] = topologicalSort(g)
print('topological sort path', topological_sort_path)

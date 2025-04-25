from typing import Iterable, Tuple, Union, Dict, List

Node = Union[str, int]
Edge = Tuple[Node, Node]


class Graph(object):
    """Graph data structure, undirected by default."""

    def __init__(self, edges: Iterable[Edge] = [], directed: bool = False):
        self.directed = directed
        self.graph: Dict[Node, List[Node]] = {}

        for edge in edges:
            self.add_edge(edge)

    def has_node(self, node: Node) -> bool:
        """Check if a node exists in the graph."""
        return node in self.graph

    def has_edge(self, edge: Edge) -> bool:
        """Check if an edge exists in the graph."""
        node1, node2 = edge
        if node1 not in self.graph or node2 not in self.graph:
            return False
        if self.directed:
            return node2 in self.graph[node1]
        else:
            return node2 in self.graph[node1] or node1 in self.graph[node2]

    def add_node(self, node: Node):
        """Add a node to the graph."""
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, edge: Edge):
        """Add an edge to the graph."""
        node1, node2 = edge
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        self.graph[node1].append(node2)
        if not self.directed:
            self.graph[node2].append(node1)

    def remove_node(self, node: Node):
        """Remove a node and all its edges from the graph."""
        if node not in self.graph:
            raise ValueError(f"Node {node} not found in the graph.")

        # Remove the node and its edges
        del self.graph[node]

        # Remove references to the node in other nodes' neighbors
        for neighbors in self.graph.values():
            if node in neighbors:
                neighbors.remove(node)

    def remove_edge(self, edge: Edge):
        """Remove an edge from the graph."""
        node1, node2 = edge
        if node1 not in self.graph or node2 not in self.graph:
            raise ValueError(f"Edge {edge} not found in the graph.")

        if node2 in self.graph[node1]:
            self.graph[node1].remove(node2)
            if not self.directed:
                self.graph[node2].remove(node1)
        elif self.directed:
            raise ValueError(f"Directed edge {edge} not found.")

    def indegree(self, node: Node) -> int:
        """Compute the indegree of a node (number of incoming edges)."""
        if node not in self.graph:
            raise ValueError(f"Node {node} not found in the graph.")
        return sum(1 for neighbors in self.graph.values() if node in neighbors)

    def outdegree(self, node: Node) -> int:
        """Compute the outdegree of a node (number of outgoing edges)."""
        if node not in self.graph:
            raise ValueError(f"Node {node} not found in the graph.")
        return len(self.graph[node])

    def __str__(self) -> str:
        """String representation of the graph."""
        result = []
        for node, neighbors in self.graph.items():
            result.append(f"{node}: {', '.join(map(str, neighbors))}")
        return "\n".join(result)

    def __repr__(self) -> str:
        """Official string representation of the graph."""
        return f"Graph(directed={self.directed}, graph={self.graph})"

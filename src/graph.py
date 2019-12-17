import networkx as nx


class Graph:
    def __init__(self):
        self.g = nx.Graph()

    def add_node_list(self, node_list):
        self.g.add_weighted_edges_from(node_list)

    def node_count(self):
        return self.g.number_of_nodes()

    def edge_count(self):
        return self.g.number_of_edges()

    def get_edges(self):
        return self.g.edges

    def get_edge_weight(self, node1, node2):
        return self.g.get_edge_data(node1, node2)["weight"]

    def add_node(self, node1, node2):
        self.g.add_edge(node1, node2)

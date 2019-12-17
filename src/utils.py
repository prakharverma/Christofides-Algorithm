from src.graph import Graph


def create_graph_from_txt_file(txt_file: str):
    nodes = []
    with open(txt_file) as file:
        line = file.readline()
        while line:
            if "#" not in line:
                n_info = line.replace("\n", "").split("   ")
                nodes.append((n_info[0], n_info[1], n_info[2]))

            line = file.readline()

    if len(nodes) > 0:
        g = Graph()
        g.add_node_list(nodes)
        return g

    raise Exception("Wrong input file provided")


def get_mst(graph: Graph):
    # Kruskal's algorithm
    edges = graph.get_edges()
    weighted_edges = []
    for (u, v) in edges:
        weighted_edges.append([graph.get_edge_weight(u, v), u, v])

    # sort edges by weight
    weighted_edges = sorted(weighted_edges)

    mst_graph = Graph()
    nodes = []
    for (k, u, v) in weighted_edges:
        if u in nodes and v in nodes:
            continue

        mst_graph.add_node(u, v)
        nodes.append(u)
        nodes.append(v)

    return mst_graph

import src.utils as utils


if __name__ == '__main__':

    txt_file = r"input/input_2.txt"

    # create graph from input txt file
    initial_g = utils.create_graph_from_txt_file(txt_file)
    print(f"Nodes : {initial_g.node_count()}")
    print(f"Edges : {initial_g.edge_count()}")

    # TODO : Validation of the graph. Acyclic, triangle inequality property

    # create a MST
    mst_graph = utils.get_mst(initial_g)

    print(mst_graph.get_edges())



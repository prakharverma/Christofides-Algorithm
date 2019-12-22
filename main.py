import os

import src.utils as utils


if __name__ == '__main__':

    txt_file = r"input/input_1.txt"
    output_path = r"output/"
    debug = True

    # create graph from input txt file
    initial_g = utils.create_graph_from_txt_file(txt_file)
    if debug:
        print("Initial Graph:")
        utils.print_edges_with_weight(initial_g)
        initial_g.plot_graph(os.path.join(output_path, "graph.png"))

    # TODO : Validation of the graph: triangle inequality property

    # create a MST
    mst_graph = utils.get_mst(initial_g)
    if debug:
        print("\nMST:")
        utils.print_edges_with_weight(mst_graph)
        mst_graph.plot_graph(os.path.join(output_path, "mst.png"))

    mst_degrees = utils.get_degrees(mst_graph)
    if debug:
        print(f"\nMST degree : {mst_degrees}")

    odd_degrees = utils.get_nodes_odd_degrees(mst_degrees)
    if debug:
        print(f"\nMST odd degree : {odd_degrees}")

    subgraph = utils.create_subgraph(initial_g, odd_degrees)
    if debug:
        print("\nSubgraph:")
        utils.print_edges_with_weight(subgraph)
        subgraph.plot_graph(os.path.join(output_path, "subgraph.png"))

    minimum_perfect_match = utils.create_minimum_weight_perfect_matching(subgraph)
    if debug:
        print("\nMinimum weight perfect match:")
        utils.print_edges_with_weight(minimum_perfect_match)
        minimum_perfect_match.plot_graph(os.path.join(output_path, "minimum_perfect_match.png"))

    union_graph = utils.union_graphs(mst_graph, minimum_perfect_match)
    if debug:
        print("\nUnion graph details:")
        utils.print_edges_with_weight(union_graph)
        union_graph.plot_graph(os.path.join(output_path, "union_graph.png"))

    euler_tour_itr = union_graph.get_euler_tour()
    euler_tour = []
    for e in euler_tour_itr:
        euler_tour.append(e)

    if debug:
        print(f"\n Euler tour: {euler_tour}")

"""
My version of Minimun Spanning Tree Kruskal's Variant
"""

from pprint import pprint as pp

adj_list1 = {
    'A': [('B', 7)],
    'B': [('C', 6), ('A', 7)],
    'C': [('B', 6), ('F', 3), ('D', 2)],
    'D': [('C', 2), ('F', 5)],
    'F': [('D', 5)]
}

adj_list2 = {
    'A': [('B', 4), ('F', 2)],
    'B': [('A', 4), ('C', 6), ('F', 5)],
    'C': [('B', 6), ('F', 1)],
    'F': [('C', 1), ('A', 2), ('B', 5)]
}

adj_list3 = {
    'A': [('B', 4), ('F', 2)],
    'B': [('A', 4), ('C', 6), ('F', 5)],
    'C': [('B', 6), ('F', 1), ('D', 3)],
    'D': [('C', 3), ('E', 2)],
    'E': [('D', 2), ('F', 4)],
    'F': [('C', 1), ('A', 2), ('B', 5), ('E', 4)]
}

# CLASS TO CREATE NODE

class Graph(object):
    def __init__(self, adj_list):
        self.g_dict = adj_list
        self.output_dict = {}
        self.to_node = {}
        self.visited_hist = []
        self.bookmark = (None, None, None)  # <- visited idx0 from idx1 with weight of idx2
        self.previous_children = []
        self.previous_reserved = []

    def Vertices(self):
        return self.g_dict.keys()

    def __tracer(self, visiting_vertex, visited_vertex=None, min_weigth=None):

        # starting variables
        visiting = visiting_vertex
        visiting_from = visited_vertex
        visiting_to = None

        # setting the dictionary to accept appending values in respective list
        if visiting not in self.output_dict.keys():
            self.output_dict.update({visiting: []})

        # traces the coming-from
        # direction of the path
        if visiting_from <> None:
            self.output_dict[visiting].append((visiting_from, min_weigth))

        # visit tracker to keep the history
        # of visits and prevent visiting twice
        self.visited_hist.append(visiting)
        visited_list = self.visited_hist

        # these are the children of the
        # visiting node
        visit_tracer = self.g_dict[visiting]

        # setting the weight
        # to none for...
        min_weigth = None
        new_min_weigth = None

        if visiting == 'F':
            pass

        for child, weight in visit_tracer:

            # looking for direction
            if (min_weigth > weight and visiting_to <> None) and child not in visited_list:
                """ Here the children edge minimum is set and the weight of this
                children edge is less than the one from before, so the trace will 
                change direction at this point only if the child was not already
                visited.
                """
                self.previous_reserved.append((visiting, visiting_to, min_weigth)) # <- what is the purpose of the reserve?
                visiting_to = child
                min_weigth = weight
            elif (min_weigth > weight or min_weigth == None) and child not in visited_list:
                """ Here the children edge minimum is not set or the weight of this 
                children edge is less than the one from before, so the trace will
                change direction at this point only if the child was not already
                visited.
                """

                visiting_to = child
                min_weigth = weight
            elif child not in visited_list:
                """ Here are the children visited that did not met
                the minimum value.
                """
                self.previous_children.append((visiting, child, weight))

        # if trace is not over continue with bookmark
        if visiting_to == None:
            if len(self.visited_hist) < len(self.g_dict.keys()):
                """ All nodes should be visited.
                if not we continue with bookmarks or
                saved children
                """

                if self.bookmark[0] <> None:
                    """ If there is a bookmark,
                    there was a change in direction
                    """

                    self.__tracer(self.bookmark[0], self.bookmark[1], self.bookmark[2])
                else:
                    """ When there is no bookmark,
                    it look for previous children
                    """

                    reserved_weigth = None
                    for visited, child, weight in self.previous_children:
                        if weight < reserved_weigth or reserved_weigth == None:
                            self.bookmark = child
                    self.previous_children = []
                    self.__tracer(self.bookmark, visited, weight)

            return self.output_dict

        # assigning visited children to assess
        last_visit_children = self.previous_children

        # comparing children weights
        if visiting_from <> None:

            # beating the current path
            for visited, child, weight in last_visit_children:

                assess_min = new_min_weigth or min_weigth

                if assess_min > weight:
                    """ A previous better
                    path was found, so
                    direction change.
                    """

                    new_min_weigth = weight
                    self.bookmark = (visiting, None, None)
                    visiting_to = child
                    visiting = visited

            # beating the bookmark
            for visited, child, weight in last_visit_children:
                if child <> visiting_to:
                    if min_weigth > weight:
                        self.bookmark = (child, visited, weight)

            # changing minimum direction
            min_weigth = new_min_weigth or min_weigth

            # clear preserved children when done using them
            self.previous_children = []
            self.previous_children = self.previous_reserved
            self.previous_reserved = []

        # traces the forward direction in the dictionary
        self.output_dict[visiting].append((visiting_to, min_weigth))

        # recurse in the code over the next node
        self.__tracer(visiting_to, visiting, min_weigth)

    def MST(self, next_vet=None):

        start_vet = self.__find_start_point()

        self.__tracer(start_vet)

        return self.output_dict

    def __find_start_point(self):

        min_edge = None

        for vert, neigs in self.g_dict.items():

            for neig in neigs:

                """
                The minimum edge is the first minimum found. If there is two competing minimum edges,
                the first first minimum will be collected.
                """
                if min_edge > neig[1] or min_edge == None:
                    start_point = neig[0]
                    min_edge = neig[1]

        "The starting point will be the to_vertex related to the minimum edge"
        return start_point # <- this is the start of the minimum spanning tree


graph = Graph(adj_list1)
pp(graph.MST())

print

graph = Graph(adj_list2)
pp(graph.MST())

print

graph = Graph(adj_list3)
pp(graph.MST())


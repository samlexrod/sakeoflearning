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
    'F': [('C', 1), ('A', 2), ('B', 5)]
}

# CLASS TO CREATE NODE

class Graph(object):
    def __init__(self, adj_list):
        self.g_dict = adj_list
        self.output_dict = {}
        self.to_node = {}
        self.visited_hist = []
        self.bookmark = None
        self.previous_children = []
        self.previous_reserved = []

    def Vertices(self):
        return self.g_dict.keys()

    def __tracer(self, visiting_vertex, visited_vertex=None, min_weigth=None):
        output_debug = self.output_dict
        # starting variables
        visiting = visiting_vertex
        visiting_from = visited_vertex
        visiting_to = None

        if visiting not in self.output_dict.keys(): self.output_dict.update({visiting: []})

        if visiting_from <> None:
            self.output_dict[visiting].append((visiting_from, min_weigth))
        output_debug = self.output_dict

        # visit tracker
        self.visited_hist.append(visiting)
        visited_list = self.visited_hist

        # visit tracker
        visit_tracer = self.g_dict[visiting]
        min_weigth = None

        for child, weight in visit_tracer:

            # looking for direction
            if (min_weigth > weight and visiting_to <> None) and child not in visited_list:
                self.previous_reserved.append((visiting, visiting_to, min_weigth))
                visiting_to = child
                min_weigth = weight
            elif (min_weigth > weight or min_weigth == None) and child not in visited_list:
                visiting_to = child
                min_weigth = weight
            elif child not in visited_list:
                self.previous_children.append((visiting, child, weight))

        # if trace is not over continue with bookmark
        if visiting_to == None:
            if len(self.visited_hist) < len(self.g_dict.keys()):

                if self.bookmark <> None:
                    self.__tracer(self.bookmark)
                else:
                    reserved_weigth = None
                    for visited, child, weight in self.previous_children:
                        if weight < reserved_weigth or reserved_weigth == None:
                            self.bookmark = child
                    self.previous_children = []
                    self.__tracer(self.bookmark, visited, weight)


            return self.output_dict

        last_visit_children = self.previous_children

        # comparing children weights
        if visiting_from <> None:
            for visited, child, weight in last_visit_children:
                if min_weigth > weight:
                    min_weigth = weight
                    self.bookmark = visiting
                    bookmark = self.bookmark
                    visiting_to = child
                    visiting = visited

            # clear preserved children when done using them
            self.previous_children = []
            self.previous_children = self.previous_reserved
            self.previous_reserved = []

        self.output_dict[visiting].append((visiting_to, min_weigth))
        #self.output_dict.update({visiting: [(visiting_to, min_weigth)]})
        output_debug = self.output_dict

        self.__tracer(visiting_to, visiting, min_weigth)

    def MST(self, next_vet=None):

        start_vet = self.__find_start_point()

        self.__tracer(start_vet)

        return self.output_dict

    def __find_start_point(self):

        min_edge = None

        for vert, neigs in self.g_dict.items():

            for neig in neigs:

                # print min_edge, "<", neig[1], min_edge > neig[1], vert, neig[0]

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


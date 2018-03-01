"""
My version of a leas common ancestor on a binary tree
"""

      #0| 1| 2| 3| 4|
T1 = [[0, 0, 0, 0, 0], #0
      [0, 0, 0, 0, 0], #1
      [1, 1, 0, 0, 0], #2
      [0, 0, 1, 0, 1], #3
      [0, 0, 0, 0, 0]] #4

      #0| 1| 2| 3| 4| 5| 6| 7| 8| 9|
T2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #0
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], #1
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2
      [0, 1, 1, 0, 0, 0, 0, 0, 0, 0], #3
      [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], #4
      [0, 0, 0, 0, 0, 0, 1, 1, 0, 0], #5
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #6
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #7
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #8
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] #9

      #0| 1| 2| 3| 4| 5| 6| 7| 8|
T3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], #0
      [0, 0, 0, 0, 0, 0, 0, 0, 0], #1
      [1, 1, 0, 0, 0, 0, 0, 0, 0], #2
      [0, 0, 1, 0, 1, 0, 0, 0, 0], #3
      [0, 0, 0, 0, 0, 1, 1, 0, 0], #4
      [0, 0, 0, 0, 0, 0, 0, 0, 0], #5
      [0, 0, 0, 0, 0, 0, 0, 1, 1], #6
      [0, 0, 0, 0, 0, 0, 0, 0, 0], #7
      [0, 0, 0, 0, 0, 0, 0, 0, 0]] #8


class Tree:
    def __init__(self):
        self.tree = []
        self.parameters = (None, None, None)
        self.ancestor = None
        self.parent_list = [None, None]
        self.connections = []

    def insert_tree(self, T, r, n1, n2):
        self.tree = T
        self.parameters = (r, n1, n2)

    def __findLCA(self, node_L=None, node_R=None):

        for node, row in enumerate(self.tree):
            """ Finds connections not visited
            it iterates through each row of the 
            columns n1 and n2 """

            left  = row[node_L]
            right = row[node_R]

            if left or right:
                """ 
                Connection 
                found 
                """

                if left and right:           # the lca is the direct parent
                    self.ancestor = node
                    break
                elif node in (node_L, node_R): # the lca is the actual parent
                    self.ancestor = node
                    break
                elif node in self.connections: # the lca is the common one
                    self.ancestor = node
                    break

                # adding all the connections
                self.connections.append(node)

                # tracking the next iteration
                if left: self.parent_list[0]  = node
                if right: self.parent_list[1] = node

                # break look after second search
                if len(self.connections) % 2 == 0:
                    break

        if self.ancestor == None:
            """If there is still no ancestor 
            recurse over the code with new 
            arguments"""

            node_L, node_R = self.parent_list
            self.parent_list = [None, None]
            self.__findLCA(node_L, node_R)

    def LCA(self):
        self.__findLCA(self.parameters[1], self.parameters[2])
        print "Returning: {}".format(self.ancestor)
        return self.ancestor

def question4(T, r, n1, n2):
    tree = Tree()
    tree.insert_tree(T, r, n1, n2)
    tree.LCA()


# Test one
question4(T3, 0, 8, 6) #<- testing root from both sides
question4(T3, 0, 3, 6) #<- testing root form same sides
question4(T3, 0, 3, 4) #<- testing direct parent
question4(T3, 0, 2, 4) #<- testing direct ancestor
print '-'

# Test two
question4(T2, 2, 7, 9) #<- testing root from both sides
question4(T2, 2, 5, 9) #<- testing root form same sides
question4(T2, 2, 7, 8) #<- testing direct parent
question4(T2, 2, 1, 0) #<- testing direct ancestor
print '-'

# Test three
question4(T1, 3, 1, 4) #<- testing root from both sides
question4(T1, 3, 1, 2) #<- testing root form same sides
question4(T1, 3, 0, 4) #<- testing direct parent
question4(T1, 3, 0, 2) #<- testing direct ancestor
print '-'
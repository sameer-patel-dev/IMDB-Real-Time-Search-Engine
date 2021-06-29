import _pickle as pickle
from collections import defaultdict

class Graph(object):

    def __init__(self):
        print("Initializing Graph Object")

        try:
            pickle_file = open('imdb.pickle', 'rb')
        except IOError:
            print("Cannot find pickle file. Initializing new graph...")
            self.is_pickled = False
            graph = defaultdict(set)
        else:
            print("Loading pickle file for scraper...")
            self.is_pickled = True
            graph = pickle.load(pickle_file)
            pickle_file.close()
        
        self.graph = graph
        

    
    
    def addConnections(self, connections):
        if len(connections) == 0: return None

        for node1, node2 in connections:
            self.graph[node1].add(node2)
    

    def getNeighbors(self, node):
        if node == None or node == "": return None
        return self.graph[node]
    

    def findCommonNeighbors(self, nodes):
        if len(nodes) == 0: return None

        adj_sets = list()
        for node in nodes:
            adj_sets.append(self.getNeighbors(node))

        return list(set.intersection(*adj_sets))
    

    def saveGraph(self):
        #print("Serializing Search Graph with " + str(len(self.graph.keys())) + " keys")
        with open('imdb.pickle', 'wb') as f:
            pickle.dump(self.graph, f)
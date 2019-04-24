import numpy as np
from collections import defaultdict
import math

class Graph():
  def __init__(self):
    # default dictionary to store graph
    self.graph = defaultdict(list)
    self.undirectedgraph = defaultdict(list)
    self.dfs_output = np.array([],dtype=int)
    self.bfs_output = np.array([],dtype=int)
    self.no_nodes = 0
    self.no_edges = 0
    self.nodesSet = set()
    self.graphWeights = {}

  #adds node to the set of all nodes
  def addNode(self, node):
    self.nodesSet.add(node)

  #adds edge in both directed and undirected fashion
  def addEdge(self,source,destination,weight):
    self.graph[source].append(destination)
    self.undirectedgraph[source].append(destination)
    self.undirectedgraph[destination].append(source)
    self.graphWeights[(source, destination)] = weight

  #creates the graph after taking inputs from the user
  def createGraph(self):
    self.graph = defaultdict(list)
    nodes = int(input("Enter total number of nodes in your graph :"))
    self.no_nodes = nodes
    edges = int(input("Enter total number of edges in your graph: "))
    print("Please denote the nodes as 0,1,2... : \n")
    for i in range(edges):
      userinput = input("Enter source, destination, and weight of the edge (separated by comma):")
      userinput = userinput.split(",")
      source = int(userinput[0])
      destination = int(userinput[1])
      weight = int(userinput[2])
      self.addEdge(source,destination,weight)
    print("The connectivity in directed graph is (ignoring the edge weight) :\n")
    for entry in self.graph:
      print (entry, "-->" ,self.graph[entry])
      self.no_edges = self.no_edges + len(self.graph[entry])
    for k in range(nodes):
      self.addNode(k)

  #prints onnectivity in directed graph
  def printGraph(self):
    print("The connectivity in directed graph is (ignoring the edge weight) :\n")
    for entry in self.graph:
      print (entry, "-->" ,self.graph[entry])

  #Dijkstra from source to all the vertices
  def Dijkstra(self, source):
    visitedDijkstra = {source: 0}
    path = {}

    nodesArray = set(self.nodesSet)
    while nodesArray: 
      min_node = None
      for node in nodesArray:
        if node in visitedDijkstra:
          if min_node is None:
            min_node = node
          elif visitedDijkstra[node] < visitedDijkstra[min_node]:
            min_node = node

      if min_node is None:
        break

      nodesArray.remove(min_node)
      current_weight = visitedDijkstra[min_node]

      for edge in self.graph[min_node]:
        try:
          weight = current_weight + self.graphWeights[(min_node, edge)]
        except:
          weight = current_weight + math.inf
        if edge not in visitedDijkstra or weight < visitedDijkstra[edge]:
          visitedDijkstra[edge] = weight
          path[edge] = min_node

    for entry in visitedDijkstra:
      print ("Destination:", entry, "Distance:", visitedDijkstra[entry])

  def DFSHelper(self,source,visitedDFS):
    visitedDFS[source] = True
    self.dfs_output = np.append(self.dfs_output, int(source))
    for i in self.graph[source]:
      if visitedDFS[i] == False:
        self.DFSHelper(i, visitedDFS)

  # The function to do DFS traversal. It uses recursive DFSHelper()
  def DFS(self,source):
    self.dfs_output = np.array([],dtype=int)
    visitedDFS = [False]*(self.no_nodes)
    self.DFSHelper(source,visitedDFS)
    print(self.dfs_output)
  
  # The function to do BFS traversal.
  def BFS(self, source):
    self.bfs_output = np.array([],dtype=int)
    visitedBFS = [False]*(self.no_nodes)
    queueBFS = []
    queueBFS.append(source)
    visitedBFS[source] = True
    while queueBFS:
      source = queueBFS.pop(0)
      self.bfs_output = np.append(self.bfs_output, int(source))
      if len(self.bfs_output) == self.no_nodes:
        break
      for i in self.graph[source]:
        if visitedBFS[i] == False:
          queueBFS.append(i)
          visitedBFS[i] = True
    print(self.bfs_output)

  # function to detect if the graph has cycle
  def isCyclicHelper(self, source, visitedCyclic, recStackCyclic): 
    visitedCyclic[source] = True
    recStackCyclic[source] = True

    for neighbour in self.graph[source]: 
      if visitedCyclic[neighbour] == False: 
        if self.isCyclicHelper(neighbour, visitedCyclic, recStackCyclic) == True:
          return True
      elif recStackCyclic[neighbour] == True: 
        return True

    recStackCyclic[source] = False
    return False

  # Returns true if graph is cyclic else false 
  def isCyclic(self):
    visitedCyclic = [False]*self.no_nodes 
    recStackCyclic = [False]*self.no_nodes
    for node in range(self.no_nodes): 
      if visitedCyclic[node] == False: 
        if self.isCyclicHelper(node,visitedCyclic,recStackCyclic) == True: 
          return True
    return False
  # converts directed dictionary to undirected matrix
  def ToUndirected(self):
    undirected = [[0 for column in range(self.no_nodes)]for row in range(self.no_nodes)]
    for i in range(self.no_nodes):
      for j in self.graph[i]:
        undirected[int(i)][int(j)] = 1
        undirected[int(j)][int(i)] = 1
    return undirected

  def isBipartiteHelper(self, source, colorArray, undirected): 
  
    colorArray[source] = 1
    queueBipartite = [] 
    queueBipartite.append(source) 
    while queueBipartite: 
      u = queueBipartite.pop()
      if undirected[u][u] == 1: 
        return False; 
      for v in range(self.no_nodes):
        if undirected[u][v] == 1 and colorArray[v] == -1:
          colorArray[v] = 1 - colorArray[u] 
          queueBipartite.append(v)
        elif undirected[u][v] == 1 and colorArray[v] == colorArray[u]: 
          return False

  # Function that returns true if the graph is bipartite
  def isBipartite(self):
    undirected = self.ToUndirected()
    colorArray = [-1] * self.no_nodes 
    for i in range(self.no_nodes):
      if colorArray[i] == -1: 
        if self.isBipartiteHelper(i, colorArray,undirected) == False:
          return False;
    return True
  
  #checks and returns true if the graph is connecte
  def isConnected(self, vertices_encountered = None, source=None):
    if vertices_encountered is None:
      vertices_encountered = set()

    vertices = list(self.undirectedgraph.keys()) 
    if not source:
      source = vertices[0]
    vertices_encountered.add(source)
    if len(vertices_encountered) != len(vertices):
      for vertex in self.undirectedgraph[source]:
        if vertex not in vertices_encountered:
          if self.isConnected(vertices_encountered, vertex):
            return True
    else:
        return True
    return False
 
 # given a graph, check if the graph is a tree
  def isTree(self):
    #check if the graph is connected
    isconnected = self.isConnected()
    if (isconnected==0):
      return False

    # check if |E| = |V| - 1
    if self.no_edges != self.no_nodes - 1:
      return False

    # check if the graph has cycles
    hasCycle = self.isCyclic()
    if hasCycle:
      return False
    # otherwise passes all properties for a tree
    return True

choice = 0
g = Graph()
while(choice!=9):
  print("Enter your choice : \n")
  print(" 1. Create a Directed Graph \n 2. Print the connectivity of the Graph \n 3. DFS Traversal of Graph \n 4. BFS Traversal of Graph \n 5. Shortest path from source to all reachable vertices \n 6. Is there a Cycle in Graph? \n 7. Graph is Bipartite or not? \n 8. Graph is a Tree or not?\n 9. Exit!\n")
  choice = int(input())

  if(choice==1):
    g.createGraph()
  if(choice==2):
    g.printGraph()
  if(choice==3):
    print("DFS Traversal starting from vertex :")
    v = int(input())
    g.DFS(v)
  if(choice==4):
    print("BFS Traversal starting from vertex :")
    s = int(input())
    g.BFS(s)
  if(choice==5):
    print("Source from which to find the shortest path to all vertices using Dijkstra’s Algorithm. :")
    s = int(input())
    g.Dijkstra(s)
  if(choice==6):
    if g.isCyclic() == 1: 
      print ("Graph has a cycle")
    else: 
      print ("Graph has no cycle")
  if(choice==7):
    if g.isBipartite() == 1: 
      print ("Graph is Bipartite")
    else: 
      print ("Graph is not Bipartite")
  if(choice==8):
    if g.isTree() == 1: 
      print ("Graph is a tree")
    else: 
      print ("Graph is not a tree")
  if(choice==9):
    print ("Thank you and exit!")
    break
This is the readme file for the Programming Project – 3 on graphs.

The key idea here is to use a one to many dictionary to store the directed edges of the graph. Also, another dictionary is use to store the undirected version of the graph and yet another is used to store the weights of the edges. The main class "Graph" has various routines to add a node, add an edge, print the graph connectivity, perform BFS, perform DFS, perform Dijkstra’s algorithm, check graph connectivity, check if there is a cycle, check if graph is bipartite, check if graph is a tree etc. I also have two arrays to store the DFS and BFS traversal nodes. I have used sets to represents the nodes in the graph. I have used queues in BFS and Bipartite functions. I also have a function that converts directed dictionary to undirected matrix. I use lists to check connectivity in a graph.

Steps to compile and run the program:-
1. Compile and run the file "graph.py"
2. After running the file, the console asks for your choice of task to perform (which is an integer value from 1 to 9). After the desired size, "ENTER" is expected.
3. The first step would usually be to create the graph. Then it prompts you for number of nodes and number of egdes in your graph. It then takes the source, destination and weight for each the edges in your directed graph. Also it is expected that the nodes are numbered as 0,1,2,3 and so on.
4. After this, you can choose to print your graph, DFS traverse it from a source, BFS traverse it from a source, find the shortest path from a source to all the reachable vertices, check if there is a cycle, check if the graph is bipartite, check if the graph is a tree.
5. The program runs until exit operation is selected.


An example to execute the program is as belows:-


Enter your choice : 

 1. Create a Directed Graph 
 2. Print the coonectivity of the Graph 
 3. DFS Traversal of Graph 
 4. BFS Traversal of Graph 
 5. Shortest path from source to all reachable vertices 
 6. Is there a Cycle in Graph? 
 7. Graph is Bipartite or not? 
 8. Graph is a Tree or not?
 9. Exit!

1
Enter total number of nodes in your graph :4
Enter total number of edges in your graph: 6
Please denote the nodes as 0,1,2... : 

Enter source, destination, and weight of the edge (separated by comma):0,1,3
Enter source, destination, and weight of the edge (separated by comma):0,2,10
Enter source, destination, and weight of the edge (separated by comma):1,2,4
Enter source, destination, and weight of the edge (separated by comma):2,0,5
Enter source, destination, and weight of the edge (separated by comma):2,3,1
Enter source, destination, and weight of the edge (separated by comma):3,3,20
The connectivity in directed graph is (ignoring the edge weight) :

0 --> [1, 2]
1 --> [2]
2 --> [0, 3]
3 --> [3]
Enter your choice : 

 1. Create a Directed Graph 
 2. Print the coonectivity of the Graph 
 3. DFS Traversal of Graph 
 4. BFS Traversal of Graph 
 5. Shortest path from source to all reachable vertices 
 6. Is there a Cycle in Graph? 
 7. Graph is Bipartite or not? 
 8. Graph is a Tree or not?
 9. Exit!

3
DFS Traversal starting from vertex :
2
[2 0 1 3]
Enter your choice : 

 1. Create a Directed Graph 
 2. Print the coonectivity of the Graph 
 3. DFS Traversal of Graph 
 4. BFS Traversal of Graph 
 5. Shortest path from source to all reachable vertices 
 6. Is there a Cycle in Graph? 
 7. Graph is Bipartite or not? 
 8. Graph is a Tree or not?
 9. Exit!

4
BFS Traversal starting from vertex :
2
[2 0 3 1]
Enter your choice : 

 1. Create a Directed Graph 
 2. Print the coonectivity of the Graph 
 3. DFS Traversal of Graph 
 4. BFS Traversal of Graph 
 5. Shortest path from source to all reachable vertices 
 6. Is there a Cycle in Graph? 
 7. Graph is Bipartite or not? 
 8. Graph is a Tree or not?
 9. Exit!

4
BFS Traversal starting from vertex :
0
[0 1 2 3]
Enter your choice : 

 1. Create a Directed Graph 
 2. Print the coonectivity of the Graph 
 3. DFS Traversal of Graph 
 4. BFS Traversal of Graph 
 5. Shortest path from source to all reachable vertices 
 6. Is there a Cycle in Graph? 
 7. Graph is Bipartite or not? 
 8. Graph is a Tree or not?
 9. Exit!

4
BFS Traversal starting from vertex :
3
[3]
Enter your choice : 

 1. Create a Directed Graph 
 2. Print the coonectivity of the Graph 
 3. DFS Traversal of Graph 
 4. BFS Traversal of Graph 
 5. Shortest path from source to all reachable vertices 
 6. Is there a Cycle in Graph? 
 7. Graph is Bipartite or not? 
 8. Graph is a Tree or not?
 9. Exit!

3
DFS Traversal starting from vertex :
3
[3]
Enter your choice : 

 1. Create a Directed Graph 
 2. Print the coonectivity of the Graph 
 3. DFS Traversal of Graph 
 4. BFS Traversal of Graph 
 5. Shortest path from source to all reachable vertices 
 6. Is there a Cycle in Graph? 
 7. Graph is Bipartite or not? 
 8. Graph is a Tree or not?
 9. Exit!

5
Source from which to find the shortest path to all vertices using Dijkstra’s Algorithm. :
0
Destination: 0 Distance: 0
Destination: 1 Distance: 3
Destination: 2 Distance: 7
Destination: 3 Distance: 8
Enter your choice : 

 1. Create a Directed Graph 
 2. Print the coonectivity of the Graph 
 3. DFS Traversal of Graph 
 4. BFS Traversal of Graph 
 5. Shortest path from source to all reachable vertices 
 6. Is there a Cycle in Graph? 
 7. Graph is Bipartite or not? 
 8. Graph is a Tree or not?
 9. Exit!

5
Source from which to find the shortest path to all vertices using Dijkstra’s Algorithm. :
3
Destination: 3 Distance: 0
Enter your choice : 

 1. Create a Directed Graph 
 2. Print the coonectivity of the Graph 
 3. DFS Traversal of Graph 
 4. BFS Traversal of Graph 
 5. Shortest path from source to all reachable vertices 
 6. Is there a Cycle in Graph? 
 7. Graph is Bipartite or not? 
 8. Graph is a Tree or not?
 9. Exit!

6
Graph has a cycle
Enter your choice : 

 1. Create a Directed Graph 
 2. Print the coonectivity of the Graph 
 3. DFS Traversal of Graph 
 4. BFS Traversal of Graph 
 5. Shortest path from source to all reachable vertices 
 6. Is there a Cycle in Graph? 
 7. Graph is Bipartite or not? 
 8. Graph is a Tree or not?
 9. Exit!

7
Graph is not Bipartite
Enter your choice : 

 1. Create a Directed Graph 
 2. Print the coonectivity of the Graph 
 3. DFS Traversal of Graph 
 4. BFS Traversal of Graph 
 5. Shortest path from source to all reachable vertices 
 6. Is there a Cycle in Graph? 
 7. Graph is Bipartite or not? 
 8. Graph is a Tree or not?
 9. Exit!

8
Graph is not a tree
Enter your choice : 

 1. Create a Directed Graph 
 2. Print the coonectivity of the Graph 
 3. DFS Traversal of Graph 
 4. BFS Traversal of Graph 
 5. Shortest path from source to all reachable vertices 
 6. Is there a Cycle in Graph? 
 7. Graph is Bipartite or not? 
 8. Graph is a Tree or not?
 9. Exit!

9
Thank you and exit!
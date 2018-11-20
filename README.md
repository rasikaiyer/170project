The creategraph method takes in one parameter D and creates a graph with subgraphs of
size 1, 2, 3, ..., D-1, D. With a total number of vertices of D * (D+1) / 2

In this method, we initially add six edges to the first five edgeds that corresponds to the first 3 smallest subgraphs. Then we generalize the creation of the rest of the subgraphs. We create clusters of i verticies using a for loop where i goes from 4 to D. Each of these subgraphs is created in a nested for loop ranging from start, which is the 6th vetex initially, to start + i - 1.

For each subraph, vertex start will be connected (frienship) to each vertex but start will form a rowdy group with every vertex except start + 1, start + 2. Start will also create a rowdy group if combined with start + 1, and start + i (the vertex in the next subgraph). Also, we also created a friendship between start + 1, and start + 2. We also created a pair and triples of rowdy for each vertex except start, start + 1, and start + 2 because we want this to be one of the possible solutions.

We do this repeatedly until all subgraphs are created and this will create a connected graph with clusters.

The optimal solution is combining the start, start + 2, start + i, and all the possible vertices we can connect with start + i in a set rather than start , start + 1, start +2, which a greedy solution would choose.

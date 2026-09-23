# Dijkstra Maze Visualizer

This is a small Python project I made while learning Dijkstra's shortest path algorithm

The program uses Dijkstra's algorithm to find the shortest path from a starting point to an ending point in a simple grid-based maze. I also added a terminal visualization so I could actually see how the algorithm explores the maze instead of just getting the final answer.

# How the maze works

The maze is stored as a 2D list.

* "0" means the cell can be visited
* "1" means there is a wall

The starting point and ending point are represented using their row and column positions.

For example:

python
start_point = (0, 0)
end_point = (4, 4)


# How Dijkstra works in this project

The algorithm starts from the starting cell with a distance of "0".

It then:

1. Takes the cell with the smallest known distance.
2. Checks its four possible neighbors.
3. Ignores walls and cells outside the maze.
4. Calculates the distance to each valid neighbor.
5. Updates the neighbor if a shorter route has been found.
6. Adds the updated cell to the priority queue.
7. Continues until the destination is reached.

I use Python's "heapq" module to implement the priority queue.

The program also keeps track of where each cell came from using "came_from". This is used at the end to reconstruct the actual path instead of only knowing the shortest distance.

# Visualization

The program shows the search happening in the terminal.

* 🟢 Start
* 🔴 End
* 🎯 Current cell being processed
* 🟡 Cells waiting in the priority queue
* 🔍 Visited cells
* ⬛ Walls
* ⬜ Unexplored cells

The visualization was mainly added to make the algorithm easier for me to understand while learning it.

# A small thing I learned

In this particular maze, every move has the same cost ("1").

Because of that, BFS could also find the shortest path here.

Dijkstra is still useful for understanding the general shortest-path approach, especially the idea of using a priority queue and updating a distance when a shorter route is found. If the edges had different weights, Dijkstra would become more important.

## Running the project

You just need Python installed.

bash
python main.py


The search will start in the terminal and the final shortest path will be displayed after the algorithm reaches the destination.

## What I practiced

While making this project, I got practice with:

* Dijkstra's algorithm
* Priority queues
* 2D grids
* Dictionaries and sets
* Tracking visited nodes
* Path reconstruction
* Python functions
* Following the state of an algorithm while it runs


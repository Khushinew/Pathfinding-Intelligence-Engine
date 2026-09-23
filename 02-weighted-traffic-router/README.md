# Dijkstra Traffic Router 🚦

A small Python project that uses Dijkstra's algorithm to find the fastest route through a traffic-based grid.

Instead of treating every road as having the same cost, each cell in the grid represents a different traffic condition. This allows the algorithm to choose a route based on total travel time, rather than simply choosing the route with the fewest steps.

# How It Works

The grid uses different values to represent road conditions:

* 1 → Highway / low travel cost
* 3 → Normal city road
* 10 → Heavy traffic
* -1 → Closed road / accident

For example:

```text
3   -1   1   3   10
1   -1  -1  -1    3
1    1   1   1    1
```

The program starts from a given intersection and searches for the destination while considering the travel cost of each road.

# Dijkstra's Algorithm

The main idea is to always explore the currently known lowest-cost route first.

For every neighboring cell, the program calculates:

```text
new travel time = current travel time + road cost
```

If this new time is smaller than the previously known time for that intersection, the value is updated and the intersection is added to the priority queue.

The program keeps track of:

* Priority Queue — intersections waiting to be explored, ordered by travel time.
* Fastest Time — the smallest known travel time to each intersection.
* Visited Intersections — intersections that have already been processed.
* "came_from" — stores where each intersection was reached from, so the final route can be reconstructed.

## Visualization

The program also displays the search process in the terminal.

```text
🟢 Start
🔴 Destination
🎯 Currently processing
🟡 Waiting in queue
🔍 Already visited
🛣️ Highway
🚙 Normal traffic
🚗 Heavy traffic
🚧 Closed road
```

The animation makes it easier to see how Dijkstra explores the grid and gradually finds the fastest route.

# Why Use Dijkstra Here?

In a simple maze where every movement has the same cost, algorithms such as **Breadth-First Search (BFS)** can find the shortest path.

This project adds different costs to the roads, so the route with the fewest steps is not necessarily the fastest route.

For example:

```text
Route A → 4 roads × 1 minute = 4 minutes
Route B → 2 roads × 10 minutes = 20 minutes
```

A shortest-step approach could prefer Route B, while Dijkstra chooses the route with the lower total cost.

# What I Learned

This project helped me understand Dijkstra's algorithm beyond just its theory.

Some of the things I practiced were:

* Working with Python's `heapq` priority queue
* Representing a map using a 2D list
* Tracking the shortest known distance to each node
* Updating a path when a better route is discovered
* Reconstructing the final path using a predecessor dictionary
* Understanding the difference between a discovered node and a visited node
* Visualizing an algorithm while it is running

One of the things I found interesting was that changing the problem from an equal-cost maze to a weighted traffic grid required only a small change in the core Dijkstra logic, but it changed what the algorithm was actually optimizing.

# Running the Project

Make sure Python is installed, then run:

```bash
python traffic_router.py
```

The program will display the route search in the terminal and show the final fastest route once the destination is reached.

# Possible Improvements

Some ideas I may explore later:

* Generate larger maps automatically
* Add randomly changing traffic conditions
* Allow the user to choose the start and destination
* Compare Dijkstra with BFS and A*
* Add diagonal movement
* Create a graphical interface instead of a terminal visualization

# Project Status

This is a learning project created while studying graph algorithms and shortest-path problems. The main goal was to understand how Dijkstra's algorithm works in a practical situation rather than just implementing it as a textbook exercise.

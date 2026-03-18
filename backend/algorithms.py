import heapq
import math

def heuristic(G, a, b):
    x1, y1 = G.nodes[a]["x"], G.nodes[a]["y"]
    x2, y2 = G.nodes[b]["x"], G.nodes[b]["y"]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def dijkstra(G, start, goal):

    queue = [(0, start)]
    visited = set()
    dist = {start: 0}
    parent = {start: None}

    while queue:
        cost, node = heapq.heappop(queue)

        if node == goal:
            break

        if node in visited:
            continue

        visited.add(node)

        for neighbor in G.neighbors(node):
            weight = G[node][neighbor]["weight"]
            new_cost = cost + weight

            if neighbor not in dist or new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(queue, (new_cost, neighbor))

    return reconstruct_path(parent, goal)


def astar(G, start, goal):

    queue = [(0, start)]
    g = {start: 0}
    parent = {start: None}

    while queue:
        _, node = heapq.heappop(queue)

        if node == goal:
            break

        for neighbor in G.neighbors(node):
            cost = g[node] + G[node][neighbor]["weight"]

            if neighbor not in g or cost < g[neighbor]:
                g[neighbor] = cost
                priority = cost + heuristic(G, neighbor, goal)

                heapq.heappush(queue, (priority, neighbor))
                parent[neighbor] = node

    return reconstruct_path(parent, goal)


def reconstruct_path(parent, goal):

    path = []
    node = goal

    while node:
        path.append(node)
        node = parent[node]

    return path[::-1]
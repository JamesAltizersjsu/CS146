def canFinish(numCourses, prerequisites):
    # Initialize in-degree array and adjacency list
    in_degree = [0] * numCourses
    graph = [[] for _ in range(numCourses)]

    # Populate in-degree and adjacency list
    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1

    # Initialize queue with courses having in-degree 0
    queue = []
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    # Perform topological sort
    while queue:
        course = queue.pop(0)
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all courses are processed, return True
    return len(queue) == 0

# Example usage
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(canFinish(numCourses, prerequisites))  # Output: True

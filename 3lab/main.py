import math


def dfs(graph, start, end, visited, current_path, current_distance, min_distance, min_path):
    current_path.append(start)

    if start == end:
        if current_distance < min_distance[0]:
            min_distance[0] = current_distance
            min_path[0] = current_path.copy()
        print(
            f"Текущий путь: {current_path}, Пробованные маршруты: {visited}, Промежуточные минимальные расстояния: {min_distance[0]}")
        return

    visited.add(start)

    for neighbor, weight in graph[start].items():
        if neighbor not in visited:
            dfs(graph, neighbor, end, visited, current_path, current_distance + weight, min_distance, min_path)

    visited.remove(start)
    current_path.pop()

    print(
        f"Текущий путь: {current_path}, Пробованные маршруты: {visited}, Промежуточные минимальные расстояния: {min_distance[0]}")


def find_shortest_path(graph, start, end):
    visited = set()
    current_path = []
    min_distance = [
        math.inf]
    min_path = [[]]

    dfs(graph, start, end, visited, current_path, 0, min_distance, min_path)

    print(f"Кратчайший путь: {min_path[0]}")
    print(f"Минимальное расстояние: {min_distance[0]}")


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
end_vertex = 'D'

find_shortest_path(graph, start_vertex, end_vertex)

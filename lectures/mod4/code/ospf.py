from collections import defaultdict
import heapq

# 网络拓扑
network = {
    'A': {'B': 1, 'D': 3},
    'B': {'A': 1, 'C': 2, 'E': 1},
    'C': {'B': 2},
    'D': {'A': 3, 'E': 4},
    'E': {'B': 1, 'D': 4}
}

# LSA 数据
lsas = {
    'A': {'neighbors': {'B': 1, 'D': 3}, 'seq': 1},
    'B': {'neighbors': {'A': 1, 'C': 2, 'E': 1}, 'seq': 1},
    'C': {'neighbors': {'B': 2}, 'seq': 1},
    'D': {'neighbors': {'A': 3, 'E': 4}, 'seq': 1},
    'E': {'neighbors': {'B': 1, 'D': 4}, 'seq': 1}
}

# 泛洪模拟
def flood_lsa(network, lsas):
    lsdb = defaultdict(dict)
    visited = {}
    def propagate(router, lsa, source):
        lsa_id = lsa['router']
        seq = lsa['seq']
        if lsa_id not in visited or seq > visited[lsa_id]:
            visited[lsa_id] = seq
            lsdb[lsa_id] = lsa
            for neighbor in network[router]:
                if neighbor != source:
                    propagate(neighbor, lsa, router)
    for router, lsa in lsas.items():
        lsa['router'] = router
        propagate(router, lsa, None)
    return lsdb

# Dijkstra算法
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    pq = [(0, start)]
    visited = set()
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    return distances, previous

# 运行OSPF
lsdb = flood_lsa(network, lsas)
print("LSDB:")
for router, lsa in lsdb.items():
    print(f"路由器 {router}: {lsa}")

# 构建拓扑图并运行Dijkstra
graph = {r: lsa['neighbors'] for r, lsa in lsdb.items()}
distances, previous = dijkstra(graph, 'A')

# 输出路由表
print("\n路由器 A 的路由表:")
for node in graph:
    if node != 'A':
        path = []
        current = node
        while current:
            path.append(current)
            current = previous[current]
        path.reverse()
        print(f"到 {node}: 路径 {' -> '.join(path)}, 代价 {distances[node]}, 下一跳 {path[1] if len(path) > 1 else 'N/A'}")
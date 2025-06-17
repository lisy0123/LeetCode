class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        visited = {}
        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, k)]

        # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, cnt = heapq.heappop(Q)
            if node == dst:
                return price

            if cnt >= 0 and (node not in visited or visited[node] < cnt):
                visited[node] = cnt
                for v, w in graph[node]:
                    heapq.heappush(Q, (price + w, v, cnt - 1))
        return -1

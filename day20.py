import sys
from heapq import heappush, heappop


def func():
    N, M, K, X = map(int, sys.stdin.readline().split())

    adjacent = [[] for _ in range(N+1)]

    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        adjacent[A].append(B)

    # 이 문제는 도시의 사이의 거리가 1으로 고정되어 있으므로, BFS로도 풀 수 있으나, 다익스트라로 풀어보자.

    # 다익스트라 알고리즘은 특정 도시 X에서 각 도시로 가는 가장 짧은 거리를 찾는다.

    # 이를 위해, 우선 이론상 최장거리 이상의 값으로 최단거리를 저장하는 배열을 만든다.
    # 이는 X에서 각 도시로 도달하는 최단 거리를 의미한다.
    min_distance = [300000 for _ in range(N+1)]  # 30만-1개의 도시(도로)를 거쳐 도달할 수 있으므로, 최댓값으로 초기화

    # 또한 방문한 도시를 저장하는 배열을 만든다.
    visited = [False for _ in range(N + 1)]  # 방문한 도시 표기

    # 이때 시작 도시에 대한 최단거리는 0으로 설정한다.
    min_distance[X] = 0

    # 다익스트라 알고리즘은 우선순위 큐를 이용한다. (현재 노드에서 가장 거리가 짧은 노드를 방문하기 위함)
    pq = [(0, X)]
    while pq:
        distance, vertex = heappop(pq)

        # 이미 방문한 지점이거나 저장된 최단거리보다 더 큰 경우는 순회할 필요 없음
        if visited[vertex] or distance > min_distance[vertex]:
            continue

        visited[vertex] = True  # 방문한 도시로 표기

        # 현재 노드에서 갈 수 있는 정점 중 가장 가까운 점을 먼저 탐색한다. (이 문제에서는 거리가 1이므로 이는 상관이 없다)
        for next_vertex in adjacent[vertex]:
            if visited[next_vertex]:  # 이미 방문한 도시라면 방문하지 않음
                continue

            # 다음 정점을 탐색할 때, 현재 저장되어있는 최단거리(X에서 해당 정점으로 가는 최단거리)와,
            # 현재 정점까지의 거리와 이 정점에서 다음 정점까지 가는 도로의 거리(이 문제에서는 1)의 합을 비교한다.
            if min_distance[next_vertex] > min_distance[vertex] + 1:

                # 후자의 값이 더 크다면 해당 도시까지 가는 최단 거리 값이 새로 갱신되므로, 이로 교체해준다.
                min_distance[next_vertex] = min_distance[vertex] + 1

                # 우선순위 큐에 다음 노드와, 거리를 저장한다.
                heappush(pq, (min_distance[next_vertex], next_vertex))

    # 이 과정을 거치면, 우선순위 큐가 이용되므로 가장 짧은 거리를 우선하여 선택하며 진행하게 되며,
    # 이미 방문한 도시는 방문하지 않으므로 최단거리가 자동으로 선택된다.

    # 이제 저장된 최단거리를 순회하며, 거리가 K인 도시를 오름차순으로 출력하자.
    flag = False
    for i in range(1, N+1):
        if min_distance[i] == K:
            sys.stdout.write(str(i) + "\n")
            flag = True

    if not flag:
        print(-1)


func()














































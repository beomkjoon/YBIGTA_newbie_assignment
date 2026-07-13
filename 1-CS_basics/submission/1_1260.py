# -*- coding: utf-8 -*-
from __future__ import annotations
import copy
from collections import deque
from collections import defaultdict
from typing import DefaultDict, List


"""
TODO:
- __init__ �����ϱ�
- add_edge �����ϱ�
- dfs �����ϱ� (��� �Ǵ� ���� ��� ����)
- bfs �����ϱ�
"""


class Graph:
    def __init__(self, n: int) -> None:
        """
        �׷��� �ʱ�ȭ
        n: ������ ���� (1������ n������)
        """
        self.n = n
        self.adj: list[list[int]] = [[] for _ in range(n+1)]
        # �����ϼ���!

    
    def add_edge(self, u: int, v: int) -> None:
        """
        ����� ���� �߰�
        """
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.adj[u].sort()
        self.adj[v].sort()
        # �����ϼ���!
        pass
    
    def dfs(self, start: int) -> list[int]:
        """
        ���� �켱 Ž�� (DFS)
        
        ���� ��� ����:
        1. ��� ���: �Լ� ���ο��� ��� �Լ� �����Ͽ� ����
        2. ���� ���: ������ ������ ����Ͽ� �ݺ������� ����
        """
        visited = [False] * (self.n + 1)
        result: list[int] = []
        stack = [start]

        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            result.append(node)
            # ���� ��ȣ�� ���� pop�ǵ��� �������� push
            for nxt in reversed(self.adj[node]):
                if not visited[nxt]:
                    stack.append(nxt)

        return result
        # �����ϼ���!
        pass
    
    def bfs(self, start: int) -> list[int]:
        """
        �ʺ� �켱 Ž�� (BFS)
        ť�� ����Ͽ� ����
        """
        visited = [False] * (self.n + 1)
        result: list[int] = []
        queue: deque[int] = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            result.append(node)
            for nxt in self.adj[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    queue.append(nxt)

        return result
        # �����ϼ���!
        pass
    
    def search_and_print(self, start: int) -> None:
        """
        DFS�� BFS ����� ���
        """
        dfs_result = self.dfs(start)
        bfs_result = self.bfs(start)
        
        print(' '.join(map(str, dfs_result)))
        print(' '.join(map(str, bfs_result)))



from typing import Callable
import sys


"""
-�ƹ��͵� �������� ������!
"""


def main() -> None:
    intify: Callable[[str], list[int]] = lambda l: [*map(int, l.split())]

    lines: list[str] = sys.stdin.readlines()

    N, M, V = intify(lines[0])
    
    graph = Graph(N)  # �׷��� ����
    
    for i in range(1, M + 1): # ���� ���� �Է�
        u, v = intify(lines[i])
        graph.add_edge(u, v)
    
    graph.search_and_print(V) # DFS�� BFS ���� �� ���


if __name__ == "__main__":
    main()

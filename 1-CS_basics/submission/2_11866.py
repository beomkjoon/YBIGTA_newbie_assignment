# -*- coding: utf-8 -*-
from __future__ import annotations
from collections import deque


"""
TODO:
- rotate_and_remove �����ϱ� 
"""


def create_circular_queue(n: int) -> deque[int]:
    """1���� n������ ���ڷ� deque�� �����մϴ�."""
    return deque(range(1, n + 1))

def rotate_and_remove(queue: deque[int], k: int) -> int:
    """
    ť���� k��° ���Ҹ� �����ϰ� ��ȯ�մϴ�.
    """
    queue.rotate(-(k - 1))
    return queue.popleft()
    # �����ϼ���!
    pass




"""
TODO:
- josephus_problem �����ϱ�
    # �似Ǫ�� ���� ����
        # 1. ť ����
        # 2. ť�� �� ������ �ݺ�
        # 3. ���� ���� ����Ʈ ��ȯ
"""


def josephus_problem(n: int, k: int) -> list[int]:
    """
    �似Ǫ�� ���� �ذ�
    n�� �� k��°���� �����ϴ� ������ ��ȯ
    """
    queue = create_circular_queue(n)
    result: list[int] = []
    while queue:
        result.append(rotate_and_remove(queue, k))
    return result
    # �����ϼ���!
    pass

def solve_josephus() -> None:
    """��, ��� format"""
    n: int
    k: int
    n, k = map(int, input().split())
    result: list[int] = josephus_problem(n, k)
    
    # ��� ����: <3, 6, 2, 7, 5, 1, 4>
    print("<" + ", ".join(map(str, result)) + ">")

if __name__ == "__main__":
    solve_josephus()
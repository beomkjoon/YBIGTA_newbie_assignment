# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push �����ϱ�
- (�ʿ��� ���) Trie�� �߰� method �����ϱ�
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T�� �� (list[int]�� ���� �ְ� str�� ���� �ְ� ���...)

        action: trie�� seq�� �����ϱ�
        """
        # �����ϼ���!
        pass

    # �����ϼ���!


import sys


"""
TODO:
- �ϴ� lib.py�� Trie Class���� �����ϱ�
- main �����ϱ�

��Ʈ: �� ����¥�� �ڷῡ�� �׳� str�� ���⿡�� �޸𸮰� �Ʊ���...
"""


def main() -> None:
    MOD = 1_000_000_007
    data = sys.stdin.read().split()
    n = int(data[0])
    names = data[1:1 + n]

    trie: Trie[str] = Trie()
    for name in names:
        trie.push(name)

    answer = 1
    for node in trie:
        k = len(node.children)
        if k > 1:
            fact = 1
            for i in range(2, k + 1):
                fact = fact * i % MOD
            answer = answer * fact % MOD

    print(answer)


if __name__ == "__main__":
    main()
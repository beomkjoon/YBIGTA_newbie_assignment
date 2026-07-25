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
- �ϴ� Trie���� �����ϱ�
- count �����ϱ�
- main �����ϱ�
"""


def count(trie: Trie, query_seq: str) -> int:
    """
    trie - �̸� �״�� trie
    query_seq - �ܾ� ("hello", "goodbye", "structures" ��)

    returns: query_seq�� �ܾ �Է��ϱ� ���� ��ư�� ������ �ϴ� Ƚ��
    """
    pointer = 0
    cnt = 0

    for element in query_seq:
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        new_index = 0 # �����ϼ���!

        pointer = new_index

    return cnt + int(len(trie[0].children) == 1)


def main() -> None:
    # �����ϼ���!
    pass


if __name__ == "__main__":
    main()
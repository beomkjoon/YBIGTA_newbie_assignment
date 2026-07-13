# -*- coding: utf-8 -*-
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree �����ϱ�
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    # �����ϼ���!
    pass


import sys


"""
TODO:
- �ϴ� SegmentTree���� �����ϱ�
- main �����ϱ�
"""


class Pair(tuple[int, int]):
    """
    ��Ʈ: 2243, 3653���� int�� ���� ���׸�Ʈ Ʈ���� ������ٸ� ���⼭�� Pair�� ���� ���׸�Ʈ Ʈ���� ���� �� ��������...?
    """
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
        """
        �⺻��
        �̰� �� �ʿ��ұ�...?
        """
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
        """
        ���� ������ ���� �����Ǵ� Pair ������ ��ȯ�ϴ� ����
        �̰� �� �ʿ��ұ�...?
        """
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: Pair, b: Pair) -> 'Pair':
        """
        �� Pair�� �ϳ��� Pair�� ��ġ�� ����
        �̰� �� �ʿ��ұ�...?
        """
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]


def main() -> None:
    # �����ϼ���!
    pass


if __name__ == "__main__":
    main()
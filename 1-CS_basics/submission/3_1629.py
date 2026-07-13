# -*- coding: utf-8 -*-
# lib.py�� Matrix Ŭ������ �������� ����
import sys


"""
TODO:
- fast_power �����ϱ� 
"""


def fast_power(base: int, exp: int, mod: int) -> int:
    """
    ���� �ŵ����� �˰����� ����
    ���� ������ �̿�, �ð����⵵ ����!
    """
    if mod == 1:
        return 0

    result = 1
    base %= mod

    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1

    return result
    # �����ϼ���!
    pass

def main() -> None:
    A: int
    B: int
    C: int
    A, B, C = map(int, input().split()) # �Է� ����
    
    result: int = fast_power(A, B, C) # ��� ����
    print(result) 

if __name__ == "__main__":
    main()

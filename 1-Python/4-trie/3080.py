from lib import Trie
import sys


"""
TODO:
- 일단 lib.py의 Trie Class부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
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
from collections import deque
import sys

input = sys.stdin.readline

def goblins_and_shamans():
    n = int(input())
    left = deque()
    right = deque()

    for _ in range(n):
        command = input().strip()

        if command[0] == '+':
            _, x = command.split()
            right.append(x)

        elif command[0] == '*':
            _, x = command.split()
            left.append(x)

        elif command[0] == '-':
            print(left.popleft())

        if len(left) < len(right):
            left.append(right.popleft())
        elif len(left) > len(right) + 1:
            right.appendleft(left.pop())

goblins_and_shamans()

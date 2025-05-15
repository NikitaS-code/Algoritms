def can_sort_train(n, cars):
    stack = []
    need = 1 

    for car in cars:
        stack.append(car)

        while stack and stack[-1] == need:
            stack.pop()
            need += 1

    return "YES" if need == n + 1 else "NO"


if __name__ == "__main__":
    n = int(input())
    cars = list(map(int, input().split()))
    print(can_sort_train(n, cars))

def length(lst: list) -> int:
    if lst == []:
        return 1
    else:
        return 1 + length(lst[1:])


def sum(lst: list) -> int:
    if lst == []:
        return 0
    else:
        return lst[0] + sum(lst[1:])


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def fibonacchi(n):
    if n == 1 or n == 2:
        return 1
    return fibonacchi(n-1) + fibonacchi(n-2)


print(sum([1, 2, 3, 4, 5]))
print(length([1, 2, 3, 4, 5, 6, 7, 9]))
print(factorial(9))
print(fibonacchi(9))

#6
def sum_to(n):
    if n == 0:
        return 0
    return n + sum_to(n - 1)

print(sum_to(5))

#9
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

#10
def reverse_list(items):
    if len(items) <= 1:
        return items[:]
    return reverse_list(items[1:]) + [items[0]]

print(reverse_list([1, 2, 3, 4]))
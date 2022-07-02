def print_triangel(n):
    for i in range(1, n + 1):
        print(str("#" * i).rjust(n))


x = print_triangel(6)
print(x)

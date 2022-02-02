def fib_numbers(n):
    fib_num1 = fib_num2 = 1
    if n == 1:
        return fib_num2
    for i in range(2, n):
        fib_num3 = fib_num1 + fib_num2
        fib_num1 = fib_num2
        fib_num2 = fib_num3
    return fib_num2


if __name__ == '__main__':
    print(fib_numbers(3))

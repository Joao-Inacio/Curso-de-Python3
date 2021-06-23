def FizzBuzz(n):
    if (n % 5) == 0 and (n % 3) == 0:
        return f'{n} FizzBuzz'
    if (n % 3) == 0:
        return f'{n} é fizz'
    if (n % 5) == 0:
        return f'{n} buzz'
    return n


print(FizzBuzz(25))

def FizzBuzz(n):
    if (n % 2) == 0:
        return f'{n} é fizz'
    elif (n % 5) == 0:
        return f'{n} buzz'
    elif (n % 5) == 0 and (n % 3) == 0:
        return f'{n} FizzBuzz'
    else:
        return n


print(FizzBuzz(55))

def divisao(x, y):
    """Divisao X e Y

    >>> divisao(25, 5)
    5
    """
    return x / y


def maiuscular(text):
    """Maiuscular texto
    
    >>> maiuscular('texto')
    'TEXTO'
    
    """
    return text.upper()

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

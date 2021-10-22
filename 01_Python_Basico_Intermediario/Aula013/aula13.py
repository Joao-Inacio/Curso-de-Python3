n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
if n1.isdigit() and n2.isdigit():
    n1 = int(n1)
    n2 = int(n2)

    print(n1 + n2)
else:
    print("Números invalidos tente novamente ")

"""print("Hello word!")
print('Olá Mundo!')"""
n1 = int(input("Primeiro Número: "))
n2 = int(input("Segundo Número: "))
op = input("Qual operação você quer fazer:\n"
           "[+] = Soma\n"
           "[-] = Subtração\n"
           "[*] = Multiplicação\n"
           "[/] = Divisão\n"
           ": ")
if op == "+":
    r1 = n1 + n2
    print("O resultado é: ", r1)
elif op == "-":
    r2 = n1 - n2
    print("O resultado é: ", r2)
elif op == "*":
    r3 = n1 * n2
    print("O resultado é: ", r3)
elif op == "/":
    r4 = n1 / n2
    print("O resultado é: ", r4)
else:
    print("Verifique o tipo de operação")




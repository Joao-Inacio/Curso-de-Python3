frase = "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
tamanho_frase = len(frase)
contador = 0
nova_string = ''
while contador < tamanho_frase:
    # print(frase[contador], contador)
    nova_string += frase[contador]
    print(nova_string)
    contador += 1
print(nova_string)

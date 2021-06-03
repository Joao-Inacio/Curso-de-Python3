try:
    horas = int(input('Que horas é: '))
    if horas >= 0 and horas <= 11 :
        print('Olá Bom Dia!')
    elif horas >= 12 and horas <= 17:
        print('Uma Boa Tarde')
    elif horas >= 18 and horas <= 23:
        print('Tenha uma Boa Noite')
except:
    print('Horas invalidas ')


def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError, NameError):
            print('\033[31mERRO : Digite um numero inteiro valido.\033[m')
        except(KeyboardInterrupt):
            print('\033[31mUsuario preferiu não digitar o valor ')
        else:
            return num
            break


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except(ValueError, TypeError, NameError):
            print('\033[31mERRo : Digite um numero real valido\033[m')
        except(KeyboardInterrupt):
            print('\033[31mUsuario preferiu não digitar valor ')
        else:
            return num
            break


def linha(tamanho):
    print('-' * tamanho)


def cabecalho(msg, tamanho):
    linha(tamanho)
    print(f'{msg:^{tamanho}}')
    linha(tamanho)


def menu(titulo,lista, tamanho=0):
    cabecalho(titulo,tamanho)
    c=1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    linha(tamanho)
    opc = leiaint('\033[33mSua opção:\033[m')
    return opc

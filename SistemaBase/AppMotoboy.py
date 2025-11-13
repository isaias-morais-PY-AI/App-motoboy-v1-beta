from time import sleep
from SistemaBase.utilidades import *
from SistemaBase.cadastros import *

#verificçao de docs
verificao_inicial()

# calendario

data = datetime.now().date()
calendario = data.strftime('%d/%m/%Y')

# Progama pricipal
print(calendario)
while True:
    resposta_menu = menu("MENU PRINCIPAL",['Registrar dia', 'Abastecimento', 'Historico', 'moto', 'Sair do sistema'], 45)


    match resposta_menu:
        # Primeiro caso regitra dia
        case 1:
            registrardia(calendario)
        # Segundo caso registra abastecimento
        case 2:
            registro_abastecimento_(calendario,)
        #Historicos
        case 3:
            while True:
                resposta_historico = menu('HISTORICO',['Dia','abastecimentos','manutencoes' ,'menu principal'],45)
                match resposta_historico:
                    case 1:
                        historico_dia()
                    case 2:
                        historico_abastecimento()
                    case 3:
                        historico_manutencoes()
                    case 4:
                        break
                    case _:
                        print('\033[31mDIGITE UMA OPCÃO VALIDA\033[m')
        #Menu de moto
        case 4:
            while True:
                resposta_moto = menu('MOTO',['Configuracoes','Manutençoes','Menu princial'],45)
                match resposta_moto:
                    case 1:
                        configuracao_moto()
                    case 2:
                        manutençao(calendario)
                        break
                    case 3:
                        break
                    case _:
                        print('\033[31mDIGITE UMA OPÇÃO VALIDA\033[m ')
        #sai do sitema
        case 5:
            cabecalho('SAINDO DO SISTEMA...', 45)
            print('ate logo...')
            break
        case _:
            print('\033[31mDIGITE UMA OPÇÃO VALIDA\033[m ')
    sleep(2)



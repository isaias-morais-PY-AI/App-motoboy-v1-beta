import json
from string import whitespace

from SistemaBase.inteface import *
from SistemaBase.cadastros import *


def verificao_inicial():
    if not verificarDoc('dados.json'):
        criarDoc('dados')

    if not verificarDoc('historico.json'):
        criarDoc('historico')

    if not verificarDoc('abastecimento.json'):
        criarDoc('abastecimento')

    if not verificarDoc('manutencao.json'):
        criarDoc('manutencao')

    if not verifiarq('dados.json'):
        nome = str(input('Digite seu Nome: ')).strip()
        moto = str(input('Qual modelo da sua moto? : ')).strip()
        consumo = leiaint('Quantos Km em media ela faz por litro? :')
        gas = leiafloat('Qual preço da gasolina na sua regiao?: R$')

        while True:
            resp = str(input('Sabe quanto ela gasta de manutencao por km? [S/N] ')).lower().strip()
            resp = resp[0]
            if resp == 's':
                manu = leiafloat('Quantos em centavos ela faz por km? R$ ')
                break
            elif resp == 'n':
                print('obs:recomendamos fazer uma pesquisa breve para conseguimos ter o maximo de precisao\n Altere na aba (Moto) o valor de manutencao por km')
                manu = 0.15
                break
            else:
                print('Digite somente s ou n')
        cadastrarUser(nome, moto, consumo, manu, gas)
        print("Cadastro concluido com sucesso. ")



def calculoliquido (bruto,km, gasto = False):

    with open('dados.json','r',encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    gasolina_km = dados[0]['moto']['preco_gasolina']/dados[0]['moto']['consumo_medio']
    manutencao_km = dados[0]['moto']['custo_manutencao']
    custo_totalKM = (manutencao_km + gasolina_km) * km
    liquido = bruto - custo_totalKM
    if gasto == False:
        return liquido
    elif gasto == True:
        return custo_totalKM

def registrardia(data, arquivo='historico.json'):
    strdata = str(data)
    cabecalho('REGISTRAR DIA', 45)
    if verificardia(data, 'historico.json'):
        print('Dia ja cadastrado')
    else:
        kmrodados = leiafloat("Quantos KM vc rodou hj?")
        lucrobruto = leiafloat('Quanto voce faturou hoje? : R$')
        horas = leiaint('Quantas horas foram rodadas?')
        minutos = leiaint('e minutos ?:')
        horasrodadas = horas + (minutos) / 60
        horasstr = f'{horas}:{minutos}'
        calculoliquido(lucrobruto, kmrodados)
        totliquido = calculoliquido(lucrobruto, kmrodados)
        gastos_dia = calculoliquido(lucrobruto, kmrodados, True)
        ganho_hora = lucrobruto / horasrodadas
        ganho_km = lucrobruto/kmrodados

        try:
            with open(arquivo ,'r', encoding='utf-8') as f:
                historico = json.load(f)
        except:
            historico = []

        novo_dia = {
                'data': (strdata),
                'dia': {
                    'kmrodados': kmrodados,
                    'horasrodadas': horasrodadas,
                    'horasstr': horasstr,
                    'lucrobruto': lucrobruto,
                    'ganho_hora': ganho_hora,
                    "ganho_km": ganho_km,
                    'Custo_dia':gastos_dia,
                    'lucroliquido':totliquido,


                }
            }
        #salva dia completo de volta no arquivo
        historico.append(novo_dia)
        with open("historico.json", "w", encoding="utf-8") as f:
            json.dump(historico, f, ensure_ascii=False, indent=4)
            linha(45)
            print(f'{"Bruto:":<10} {lucrobruto:>30.2f}')
            print(f'{"Ganhos p/Hora:":<10} {ganho_hora:>30.2f}')
            print(f'{"Ganhos p/Km:":<10} {ganho_km:>30.2f}')
            print(f'{"Custo:":<10} {gastos_dia:>30.2f}')
            print(f'{"Liquido:":<10} {totliquido:>30.2f}')
        linha(45)
        print('Dia cadastrado com Sucesso')



def registro_abastecimento_(data,arquivo="abastecimento.json"):
    data_str =str(data)
    cabecalho('ABASTECIMENTO', 45)

    posto = str(input("onde voce absteceu? : "))
    litros = leiafloat("Quantos litro voce abasteceu?")
    valor_total = leiafloat('Quanto foi? : R$')
    vlitro = leiafloat('Quanto por litro? : R$')
    try:
        with open(arquivo, "r", encoding='utf-8') as f:
            abastecimento = json.load(f)
    except:
        abastecimento = []


    novo_abastecimento ={
        'data':str(data),
        'abastecimento':{
            'posto':posto,
            'litros':litros,
            'valor_total':valor_total,
            'preco_litro':vlitro
        }
    }

    abastecimento.append(novo_abastecimento)

    with open('abastecimento.json','w',encoding='utf-8') as f1:
        json.dump(abastecimento,f1 , ensure_ascii=False,indent=4)
    print('Abatecimento registrado com sucesso ')

    with open("dados.json", 'r', encoding='utf-8') as f2:
        dados = json.load(f2)

        dados[0]['moto']['preco_gasolina'] = vlitro

    with open("dados.json", 'w', encoding='utf-8') as aqv:
        json.dump(dados, aqv, indent=4, ensure_ascii=False)


def manutençao(data,arquivo='manutencao.json'):
    datastr = str(data)

    cabecalho('manutençao',45)
    item = str(input('Item : '))
    valor = leiafloat("Valor : R$ ")

    try:
        with open(arquivo ,'r',encoding='utf-8') as f:
            manutencao = json.load(f)
    except:
        manutencao = []

    novo_registro = {
        'data':str(data),
        'manutencao':{
            'peca':item,
            'valor':valor
        }
    }
    manutencao.append(novo_registro)

    with open('manutencao.json','w', encoding='utf-8') as f2:
        json.dump(manutencao,f2, ensure_ascii=False,indent=4)
    print('Manutenção registrada com sucesso')


def configuracao_moto(arquivo='dados.json'):
    while True:

        with open(arquivo, 'r',encoding='utf-8') as f:
            moto = json.load(f)
        c = 1
        for item in moto[0]['moto']:
           print(f"\033[33m{c}\033[m - \033[34m{item:<20} {':':^} {moto[0]['moto'][item]:>20}\033[m")
           c+=1
        print(f"\033[33m{'5'}\033[m - \033[34m{'voltar':<20}\033[m")
        linha(45)

        opc = leiaint("\033[33mSua opção:\033[m")

        match opc :
            case 1:
                alteracao = str(input('Digite o novo modelo : '))
                moto[0]['moto']['modelo'] = alteracao
            case 2:
                alteracao = str(input('Digite o novo consumo : '))
                moto[0]['moto']['consumo_medio'] = alteracao
            case 3 :
                alteracao = str(input('Digite o novo custo manutenção : '))
                moto[0]['moto']['custo_manutencao'] = alteracao
            case 4 :
                alteracao = str(input('Digite o novo preço de gasolina : '))
                moto[0]['moto']['preco_gasolina'] = alteracao
            case 5 :
                break
            case _:
                print('\033[31mDIGITE UMA OPÇÃO VALIDA\033[m ')

        with open('dados.json', 'w', encoding='utf-8') as f:
            json.dump(moto, f, ensure_ascii=False, indent=4)

        print('Alteração feita com sucesso ')


def coleta_dia():
    while True:
        dia = leiaint('DIA:\033[33mdd/\033[mmm/aaaa:')
        if dia <1 or dia >31 :
            print('Digite dia valido')
            continue
        else:
            break
    while True:
        mes = leiaint('MES:dd/\033[33mmm\033[m/aaaa:')
        if mes <1 or mes >12:
            print("digite mes valido")
            continue
        else:
            break
    while True:
        ano =str(input('ANO:dd/mm/\033[33maaaa\033[m:')).strip()
        if len(ano) <4 or len(ano) >4:
            print('Digite ano valido ')
        else:
            break
    ano_f = (f'{dia}/{mes}/{ano}')
    ano_format = str(ano_f)
    return ano_format


def historico_dia():
    data_dia = coleta_dia()

    try:
        with open('historico.json', 'r', encoding='utf-8') as historico:
         arq = json.load(historico)

        verific = False
        for item in arq:
            if item['data'] == data_dia:
                print(f'Exibindo historico do dia {data_dia}')
                linha(45)

                for chave,dado in item['dia'].items():
                    if isinstance(dado,(float)):
                        print(f'{chave:<15} {dado:.2f}')

                    else:
                        print(f'{chave:<15} {dado}')
                verific = True
                break

        if not verific:
            print('\033[31mDia não cadastrado\033[m')

    except FileNotFoundError:
        print('\033[31mArquivo não encontrado\033[m')
    except json.JSONDecodeError:
        print('\033[31mArquivo corrompido\033[m')

def historico_abastecimento():
    data = coleta_dia()

    try:
        with open('abastecimento.json','r', encoding='utf-8') as f:
            abastecimentos = json.load(f)

        verific=False
        print(f'Exibindo historico de abastecimento do dia {data}')
        for item in abastecimentos:
            if item['data'] == data:
                linha(45)

                for chave, dado in item['abastecimento'].items():
                    if isinstance(dado,(float)):
                        print(f'{chave:<15} {dado:.2f}')

                    else:
                        print(f'{chave:<15} {dado}')
                verific = True
                linha(45)
        if not verific:
            print('\033[31mDia não cadastrado\033[m')

    except FileNotFoundError:
        print('\033[31mArquivo não encontrado\033[m')
    except json.JSONDecodeError:
        print('\033[31mArquivo corrompido\033[m')

def historico_manutencoes():
    data = coleta_dia()

    try:
        with open('manutencao.json','r', encoding='utf-8') as f:
            manu = json.load(f)

        verific=False
        print(f'Exibindo historico de manutençoes do dia {data}')
        for item in manu:
            if item['data'] == data:
                linha(45)

                for chave, dado in item['manutencao'].items():
                    if isinstance(dado,(float)):
                        print(f'{chave:<15} {dado:.2f}')

                    else:
                        print(f'{chave:<15} {dado}')
                verific = True
                linha(45)
        if not verific:
            print('\033[31mDia não cadastrado\033[m')

    except FileNotFoundError:
        print('\033[31mArquivo não encontrado\033[m')
    except json.JSONDecodeError:
        print('\033[31mArquivo corrompido\033[m')


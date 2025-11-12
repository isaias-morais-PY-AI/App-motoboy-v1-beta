import json
from json import JSONDecodeError
from datetime import datetime,date


def verificarDoc(nome):
    '''
    :param nome: para verificar o nome do usuario
    :return: True siginifica q nao exite ysuario com o nome cadastrado
    '''
    try:
        a =open(nome,"rt")
        a.close()
    except:
        return False
    else:
        return True


def verificardia(data,arquivo='historico.json'):
    data = str(data)
    if isinstance(data, datetime):
        data_str = data.date().isoformat()
    elif isinstance(data, date):
        data_str = data.isoformat()
    else:
        data_str = str(data).split()[0]
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            historico = json.load(f)
    except(FileNotFoundError,JSONDecodeError):
        return False

    for registro in historico:
        registro_data_parte = str(registro['data']).split()[0]
        if registro_data_parte == data_str:
                print(f'dia {data_str} ja cadastrado')
                return True
    return False


# crai json
def criarDoc(nome):
    '''
    :param nome: vai criar arquivo com o nome
    :return: cria arquivo.json com nome
    '''
    try:
        with open(f"{nome}.json", "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo,indent=4)
    except:
        print('\033[31mErro na criacao do arquivo\033[m')
    else:
        print('Arquivo criado com sucesso')

# cadastra o usuario
def cadastrarUser( nome, modelo_moto,consumo_medio, custo_manutencao=0.15,gas=0 ):
    '''
    :param nome: nome do usuario
    :param modelo_moto: cadastra moto
    :param consumo_medio: comsumo medio por km
    :param custo_manutencao: custo medio em centavos por km
    :return: salva cadstro em json
    '''
    try:
        with open('dados.json',"r", encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except:FileNotFoundError
    dados = []
    novo_cadastro = {
            'nome': nome,
            'moto' : {
                "modelo": modelo_moto,
                "consumo_medio": consumo_medio,
                "custo_manutencao": custo_manutencao,
                'preco_gasolina': gas,
                    }   }
    dados.append(novo_cadastro)

    # Salva a lista completa de volta no arquivo
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    print(f"Usuário {nome} cadastrado com sucesso!")


def historico(nome):
    print()


def verifiarq(arquivo):
    a = True
    try:
        with open(arquivo, "r", encoding="utf-8") as arquivo:
            arquivo = json.load(arquivo)
    except:
        a = False
    finally:
        return a






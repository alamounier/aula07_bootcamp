import csv 

path_arquivo = 'vendas.csv'
vendas_itens: list[dict]

def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    """
    Função que lê um arquivo .csv e retorna uma lista de dicionários
    """
    lista = []
    with open(nome_arquivo_csv, mode= "r", encoding= "UTF-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    """
    Função que filtra produtos onde entrega = True
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("Entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

def somar_valores_dos_produtos(lista_produtos_entregues: list[dict]) -> int:
    """
    Função que retorna a quantidade total vendida dos produtos entregues
    """
    quantidade_total = 0
    for produto in lista_produtos_entregues:
        quantidade_total += int(produto.get("Venda"))
    return quantidade_total

def soma(valor_1_para_somar: float, valor_2_para_somar: float = 10) -> float:
    """ 
    Uma função simples de soma de valores do tipo float que retorna float
    """
    
    resultado_da_soma = valor_1_para_somar + valor_2_para_somar
    return resultado_da_soma

valor_1 = 5.75
valor_2 = 6.85
valor_4 = 2.87
valor_5 = 9.68

valor_3 = soma(valor_1_para_somar = valor_1,valor_2_para_somar = valor_2)
valor_6 = soma(valor_4,valor_5)
valor_7 = soma(valor_4)

print(valor_3)
print(valor_6)
print(valor_7)

import json

with open('dados.json') as faturamento_mensal:
    dados_faturamento = json.load(faturamento_mensal)

#Função que armazena os valores diários faturados dentro de um array/list e  retira os dias não faturados
def converte_dados():
    lista_ganhos = []
    for x in dados_faturamento:
        if x["valor"] != 0:
            lista_ganhos.append(x["valor"])
    return lista_ganhos


#Função que verifica o dia de menor faturamento
def menor_valor_faturado():
    menor_valor = min(converte_dados)
    print(f'\nO MENOR valor faturado no mês foi de {menor_valor:.2f}.')


#Função que verifica o dia de maior faturamento. OBS: PODERIA USAR A FUNÇÃO MAX(), MAIS OBTEI POR UTILIZAR  A LÓGICA
def maior_valor_faturado():
    maior_valor = 0
    for x in converte_dados():
        if x > maior_valor:
            maior_valor = x
    print(f'\nO MAIOR valor faturado no mês foi de R${maior_valor:.2f}.')


#Calcula a média mensal de faturamento do mês
def calcula_media_mensal():
    lucro_mensal = 0
    for x in converte_dados():
        lucro_mensal += x
    media_mensal = lucro_mensal / len(converte_dados())
    return media_mensal

#Calcula a quantidade de dias que o lucro diário superou a média mensal
def calcula_dias_superados():
    dias_superados = 0
    for x in converte_dados():
        if x < calcula_media_mensal():
            dias_superados += 1
    print(f'\nA quantidade de dias que o lucro diário superou a média mensal foi de {dias_superados} dias.')

menor_valor_faturado()
maior_valor_faturado()
calcula_dias_superados()



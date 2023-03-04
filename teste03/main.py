'''
Teste 03
 Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média

'''
import json

with open('dados.json') as faturamento_mensal:
    dados_faturamento = json.load(faturamento_mensal)

contador_dias = 1
lista_ganhos = []
menor_valor = 1000000000
maior_valor = 0

'Transformando os dados em uma array/list para facilitar a extração das informações'
for x in dados_faturamento:
    lista_ganhos.append(x["valor"])

'Descobrindo o MENOR VALOR'
for y in lista_ganhos:
    if y != 0 and y < menor_valor:
        menor_valor = y

'Descobrindo o MAIOR VALOR'
for y in lista_ganhos:
    if y > maior_valor:
        maior_valor = y

print(f'O MENOR valor faturado no mês foi de R${menor_valor:.2f}')
print(f'O MAIOR valor faturado no mês foi de R${maior_valor:.2f}')


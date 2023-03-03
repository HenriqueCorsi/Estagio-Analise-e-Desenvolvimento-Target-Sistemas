'''
Teste 02
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código
'''

fibonacci_sequence = [0, 1]
index_value01 = 0
index_value02 = 1
user_input = int(input('\nDigite o valor que gostaria de verificar: '))


while len(fibonacci_sequence) <= 20:
    next_number = fibonacci_sequence[index_value01] + fibonacci_sequence[index_value02]
    fibonacci_sequence.append(next_number)
    index_value01 += 1
    index_value02 += 1


if user_input in fibonacci_sequence:
    print(f'\nO Valor {user_input} ESTÁ dentro da sequência')
else:
    print(f'\nO Valor {user_input} NÃO ESTÁ dentro da sequência')

print(f'\nEstá é a sequencia: \n{fibonacci_sequence}')



    




    
















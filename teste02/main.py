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



    




    
















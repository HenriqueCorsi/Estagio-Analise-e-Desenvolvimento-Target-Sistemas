regional_values = {
        "SP": 67836.43, 
        "RJ": 36678.66, 
        "MG": 29229.88, 
        "ES": 27165.48, 
        "OUTROS": 19849.53
        }


# Calculado o total mensal de cada estado
def calculate_monthly_total():
    amount_list = []
    for x in regional_values.values():
        amount_list.append(x)
    amount_total = sum(amount_list)
    return amount_total


# Calcula o percentual de cada estado
def calculate_percentage():
    percentage_list = []
    for x in regional_values.values():
        percentage = (x / calculate_monthly_total()) * 100
        percentage_list.append(percentage)
    return percentage_list


# Exibi percentual de cada estado
def display_list():
    states = []
    count = 0
    for x in regional_values.keys():
        states.append(x)
    print(F'FATURAMENTO TOTAL -> {calculate_monthly_total()}')
    for i in calculate_percentage():
        count += 1
        print(f'{states[count - 1]} -> {i:.2f}%')


display_list()
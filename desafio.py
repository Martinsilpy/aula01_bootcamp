# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o seu bônus: "))

# 4) Calcule o valor do bônus final
constate_bonus = 1000
valor_do_bonus = constate_bonus + salario_usuario * bonus_usuario

# 5) Imprima cálculo do KPI para o usuário


# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"O usuário {nome_usuario} possui o bônus de {valor_do_bonus}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
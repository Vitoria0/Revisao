# Faça um Programa que pergunte quanto você ganha por hora e o número de horas de trabalhadas no mês.
# Calcule e mostre o total do seu salário no mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salario_hora = float(input('Quanto você recebe por hora? '))
horas_mes = int(input('Quantas horas você trabalha por mês? '))
salario_bruto = salario_hora * horas_mes
imposto_renda = salario_bruto * 11 / 100
inss = salario_bruto * 8 / 100
sindicato = salario_bruto * 0.5 / 100
salario_liquido = salario_bruto - imposto_renda - inss - sindicato
print(f'Se você ganha R${salario_hora} por hora e trabalha {horas_mes} horas por mês')
print(f'Seu salário bruto é {salario_bruto:.2f}')
print(f'Você paga R${imposto_renda:.2f} ao imposto de renda')
print(f'Você paga R${inss:.2f} ao INSS')
print(f'Você paga R${sindicato:.2f} ao Sindicato')
print(f'Sendo assim seu salário liquido é R${salario_liquido:.2f}')
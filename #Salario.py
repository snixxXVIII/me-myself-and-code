#Salario

#valor por hora de trabalho
X = float(input('Insira valor da hora de trabalho: '))

#total de horas trabalhadas
Y = float(input('Insira o total de horas trabalhadas: '))

#valor total
T = X * Y

#descontos
I = T * 0.11
N = T * 0.08
S = T * 0.05

#desconto total
D = I + N + S

#valor final
F = T - D

print('Seu salario bruto: ', T, ' reais')

print('Desconto INSS: ', N, ' reais')

print('Desconto sindicato: ', S, ' reais')

print('Seu salário liquido e de :', F, ' reais')
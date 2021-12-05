#Faça um algoritimo que pergunte quanto você ganha por hora e quantas horas trabalhou neste mês
#Entrada
valor_por_hora = float(input('Digite o quanto ganha por hora: '))
horas_trabalhadas = int(input('Digite quantas horas trabalhou: '))
#Processamento
salario = (valor_por_hora * horas_trabalhadas)
#saida
print('Neste mês você vai receber: R${0:.2f}'.format(salario))
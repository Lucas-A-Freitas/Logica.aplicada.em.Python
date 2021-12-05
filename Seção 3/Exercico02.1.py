#Faça um algoritimo que calcule o estoque médio de uma peça
#Entrada
quantidade_maxima = int(input('Digite a quantidade maxima: '))
quantidade_minima = int(input('Digite a quantidade minima: '))
#processamento
estoque_medio = (quantidade_maxima + quantidade_minima) / 2
#saida
print('O estoque médio é: {0}'.format(estoque_medio))
"""
Ranges:
-conhecendo o loop for para usar os ranges
-conhecendo o range pra trabalha melhor com os loops for

Ranges são utilizados para gerar sequencias numericas não de forma aleatoria
mas sim de maneira especificada

Formas gerais:

range(valor_de_parada)

obs: valor_De_parada não inclusive (incio padrão 0, e passo de 1 em 1)
"""
#Forma 1 ele irá começar de 0 até 10

for num in range(11):
    print(num)

#Forma 02
range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo de 1 em 1)
#NESSE CASO ELE VAI ESPECIFICO NO VALOR 1 INDICADO ATÉ O 10
for num in range(1, 11):
    print(num)

#Forma 03
for num in range (5, 55 , 5):
    print(num)
Ele irá contar em 05 e 05

#Forma 04 será igual a 03,somente será inverse
#(valor final para valor incico )

for num in range(10, 0, -1):
    print(num)






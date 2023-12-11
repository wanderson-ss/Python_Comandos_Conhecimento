"""
saindo de loops com break
Utilizamos o brak para sair de loops de maneira forçada  ou de maneira projetada.
Testando ele com o while e com for 

"""

# Exemplo 1 
# exemplo abaixo é uma utilização forçada do break para parar o loop


for numero in range(1, 111):
   if numero == 18:
       break
   else:
        print(numero)
print('Sair do loop')

# Exemplo 2

while True:
    comando = input("DIGITE 'sair'para sair: ")
    if comando == 'sair':
        break

"""Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
отломить k долек, если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no """

n = int(input('Введите колиество долек по горизонтали: '))
m = int(input('Введите колиество долек по вертикали: '))
k = int(input('Введите колиество долек которые хотим отломить: '))
    
if n*m<k:
    print('число долек больше, чем есть в шоколадке')
else:
    print(f'{k%n==0 or k%m==0}')
        

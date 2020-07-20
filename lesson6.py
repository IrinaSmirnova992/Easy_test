print("Введите цену в рублях")
A= int(input())
print("Введите копейки")
B= int(input())
print("Введите кол-во")
N = int(input())
cost = N * (100 * A + B)
print( "Сумма", cost // 100, "руб",  cost % 100, "коп")


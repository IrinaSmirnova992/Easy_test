print("Введите кол-во минут")
n = int(input())
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, "ч", minutes, "м")

# Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
# За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
# Выведите одно число – минимальное число операций, после применения которых в строке s
# не останется вхождений строки a, или Impossible, если операций потребуется более 1000.

s = input()
a = input()
b = input()

counter = 0
if (s.count(a) == 0) :
    print(0)
    exit()
if (a == b):
    print("Impossible")
    exit()

# пока заменять есть что продолжаем
while s.count(a) != 0:
    s = s.replace(a, b)
    counter = counter + 1
    if counter == 1000:
        print("Impossible")
        exit()

print(counter)


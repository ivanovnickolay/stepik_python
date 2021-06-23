number = 213312

cnt = 0
num = number
while num > 0:
    num = num // 10
    cnt += 1
if cnt % 2 != 0:
    cnt =- 1
palin = True
while cnt > 0:
    first = number // pow(10, cnt - 1)
    last = (number % 10)

    if first != last:
        palin = False
        break
    cnt = cnt - 1
    number = (number // 10 ) - first*pow(10, cnt - 1)
    cnt = cnt - 1

if palin:
    print('Palindrome')
else:
    print("No Palindrome")

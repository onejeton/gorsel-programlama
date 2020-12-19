count = 0
for i in range(100, 999, 1):
    i = str(i)

    number1 = i[0]
    number2 = i[1]
    number3 = i[2]

    if not number1 == number2 and not number1 == number3 and not number2 == number3:
        print(i)
        count = count + 1

print('Toplam : ', count)
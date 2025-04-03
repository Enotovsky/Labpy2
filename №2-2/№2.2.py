from multiprocessing.managers import Value

try:
    num1 = float(input())
    num2 = float(input())
    if num2 == 0:
        print("Ошибка")
    else:
        res = num1 / num2
        print(res)
except ValueError:
    print("Ошибка")
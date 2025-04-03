with open("data.txt", "r") as file:
    num = [int(x.strip()) for x in file]
print(num)

sum = sum(num)
average = sum/10
max = max(num)
min = min(num)

with open("result.txt", "w", encoding="utf-8") as file:
    file.write(f"Сумма: {sum}\n")
    file.write(f"Среднее: {average}\n")
    file.write(f"Максимум:{max}\n")
    file.write(f"Минимум: {min}\n")
file.close()
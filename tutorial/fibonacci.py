num1 = 0
num2 = 1
count = 20

series = f"{num1} {num2}"

for i in range(count-2):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    series += f' {num3}'

print(series)
#  5 , 1, 2,,3 out = 3

def frog(n,a):
    stone = 0
    for i in range(len(a)):
        if n > 0:
            path = a[i]
            n -= path
            stone += 1
    return stone

n = int(input("Enter distance: "))
a = []
for i in range(n):
    a.append(int(input("Enter a number: ")))

result = frog(n, a)

print(result)

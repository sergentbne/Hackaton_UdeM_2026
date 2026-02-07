n = int(input())
a = []
for _ in range(n):
    line = input()
    tokens = line.split()
    a.append(tokens)


total = []
numb = []
for pos, _ in enumerate(a[0]):
    if a[1][pos] == a[2][pos]:
        numb.append(pos)
total.append(numb)
one_zero = []
for i in numb:
    if a[0][int(i)] == "1":
        one_zero.append(1)
    else:
        one_zero.append(0)

total.append(one_zero)
print(total)


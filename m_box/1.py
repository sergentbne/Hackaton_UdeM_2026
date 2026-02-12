n = int(input())
a = []
for _ in range(n):
    line = input()
    tokens = line.split()
    a.append(tokens)


numb = []
for pos, _ in enumerate(a[0]):
    if a[0][pos] == a[1][pos]:
        numb.append(pos)

print(numb)

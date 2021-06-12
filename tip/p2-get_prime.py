n = int(input())

check_list = [0] * (n + 1)

count = 0
for i in range(2, n + 1):
    if check_list[i] == 0:
        count += 1
        for j in range(i, n + 1, i):
            check_list[j] = 1

print(count)


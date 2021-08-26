import time

def sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total



start = time.time()

for _ in range(10):
    sum(10 ** 6)

end_time = time.time()

print((end_time - start) / 10)
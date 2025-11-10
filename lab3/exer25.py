def fatores(n):
    return [x for x in range(1, n) if n % x == 0]

def perfects(n):
    return [x for x in range(1, n+1) if sum(fatores(x)) == x]

print(fatores(300))
print(perfects(300))
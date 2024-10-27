C, Q = map(int, input().split())

if C == 1:
    valor = Q*4
elif C == 2:
    valor = Q*4.5
elif C == 3:
    valor = Q*5
elif C == 4:
    valor = Q*2
else:
    valor = Q*1.5

print(f'Total: R$ {valor:.2f}')
och, zaoch = 0, 0
n = int(input())
for i in range(n):
    int_i = input(f"int_{i+1}: ").split()  
    if len(int_i) == 4:
        if int_i[3] == 'True': och += 1
        else: zaoch += 1
print('out:', och, zaoch)
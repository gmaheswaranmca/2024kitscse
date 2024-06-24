N = int(input('Enter number of term:'))

term = 2
diff = 1
for I in range(N):
    print(f'{term} ',end='')
    term = term + diff 
    diff += 1
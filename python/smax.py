a = int(input('First Number:'))
b = int(input('Second Number:'))
c = int(input('Third Number:'))

if a > b and a > c:
    max = a 
elif b > c:
    max = b 
else:
    max = c

if a < b and a < c:
    min = a 
elif b < c:
    min = b 
else:
    min = c

smax = (a + b + c) - max - min 
print(f'the second max of {a},{b},{c} is {smax}')

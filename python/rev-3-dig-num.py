N = int(input())    #123

Digit1 = N//100     #1
N=N%100             #23
Digit2 = N//10      #2
Digit3 = N%10       #3
R = Digit3 * 100 + Digit2 * 10 + Digit1
print(R)
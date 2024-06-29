N = int(input())
if len(str(N)) != 3:
    print("Invalid Number")
else:
    M = (N//10) % 10
    if M % 3 == 0:
        print("Trendy Number")
    else:
        print("Not a Trendy Number")
gcd = lambda int1, int2: int1 if int2 == 0 else gcd(int2, int1 % int2)

int1 : int
int2 : int

int1 = int(input('Enter first integer: '))
int2 = int(input('Enter second integer: '))

print(gcd(int1, int2))

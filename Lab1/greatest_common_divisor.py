import time

gcd = lambda int1, int2: int1 if int2 == 0 else gcd(int2, int1 % int2)

int1 : int
int2 : int

int1 = int(input('Enter first integer: '))
int2 = int(input('Enter second integer: '))

start_time = time.process_time()
greatest_common_divisor = gcd(int1, int2)
gcd_time = time.process_time() - start_time

print(greatest_common_divisor)
print(f'Time taken: {gcd_time}')

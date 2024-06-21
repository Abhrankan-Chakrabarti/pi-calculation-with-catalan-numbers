from gmpy2 import mpz
import sys

# Input: Number of digits to compute
digits = mpz(eval(input('How many digits of π? :\t')))

# Number of iterations to ensure sufficient precision
iters = digits * 5 // 3

# Initialize variables
pi = mpz()
c = d1 = d2 = m = mpz(1)

# Calculation loop
for i in range(2, iters + 2):
    pi *= 16 * (m + 2)
    pi += c * m * d2
    c = 2 * c * m // i
    d1 *= 16
    m += 2
    d2 *= m
    if i % 1000 == 0:
        print("\r%d terms..." % i, end='')

# Scaling and final adjustment
one = mpz(10)**digits
pi = 6 * pi * one // (d1 * d2) + 3 * one

# Formatting the result
pi_digits = f'{pi//one}.' + str(pi%one).zfill(digits)

# Handling logging to a file if specified in command-line arguments
if sys.argv[1:2] in (['-l'], ['--log']):
    with open((sys.argv[2:3] or [f'pi{digits}.txt'])[0], 'w') as f:
        f.write(pi_digits)
else:
    print(f'\rπ = {pi_digits}...∞')
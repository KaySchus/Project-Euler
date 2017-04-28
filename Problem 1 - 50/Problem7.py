import math

def sieve_of_eratosthenes(limit = 125000):
	sieve = [True] * limit
	sieve[0] = sieve[1] = False

	for (i, isprime) in enumerate(sieve):
		if (isprime):
			for n in range(i * i, limit, i):
				sieve[n] = False
	return sieve

prime_count = 0
for (i, isprime) in enumerate(sieve_of_eratosthenes()):
	if isprime: 
		prime_count += 1

		if (prime_count == 10001):
			print(i)
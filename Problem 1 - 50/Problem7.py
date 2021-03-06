import math

def sieve(limit = 125000):
	sieve = [True] * limit
	sieve[0] = sieve[1] = False
	primes = []

	for (i, isprime) in enumerate(sieve):
		if (isprime):
			primes.append(i)
			for n in range(i * i, limit, i):
				sieve[n] = False

	return primes

target = 10001
primes = sieve()
print(primes[target - 1])
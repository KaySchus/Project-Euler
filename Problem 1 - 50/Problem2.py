def fib_even_sum_it1(max):
	result = 0
	i = 1
	j = 1

	while (j < max):
		if (j % 2 == 0):
			result += j

		k = i + j
		i = j
		j = k

	return result

print(fib_even_sum_it1(4000000))
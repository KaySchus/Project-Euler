def factor_it1(target):
	factor = 2
	last_factor = 1

	while target > 1:
		if target % factor == 0:
			last_factor = factor
			target = target // factor

			while target % factor == 0:
				target = target // factor

		factor += 1

	return last_factor

print(factor_it1(600851475143))
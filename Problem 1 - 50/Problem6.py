def square_of_sum(target):
	val = target * (target + 1) / 2
	return int(val * val)

def sum_of_square(target):
	val = target * (target + 1) * (2 * target + 1) / 6
	return int(val)

print(square_of_sum(100) - sum_of_square(100))
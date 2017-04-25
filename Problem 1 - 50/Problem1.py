def sum_multiples(target, val1, val2):
    result = 0
    
    for i in range(1, target):
        if (i % val1 == 0) or (i % val2 == 0):
            result += i

    return result

print(sum_multiples(1000, 3, 5))

def sum_multiple(target, value):
	result = 0

	for i in range(1, target):
		if (i % value == 0):
			result += i

	return result

final = sum_multiple(1000, 3) + sum_multiple(1000, 5) - sum_multiple(1000, 15)
print(final)
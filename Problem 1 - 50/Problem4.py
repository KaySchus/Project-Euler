def find_palindrome_max_multiples(minimum, maximum):
	largest_palindrome = 0
	for i in range(minimum, maximum):
		for j in range(minimum, maximum):
			if is_palindrome(i * j) and (i * j > largest_palindrome):
				largest_palindrome = i * j

	return largest_palindrome

def is_palindrome(number):
	rev = 0
	ori = number
	while ori > 0:
		rev = rev * 10 + (ori % 10)
		ori = ori // 10

	return rev == number

def num_digits(num):
	ori = num
	digs = 0
	while ori > 0:
		ori = ori // 10
		digs += 1

	return digs

print(find_palindrome_max_multiples(100, 999))
print(num_digits(1000))

# Given an integer, return a boolean whether if it is a power of 2
# Input: Int
# Output: Bool

# Test Case: 
# Input: 8
# Output: True

# 2 4 8 16 32 64 128 

# Calculate power of 2s
# 	 Check if current number is equal to input Value
# 		Return true
# 		Check if input value is greater than current value
# 			Return false

def is_pow(x):
	current_number = 2
	while x:
		if current_number  x:
			return False
		elif current_number == x:
			return True
		current_number = current_number * 2

# Variable Table


#  Iteration	current_number
#  1				2
#  2				4
#  3				8


def is_pow(x):

	if x == 1:
		return True
	elif x < 1:
		return False
	else:
		return is_pow(x/2)

print(is_pow(20))

# Variable Table


#  Iteration	x	
#  1			x/2	
#  2			x/2
#  3			x/2

# Input: [Int]
# Output: Int
# Test Case:
# Input: [1,1,1,0,0,1,1]
# Output: 3


def longest_ones(arr):
	counter = 0
	ones = []

	for i in arr:
		if i == 1:
			counter += 1
		else:
			ones.append(counter)
			counter = 0

	return max(ones)


print(longest_ones([1,1,1,0,0,1,1]))


# Variable Table


#  Iteration	counter		ones	
#  1			0			[]
#  2			1			[]
#  3			2			[]
#  4			3			[]
#  5 			0			[3]
#  6 			0			[3]
#  7			1			[3]
#  8			2			[3]





# import time

# def countdown(s):
#     while s:
#         mins,secs = divmod(s, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print (timer, end="\r")
#         time.sleep(1)
#         s -=1
#     print("Happy Monday")
# s = input("Enter the time in seconds: ")
# countdown(int(s))


def countIndex(A, N):

	# Stores the maximum integer in A[]
	MAX = max(A)

	# Stores the frequency of each
	# element in the array A[]
	freq = [0 for i in range(MAX+1)]

	for i in range(N):
		if A[i] in freq:
			freq[A[i]] += 1
		else:
			freq[A[i]] = 1

	# Stores the valid integers in A[]
	# for all integers from 1 to MAX
	res = [0 for i in range(MAX+1)]

	for i in range(1, MAX + 1, 1):
		for j in range(i, MAX + 1, i):
		
			# Case where P = Q
			if (i == j):
			
				# Subtract 1 because P & Q
				# cannot have same index
				res[i] += (freq[j] - 1)
			else:
				# Case 1
				res[i] += freq[j]

				# Case 2
				res[j] += freq[i]

	# Loop to print answer for
	# each index of array A[]
	for i in range(N):
		print(res[A[i]],end = " ")

# Driver Code
if __name__ == '__main__':
	A = [1, 3, 4, 2, 6]
	N = len(A)

	# Function Call
	countIndex(A, N)
	
	# This code is contributed by SURENDRA_GANGWAR.




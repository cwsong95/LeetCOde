#   Uses Sieve of Eratostheness
#   Steps:
#         - Define a boolean array of size n and set all elements to True except 0, 1
#             - isPrime = [False, False, True, true, True, ..]
#       	- Start a loop with index i from 2 to square root of N
# 			- Loop as I from 2 till sqrt(N)
#		- 
class Solution:
	def countPrimes(self, n):
		if(n<2):
			return 0
		isPrime = [True] * n
		isPrime[0] = isPrime[1] = False

		for i in range(2, int(math.ceil(math.sqrt(n)))): ****** MEMORIZE!!
			if(isPrime[i]):
				for multiples_of_i in range(i*i, n, i): ****** MEMORIZE!!
					isPrime[multiples_of_i] = False

		return sum(isPrime)     
    #True = 1
    #False = 0
    #since we need to know the number of prime, we use sum() function to get sum
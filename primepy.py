def is_prime_numbers (n):
	if n < 0:

        else:
            for x in range (2, n+1):
		    for i in range(2, x):
                        if x % i == 0:
                            break
                        else:
                            primes.append(x)
                            if primes!=[]:
                                return primes
                            else:
                                return ("The output cannot be an empty list")
                

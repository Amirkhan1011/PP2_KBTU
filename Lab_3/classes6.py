class Filter_prime():
    def isPrime(self, num):
        if (num < 2):
            return False
        else:
            for i in range(2, num):
                if(num % i == 0):
                    return False
        return True   

    def filter_primes(self, list):
        return filter(lambda x : self.isPrime(x), list)

filter = Filter_prime()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = list(filter.filter_primes(nums))
print(primes)
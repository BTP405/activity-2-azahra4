def is_prime(num):
    squareroot = int(num**0.5) # to check for prime we just need to check if the number num is divisible by numbers between 2 - squareroot of (num)
    #print("This is squareroot: ", squareroot)
    return num > 1 and all(num % i != 0 for i in range(2, squareroot + 1))

def getPrimeNumbers(n):
    return [num for num in range(2, n + 1) if is_prime(num)]

print(getPrimeNumbers(13))
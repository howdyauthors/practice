def nextprime(n):

    while True:
        n += 1
        if n % 2 != 0:
            for i in range (2, n + 1):
                if n % i == 0:
                    if i == n:
                        return n
                    break
        elif n == 2 or n == 1:
            return n
def is_prime(num):

    for i in range(num):
        if num % i == 0:
            return False

    i += 1

    return True


print(is_prime(2))
print(is_prime(10))

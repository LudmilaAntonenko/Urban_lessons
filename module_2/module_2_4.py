# Цикл for
print('Задача "Всё не так уж просто":')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for elem in numbers:
    is_prime = True
    for divizor in range(2, elem):
        if elem % divizor == 0:
            is_prime = False
            not_primes.append(elem)
            break

    if is_prime == True and elem != 1:
        primes.append(elem)

print('Primes:', primes)
print('Not primes:', not_primes)

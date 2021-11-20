# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# remove the element at index 2
removed_element = prime_numbers.pop(2)

print('Removed Element:', removed_element)

numbers = []
prime_numbers.pop(1)
numbers.append(prime_numbers)
print(numbers)
import random

def generate_random_numbers(count, min_val, max_val):
    numbers = set()
    while len(numbers) < count:
        num = random.randint(min_val, max_val)

        numbers.add(num)
    return list(numbers)

list1 = generate_random_numbers(5, -5, 5)
list2 = generate_random_numbers(5, -5, 5)

print("List 1:", list1)
print("List 2:", list2)

common_elements = list(set(list1) & set(list2))
print("Common Elements:", common_elements)

all_elements = list(set(list1 + list2))

print("All Elements from List 1 and List 2 without repetition is :")
print(all_elements)
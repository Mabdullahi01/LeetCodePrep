#my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#list[start:end:step]

#print (my_list[-2:1:-1]) # step of -1 is just a way to print reversed values

#print(my_list[:3:-1])


# sample_url = 'http://coreyms.com'
#
# print(sample_url)
#
# print(sample_url[::-1])
#
# print(sample_url[-4:])
#

#LIST COMPREHENSION

#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #Using this for all the codes down below

# I want 'n' for each 'n' in nums
# my_list = []
#
# for n in nums:
#     my_list.append(n)
# print(my_list)

#Using list Comprehension
# my_list = [n for n in nums]
# print(my_list)

#I want 'n*n' for each n in nums

# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

#Using list comprehension
# my_list = []
#
# my_list = [n*n for n in nums]
# print(my_list)


# I want 'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)

#Using list comprehension
# my_list = []
# my_list = [n for n in nums if n%2 == 0] # I want an item(n) for each item(n) in nums if the item is even
# print(my_list)


# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'

# my_list = []
# for letter in "abcd":
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

#Using List comprehension
# my_list = []
# my_list = [(letter, num) for letter in 'abcd'  for num in range(4)]
# print(my_list)


#DICTIONARY COMPREHENSION


# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
#print(list(zip(names, heros)))

# I want a dict{'name', 'hero'} for each name, hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)

#Using dictionary comprehension
# my_dict = {name: hero for name, hero in zip(names, heros)}
# print(my_dict)

# If name is not equal to peter

# my_dict = {}
# for name, hero in zip(names, heros):
#     if name != 'Peter':
#         my_dict[name] = hero
# print(my_dict)

# Using dictionary comprehension
# my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
# print(my_dict)


#SET COMPREHENSION
#nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

#Using set comprehension
# my_set = {n for n in nums}
# print(my_set)

#GENERATOR EXPRESSIONS

#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# I want to yield 'n*n' for each 'n' in nums

# def gen_func(nums):
#     for n in nums:
#         yield n*n
#
# my_gen = gen_func(nums)
# print(list(my_gen))

# Using Generator expression
# my_gen = (n*n for n in nums)
#
# print(list(my_gen))










































# # conditionals in python

# is_old = True
# is_licenced = True

# if is_old and is_licenced:
#   print('You are old enough to drive, and you have a licence!')

# else:
#   print('you are not of age!')

# print('okok')

# Ternary Operator

#condition_if_true if condition else condition_if_else

# is_friend = False

# can_message = "message allowed" if is_friend else "not allowed to message"

# Short Circuiting

# is_Friend = True

# is_User = False

# if is_Friend or is_User:
#   print('best friends forever')

# Logical Operators
# print(0 != 1)

####### Logical Operators ########
# < > == <= >= !=
# and or not

### EXERCISE ON LOGICAL OPERATOR ###

# is_magician = True
# is_expert = True

# #check if magician AND expert: "You are a master magician"

# #check if magician but not expert: "At least you are getting there"

# # if you're  not a magician: "You need magic powers"

# if is_magician and is_expert:
#   print("You are a master magician")

# elif is_magician and not is_expert:
#   print("At least you are getting there")

# elif not is_magician:
#   print("You need magic powers")

##### is vs == #####

# print(True is True)
# print('1' == 1)
# print([] is [])
# print(10 == 10)

###### For Loop #####
# for item in (1, 2, 3, 4, 5):
#   for x in ['a', 'b', 'c']:
#     print(1, x)

##### Iterable #####
#iterable - list, dictionary, tuple, set, string
#iterable -> one by one check each item in the collection

# user = {'name': 'Golem', 'age': 5006, 'can_swim': False}

# for key, value in user.items():
#   print(key, value)

# for items in user.values():
#   print(items)

# for items in user.keys():
#   print(items)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# counter = 0

# for items in my_list:
#   counter = counter + items
# print(counter)

# ###### Range #####
# for _ in range(0, 10, 2):
#   print(_)

#   print(range(100))
# In for loop we can use (_) if we dont want to use the number variable in the given loop and we can also stepover a

########## Enumerate ############
#It's used to show the index of a number or a character

# for i, char in enumerate(list(range(100))):
#   print(i, char)
#   if char == 50:
#     print(f'index of 50 is ${char}')

######### While Loop ############

# i = 0

# while i < 50:
#   print(i)
#   i += 1
# else:
#   print("Done with all the work")

# my_list = [1, 2, 3]
# for item in my_list:
#   print(item)

# i = 0

# while i < len(my_list):
#   print(my_list)
#   i += 1

# while True:
#   response = input('Say Something: ')
#   if (response == 'bye'):
#     break

# ######### GUI Exercise ########
# picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
#            [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]

# fill = '*'
# empty = ' '

# for image in picture:
#   for pixel in image:
#     if (pixel):
#       print(fill, end='')
#     else:
#       print(empty, end='')
#   print('')

# Exercise: Check for duplicates in list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

print(duplicates)

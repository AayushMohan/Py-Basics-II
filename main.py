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

is_magician = True
is_expert = True

#check if magician AND expert: "You are a master magician"

#check if magician but not expert: "At least you are getting there"

# if you're  not a magician: "You need magic powers"

if is_magician and is_expert:
  print("You are a master magician")

elif is_magician and not is_expert:
  print("At least you are getting there")

elif not is_magician:
  print("You need magic powers")
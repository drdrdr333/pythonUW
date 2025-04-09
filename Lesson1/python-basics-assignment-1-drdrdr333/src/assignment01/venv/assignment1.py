# '''
# 1.
# '''
# #i.
# my_string = "new string"

# #ii.
# my_integer = 2

# #iii.
# my_float = 4.5

# '''
# 2.
# '''
# #i.
# my_integer1 = 1

# my_integer2 = 4

# sum = my_integer1 + my_integer2

# #ii.
# #Expected value of sum = 5

# #iii.
# print(sum)


# '''
# 3.
# '''
# #i.
# float1 = 3.2

# float2 = 2.2

# float_total = float1 + float2

# #ii.
# #Expected value of float_total = 5.4

# #iii.
# print(float_total)


# '''
# 4.
# '''

# #i.
# string1 = "Hello"

# string2 = "World"

# hello_world = string1 + " " + string2

# #ii
# #Expected value of hello_world = "Hello World"

# #iii
# print(hello_world)


'''
5.
'''
# #i.
# float1 = 4.5
# my_integer1 = 4
# int_plus_float = float1 + my_integer1

# #Expected value of int_plus_float = 4.2

# #ii.

# print(int_plus_float)

# #iii.
# # float
# print(type(int_plus_float))

'''
6.
'''
#i.

#iv
#int_plus_string = my_integer1 + string1

#Expected value of int_plus_string = error


#ii.

#iv.
#print(int_plus_string)

#iii.

'''
Output value was a typerror. Strings and integers are not meant to be added together because the interpreter does not know how to 'add' the two -- it is ambiguous. Interpreter is unable to decide whether to concatenate or perform mathematical operation. "Zen of Python" see above for iv.
'''


'''
------------------------------------
PART II
'''

# '''
# 1.
# '''
# my_string = "hello"
# my_integer = 4
# my_float = 5.5
# print(type(my_string), "****", type(my_integer), "***", type(my_float))


# '''
# 2.
# '''

# #i.
# string_integer = "4"

# #ii
# integer_string = int(string_integer)

# #iii
# print(integer_string)

# '''
# 3.
# '''
# value = round((5 * 7.654321), 3)
# print(value)

# '''
# 4.
# '''

# my_name = input("Enter your name: ")

# #i.

# print(my_name)


'''
5.
'''

favorite_number = input("Enter your favorite number: ")

#i.
print(favorite_number)

#ii.
#currently, it depends upon what the user types... - we'd need some sort of error correction if they typed something other than an integer, if thats what we wanted to restrict the input to **I was incorrect! items are converted to a str

#iii.
print(type(favorite_number))


'''
6.
'''

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")


#i.
sum_of_numbers = number1 + number2

#ii.
#string concatenation of the two inputs

#iii.
print(sum_of_numbers)


#iv.
#output value was the concatenation of two strings, this is because, as we learned in the last task, input function converts the type to a string!

#v.
correct_sum = int(number1) + int(number2)

#vi.
print(correct_sum)
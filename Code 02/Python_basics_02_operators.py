# Create a Variable
x = 3.14
print(type(x))

# Math Operators
# +, -, *, /, %, //, **
a = 2
b = 16
sum = a + b
print(f'Sum of two variables is {sum}')

difference = a - b
print(f'Difference of two variables is {difference}')

multiplication = a * b
print(f'Multiplication of two variables is {multiplication}')

division = a / b
print(f'Division of two variables is {division}')

modulo = a % b
print(f'Modulo of two variables is {modulo}')

double_divide = a // b # What this is doing?
print(f'Double divide of two variables is {double_divide}')

power = a ** b
print(f'Power of two variables is {power}')

# Logical Operators
# and, or, not
# Add positive number -> True
condition_1 = a > 0 and b > 0
print(f'Result of Condition 1 is {condition_1}')

condiion_2 = a == 0 or b > 0
print(f'Result of Condition 2 is {condiion_2}')

# not -> inverse of given operand
condiion_3 = not a
print(f'Result of Condition 3 is {condiion_3}')

x = 10
print(x > 5 and x < 20)

# Assignment Operators
# =, +=, -=, *=, /=
# = -> simple assignment
# += -> add and assign
x += 10
print(f'Value of x is {x}')
x -= 5
print(f'Value of x is {x}')
x *= 5
print(f'Value of x is {x}')
x /= 5
print(f'Value of x is {x}')

'''
Multiline Comment
'''

'''
Bit-Wise Operators
convert respective operands in binary and then perform operation
& bitwise and, | bitwise or, ~, ^ xor, << left shift, >> right shift, 
'''
a = 5 # 101
b = 3 # 011
print(f'Result of Bitwise and is {a & b}') # bit by bit comparison 001
print(f'Result of Bitwise or is {a | b}') # 111
print(f'Result of Bitwise xor is {a ^ b}') # 110
print(f'Result of Bitwise ~ is {~b}') # single operand, ~b = -(b+1)
print(f'Result of Bitwise << is {a << b}') # multiply by 2**b
print(f'Result of Bitwise >> is {a >> b}') # division by 2**b

# name1 = "Hi"
# name2 = 'Hi'
# print(f'Bitwise and on String : {name1 & name2}')

# Membership Operators
# in (present or not), not in (inverse of in),
# Check if letter is present in a str
print('a' in 'Ans') # case-sensitive
print('a' not in 'Ans')


# Identity Operators => Checks memory location, not just value
# is (same object), is not (inverse of is, different object)
list_x = [1,2]
list_y = list_x
print(f'Location of list_x is {id(list_x)}')
list_y.append(3)
print(f'Location of list_x is {id(list_x)}')
print(f'Location of list_y is {id(list_y)}')
print(f'Comparison Result based on identity is : {list_x is list_y}')

list_x = [1,2]
list_y = [1, 2]
print(f'Location of list_x is {id(list_x)}')
print(f'Location of list_y is {id(list_y)}')
print(f'Comparison Result based on identity is : {list_x is list_y}')
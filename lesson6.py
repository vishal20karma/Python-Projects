# important logical operators (not, and, or)
# not: Inverts the Boolean value. not True is False. (Highest precedence)
# and: Returns True if both operands are true. True and False is False. (Second Highest precedence)
# or: Returns True if at least one operand is true. True or False is True. (Last precdence)

# Example with precedence: not True and False or True
""" 
'not True' means false - result is False
then False with 'and False' - result is False
then False with 'or True' - result is True
Final result - True (any condition True in python result True)
"""
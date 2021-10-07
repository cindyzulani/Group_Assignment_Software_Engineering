"""
Function determines odd and even number
Group members: Cindy Zulani & Niken Ayuning Tyas
"""


# num() function is to determine if a number is odd or even. this function returns output as odd or even number.
def num(a):
    if a % 2 == 0:
        output = "even number"
    else:
        output = "odd number"
    return output


# to take user input
a = int(input('Enter the number: '))
output = num(a)
# print if the number that user's input is odd or even
print('{} is {}'.format(a, output))

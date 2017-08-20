#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3

n = 5

s =""

# if n%2 != 0:
#     print('Weird')
# elif n%2 == 0:
#     if (n < 5 & n > 2) | n > 20:
#         print('Not Weird')
#     else:
#         print('Weird')

if n % 2 == 0 and (n in range(2,6) or n > 20):
    s = "Not "
s += "Weird"
print(s)

x=0
while x < n:
    print(x**2)
    x += 1
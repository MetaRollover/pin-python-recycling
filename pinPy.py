'''
This program is designed to take a pin number as an input
but store each number in a single variable and print them
out to you. The idea is that some machines don't have enough
memory built into them in order to store long variables, so
instead, you just reuse the same variable over and over to,
in effect, "recycle" it.
'''

string = ""
n = 0

string = input("Please enter your pin number: ")

for s in string:
    n = n * 10
    n = n + int(s)

print(n)

#Why did we need to use a second integer in the first place?

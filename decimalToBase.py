from stackmodule import Stack

def DecToBase(decnum, base):

    digits = '0123456789ABCDEF'

    remstack = Stack()

    while decnum > 0:

        rem = decnum%base

        remstack.push(rem)
        decnum = decnum//base

    newstring = ""

    while not remstack.isempty():
        newstring += digits[remstack.pop()]

    return newstring

print(DecToBase(25,16))
print(DecToBase(25,2))
print(DecToBase(25,8))
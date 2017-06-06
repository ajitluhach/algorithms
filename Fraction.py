class Fraction:


    def __init__(self, num, deno):
        self.num = num
        self.deno = deno

    def __str__(self):
        return (str(self.num) + "/" + str(self.deno))

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.deno + self.deno*otherfraction.num
        newdeno = self.deno*otherfraction.deno
        common = gcd(newnum, newdeno)
        return Fraction(newnum//common, newdeno//common)

    def __sub__(self, other):
        newnum = self.num*other.deno - self.deno*other.num
        newdeno = self.deno*other.deno
        common = gcd(newnum, newdeno)
        return Fraction(newnum/common, newdeno/common)

    def __eq__(self, other):
        return self.num == other.num and self.deno == other.deno

    def __div__(self, other):
        newnum = self.num * other.deno
        newdeno = self.deno * other.num
        common = gcd(newnum, newdeno)
        return Fraction(newnum // common, newdeno // common)

    def __mul__(self, other):
        newnum = self.num*other.num
        newdeno = self.deno*other.deno
        common = gcd(newnum, newdeno)
        return Fraction(newnum//common, newdeno//common)

    def __ne__(self, other):
        return self.num != other.num or self.deno != other.deno

    def __gt__(self, other):
        new1 = self.num*other.deno
        new2 = self.deno*other.num
        return new1 > new2

    def __lt__(self, other):
        new1 = self.num*other.deno
        new2 = self.deno*other.num
        return new1 < new2

    def __ge__(self, other):
        new1 = self.num*other.deno
        new2 = self.deno*other.num
        return new1 >= new2

    def __le__(self, other):
        new1 = self.num*other.deno
        new2 = self.deno*other.num
        return new1 <= new2

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = n
        n = oldm%oldn
    return n



f1 = Fraction(1,2)
f2 = Fraction(3,5)
j= Fraction(3,2)
print(f1==f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)
print(f1>=j)

Fraction(3,5) <= Fraction(3,2)

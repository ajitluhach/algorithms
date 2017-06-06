import timeit


def test1():
    l = []
    for i in range(10000):
        l = l + [i]

def test2():
    l = []
    for i in range(10000):
        l.append(i)

def test3():
    l = [i for i in range(10000)]

def test4():
    l = list(range(10000))

print("Concat ", timeit.timeit(test1, number = 100))
print("Range in for loop append: ",timeit.timeit(test2, number = 100))
print("list comp: ",timeit.timeit(test3, number = 100))
print("Range : " ,timeit.timeit(test1, number = 100))

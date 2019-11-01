class A(object):
    def __init__(self, list):
        self.test = list


l = [1, 2, 3]
a = A(l)
print(a.test)

l.append(4)
print(a.test)

k = 5
b = A(k)
print(b.test)
k = k + 1
print(b.test)



class X(object):
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3


x = X()
c = A(x)
print(c.test.a)
x.a = 4
print(c.test.a)


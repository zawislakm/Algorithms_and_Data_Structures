# Find maximum party value
class Employee:
    def __init__(self, fun):
        self.emp = []
        self.fun = fun
        self.f = -1
        self.g = -1
        self.invited = False


def f(v: Employee) -> int:
    if v.f > 0:
        return v.f
    x = v.fun
    for u in v.emp:
        x += g(u)
    y = g(v)
    v.f = max(x, y)
    return v.f


def g(v: Employee) -> int:
    if v.g > 0:
        return v.g
    x = 0
    for u in v.emp:
        x += f(u)
    v.g = x

    return v.g

# Party Tree
a50 = Employee(50)
b10 = Employee(10)
b20 = Employee(20)
b1 = Employee(1)
a50.emp.extend([b10, b20, b1])

c18 = Employee(18)
c5 = Employee(5)
c23 = Employee(23)
b10.emp.extend([c18, c5, c23])

c21 = Employee(21)
c17 = Employee(17)
b20.emp.extend([c21, c17])

c1 = Employee(1)
c2 = Employee(2)
b1.emp.extend([c1, c2])

d25 = Employee(25)
d36 = Employee(36)
d7 = Employee(7)
c18.emp.extend([d25, d36, d7])

d18 = Employee(18)
d1_1 = Employee(1)
d5 = Employee(5)
c21.emp.extend([d18, d1_1, d5])

d1_2 = Employee(1)
d1_3 = Employee(1)
c1.emp.extend([d1_2, d1_3])

d1_4 = Employee(1)
c2.emp.append(d1_4)

e100_1 = Employee(100)
e100_2 = Employee(100)
e100_3 = Employee(100)
d7.emp.extend([e100_1, e100_2, e100_3])

print(f(a50))


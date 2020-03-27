origin = [0, 0]

def create(pos=origin):
    def player(directions, step):
        new_x = pos[0] + directions[0] * step
        new_y = pos[1] + directions[1] * step
        pos[0] = new_x
        pos[1] = new_y
        return pos
    return player


# stp_0 = create()
# stp_1 = create(pos=[1, 0])
#
# print(stp_0([1, 0], 10), stp_1([0, 0], 10))
# print(stp_0([-1, 1], 20))



# funcs = [lambda x: x + n for n in range(5)]
# for f in funcs:
#     print(f(3))


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print("Computing area")
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        return 2 * math.pi * self.radius

# cc = Circle(2)
# print(cc.__dict__)
#
# print(cc.area, cc.perimeter)
# print(cc.__dict__)

# from numpy import array
#
# a = array([[1,2,3], [4,5,6]])
# b = array([[4,5,6],[7,8,9]])
#
# print(a + b)

# c = [[1,2,3], [4,5,6]]
# d = [[4,5,6],[7,8,9]]
#
# print(c + d)









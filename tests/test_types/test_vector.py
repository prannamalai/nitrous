import unittest2 as unittest

from nitrous.module import module
from nitrous.function import function
from nitrous.types import Float, Pointer
from nitrous.types.vector import Vector, load, store, get_element, set_element

FloatP = Pointer(Float)
Float4 = Vector(Float, 4)

load4f = load(Float4)
store4f = store(Float4)

get4f = get_element(Float4)
set4f = set_element(Float4)


@function(Float, a=Float, b=Float, c=Float, d=Float)
def hadd4(a, b, c, d):
    v = Float4()

    v = set4f(v, 0, a)
    v = set4f(v, 1, b)
    v = set4f(v, 2, c)
    v = set4f(v, 3, d)

    return get4f(v, 0) + get4f(v, 1) + get4f(v, 2) + get4f(v, 3)


@function(a=FloatP, p=FloatP, y=FloatP, z=FloatP)
def axpy(a, p, y, z):
    store4f(load4f(a) * load4f(p) + load4f(y), z)


class VectorTests(unittest.TestCase):

    def test_get_set(self):

        m = module([hadd4])
        self.assertEqual(m.hadd4(3, 11, 13, 17), 44)

    def test_math(self):

        m = module([axpy])

        a = (Float.c_type * 4)(1, 2, 3, 4)
        y = (Float.c_type * 4)(100, 200, 300, 400)
        z = (Float.c_type * 4)()

        # a * a + y -> z
        m.axpy(a, a, y, z)
        self.assertEqual(list(z), [101, 204, 309, 416])

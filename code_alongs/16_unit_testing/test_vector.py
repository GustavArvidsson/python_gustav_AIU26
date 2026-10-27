from vector import Vector
from pytest import raises

def test_valid_init():
    v = Vector(1,2,3)
    assert v.numbers == (1,2,3)

def test_invalid_init():
    with raises(TypeError):
        Vector(1,2,"3")

def test_invalid_empty_vector():
    with raises(ValueError):
        Vector()

def test_addition():
    v1 = Vector(1,2,3)
    v2 = Vector(1,2,3)
    result = v1+v2
    assert result.numbers == (2,4,6)


def test_invalid_adding_two_types():
    v1 = Vector(1,3,5)

    for right_operand in [(1,2,3), "just a string", [1,2,3]]:
        with raises(TypeError):
            v1 + right_operand

def test_subtration():
    v1 = Vector(1,2)
    v2 = Vector(-5,3)
    result = v1-v2
    assert result.numbers == (6,-1)

def test_multiplication():
    v = Vector(1,2)
    result = v*5
    assert result.numbers == (5,10)

    result = 5*v
    assert result.numbers == (5,10)
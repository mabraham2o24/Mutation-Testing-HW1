import pytest
from Polynomial import Polynomial  # Import the Polynomial class from your module

def test_init():
    poly = Polynomial([3, 0, 2])
    assert poly.coefficients == [3, 0, 2]

def test_str():
    poly = Polynomial([3, 0, 2])
    assert str(poly) == "3x^2 + 2"

    poly2 = Polynomial([1, -1])
    assert str(poly2) == "1x + -1"

    poly3 = Polynomial([0, 0, 0])
    assert str(poly3) == "0" or str(poly3) == ""

def test_add():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [3, 1, 1]

def test_sub():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_diff = poly1 - poly2
    assert poly_diff.coefficients == [3,-1, 3]

def test_mul():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_product = poly1 * poly2
    assert poly_product.coefficients == [3, -3, 2, -2]

def test_first_degree_polynomial():
    poly = Polynomial([2, -3])  # Represents 2x - 3
    root = poly.find_root_bisection(0, 5)
    assert abs(root - 1.5) < 1e-6

def test_second_degree_polynomial():
    poly = Polynomial([1, 0, -2])  # Represents x^2 - 2
    root = poly.find_root_bisection(1, 2)
    assert abs(root - 2.0**0.5) < 1e-6

def test_third_degree_polynomial():
    poly = Polynomial([1, 0, -2, 0])  # Represents x^3 - 2x
    root = poly.find_root_bisection(-2, 2)
    assert abs(root - 0.0) < 1e-6
   

def test_evaluate():
    poly = Polynomial([3, 0, 2])
    assert poly.evaluate(2) == 14  # 3x^2 + 2, x=2 -> 3*4 + 2 = 14


def test_derivative_empty_polynomial():
    poly = Polynomial([])  # Represents an empty polynomial

    # Test derivative calculation for an empty polynomial
    der = poly.get_derivative_coefficients()
    assert der == []  # Derivative of an empty polynomial should also be empty

def test_find_root_bisection_invalid_interval():
    poly = Polynomial([1, 0, -2])  # Represents x^2 - 2

    # Test bisection method with invalid interval (where root doesn't exist)
    with pytest.raises(ValueError):
        root = poly.find_root_bisection(2, 3)  # Interval does not contain a root



def test_empty_polynomial():
    poly = Polynomial([])  # Represents an empty polynomial

    # Test string representation of an empty polynomial
    assert str(poly) == "0"

def test_negative_degree_polynomial():
    poly = Polynomial([1, 2, 3])  # Represents x^2 + 2x + 3

    # Test string representation of a polynomial with negative degree
    assert str(poly) == "1x^2 + 2x + 3"

def test_add_empty_polynomial():
    poly = Polynomial([1, 2, 3])  # Represents x^2 + 2x + 3
    empty_poly = Polynomial([])  # Represents an empty polynomial

    # Test adding an empty polynomial to another polynomial
    result = poly + empty_poly
    assert result.coefficients == [1, 2, 3]

def test_evaluate_empty_polynomial():
    poly = Polynomial([])  # Represents an empty polynomial

    # Test evaluating an empty polynomial
    assert poly.evaluate(5) == 0



def test_sub_empty_polynomial():
    poly = Polynomial([1, 2, 3])  # Represents x^2 + 2x + 3
    empty_poly = Polynomial([])  # Represents an empty polynomial

    # Test subtracting an empty polynomial from another polynomial
    result = poly - empty_poly
    assert result.coefficients == [1, 2, 3]


def test_evaluate_first_degree_polynomial():
    poly = Polynomial([2, -3])  # Represents 2x - 3

    # Test evaluating a first-degree polynomial at x=1
    assert poly.evaluate(1) == -1

def test_evaluate_second_degree_polynomial():
    poly = Polynomial([1, -5, 6])  # Represents x^2 - 5x + 6

    # Test evaluating a second-degree polynomial at x=3
    assert poly.evaluate(3) == 0





def test_evaluate_first_degree_polynomial():
    poly = Polynomial([2, -3])  # Represents 2x - 3

    # Test evaluating a first-degree polynomial at x=1
    assert poly.evaluate(1) == -1

def test_evaluate_second_degree_polynomial():
    poly = Polynomial([1, -5, 6])  # Represents x^2 - 5x + 6

    # Test evaluating a second-degree polynomial at x=3
    assert poly.evaluate(3) == 0

def test_sub_empty_polynomial():
    poly = Polynomial([1, 2, 3])  # Represents x^2 + 2x + 3
    empty_poly = Polynomial([])  # Represents an empty polynomial

    # Test subtracting an empty polynomial from another polynomial
    result = poly - empty_poly
    assert result.coefficients == [1, 2, 3]

def test_evaluate_empty_polynomial():
    poly = Polynomial([])  # Represents an empty polynomial

    # Test evaluating an empty polynomial
    assert poly.evaluate(5) == 0

def test_add_empty_polynomial():
    poly = Polynomial([1, 2, 3])  # Represents x^2 + 2x + 3
    empty_poly = Polynomial([])  # Represents an empty polynomial

    # Test adding an empty polynomial to another polynomial
    result = poly + empty_poly
    assert result.coefficients == [1, 2, 3]

def test_empty_polynomial():
    poly = Polynomial([])  # Represents an empty polynomial

    # Test string representation of an empty polynomial
    assert str(poly) == "0"

def test_negative_degree_polynomial():
    poly = Polynomial([1, 2, 3])  # Represents x^2 + 2x + 3

    # Test string representation of a polynomial with negative degree
    assert str(poly) == "1x^2 + 2x + 3"
















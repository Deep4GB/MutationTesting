from Polynomial import Polynomial 
from mutation_operators import Wrapper

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
    assert poly_diff.coefficients == [3, -1, 3]


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


# Test the behavior of the Wrapper class when initializing with mutated coefficients
def test_wrapper_mutated_initialization():
    mutated_poly = Wrapper([3, 0, 2])
    assert mutated_poly.coefficients != [3, 0, 2]  # Mutated coefficients

# Test the string representation of the Polynomial object after mutation through Wrapper class
def test_wrapper_mutated_string_representation():
    mutated_poly = Wrapper([3, 0, 2])
    assert str(mutated_poly) != "3x^2 + 2"  # Mutated __str__ representation

# Test the addition operation after mutation through Wrapper class
def test_wrapper_mutated_addition():
    poly1 = Wrapper([3, 0, 2])
    poly2 = Wrapper([1, -1])

    # Mutated addition
    poly_sum = poly1 + poly2
    assert poly_sum.coefficients != [3, 1, 1]  # Mutated addition

# Test the subtraction operation after mutation through Wrapper class
def test_wrapper_mutated_subtraction():
    poly1 = Wrapper([3, 0, 2])
    poly2 = Wrapper([1, -1])

    poly_diff = poly1 - poly2
    assert poly_diff.coefficients != [3, -1, 3]  # Mutated subtraction

# Test the multiplication operation after mutation through Wrapper class
def test_wrapper_mutated_multiplication():
    poly1 = Wrapper([3, 0, 2])
    poly2 = Wrapper([1, -1])

    # Mutated multiplication
    poly_product = poly1 * poly2
    assert poly_product.coefficients != [3, -3, 2, -2]  # Mutated multiplication

# Test to detect Arithmetic Operator Replacement (AOR) mutation in mutated multiplication operation
def test_wrapper_mutated_multiplication_aor():
    poly1 = Wrapper([3, 0, 2])
    poly2 = Wrapper([1, -1])

    # Mutated multiplication
    poly_product = poly1 * poly2
    assert poly_product.coefficients != [3, -2, 2, -2]  # Mutated multiplication

# Test to verify if zero polynomial string representation returns "0" or ""
def test_zero_polynomial_str_representation():
    zero_poly = Polynomial([0])
    assert str(zero_poly) == "0" or str(zero_poly) == ""

# Test addition with a zero polynomial (identity property)
def test_addition_with_zero_polynomial():
    poly = Polynomial([3, 0, 2])
    zero_poly = Polynomial([0])
    result = poly + zero_poly
    assert result.coefficients == poly.coefficients, "Adding zero polynomial should have no effect"

# Test subtraction of a polynomial by itself (zero polynomial property)
def test_subtraction_of_itself():
    poly = Polynomial([3, 0, 2])
    result = poly - poly
    assert result.coefficients == [0] * len(poly.coefficients), "Subtracting the same polynomial should result in a zero polynomial"

# Test multiplication by zero polynomial (zero property)
def test_multiplication_by_zero():
    poly = Polynomial([3, 0, 2])
    zero_poly = Polynomial([0])
    result = poly * zero_poly
    assert result.coefficients == [0] * (len(poly.coefficients) + len(zero_poly.coefficients) - 1), "Multiplying by zero should result in a zero polynomial"

# Test evaluation of the polynomial at x=0 (constant term)
def test_evaluation_at_zero():
    poly = Polynomial([3, -4, 2])
    assert poly.evaluate(0) == 2, "Evaluating at x=0 should return the constant term"

# Test to verify multiplication of a polynomial by a monomial with a non-unit coefficient
def test_multiply_by_non_unit_monomial():
    poly1 = Polynomial([1, 3, -2])
    poly2 = Polynomial([2, 0])  # Represents 2x
    product = poly1 * poly2
    assert product.coefficients == [2, 6, -4, 0], "Should correctly multiply a polynomial by a monomial with a coefficient other than 1"

# Test to detect an incompetent mutant due to AOR mutation (#4)
def test_incompetent_mutant_4():
    # Incompetent mutant #4: AOR mutation
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    # Check the mutated condition where the mutant survived
    result = poly1 + poly2
    assert result.coefficients != [4, -1, 3], "Should detect the mutated condition"

# Test to detect an incompetent mutant due to AOR mutation (#7)
def test_incompetent_mutant_7():
    # Incompetent mutant #7: AOR mutation
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    # Check the mutated condition where the mutant survived
    result = poly1 + poly2
    assert result.coefficients != [4, 0, 2], "Should detect the mutated condition"

# Test to detect an incompetent mutant due to AOR mutation (#8)
def test_incompetent_mutant_8():
    # Incompetent mutant #8: AOR mutation
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    # Check the mutated condition where the mutant survived
    result = poly1 + poly2
    assert result.coefficients != [4, -1, 2], "Should detect the mutated condition"

# Test for mutated initialization of MutatedPolynomialWrapper to detect IOD mutation
def test_mutated_wrapper_init_iod():
    mutated_poly = Wrapper([3, 0, 2, 1])  # Mutated initialization of MutatedPolynomialWrapper
    assert mutated_poly.coefficients != [3, 0, 2, 1], "Should detect the mutated condition for initialization"

# Test for mutated addition operation (AOR) in MutatedPolynomialWrapper
def test_mutated_wrapper_add_aor():
    poly1 = Wrapper([3, 0, 2])
    poly2 = Wrapper([1, -1])

    # Mutated addition
    poly_sum = poly1 + poly2
    assert poly_sum.coefficients != [3, 1, 2], "Should detect the mutated condition in addition"
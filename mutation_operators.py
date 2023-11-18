import random
import importlib
from Polynomial import Polynomial

# Mutation 1: Modify Coefficients
def modify_coefficients(poly_instance):
    modified_coefficients = [coef + random.randint(-1, 1) for coef in poly_instance.coefficients]
    poly_instance.coefficients = modified_coefficients

# Mutation 2: Adjust Addition Process
def adjust_addition(poly_instance):
    original_add = poly_instance.__add__
    def new_addition(self, other):
        return original_add(self, Polynomial([-coeff for coeff in other.coefficients]))
    poly_instance.__add__ = new_addition.__get__(poly_instance, Polynomial)

# Mutation 3: Introduce Redundancy in Multiplication
def introduce_redundancy(poly_instance):
    original_mul = poly_instance.__mul__
    def new_multiplication(self, other):
        result = original_mul(self, other)
        result.coefficients = [coef + 1 - 1 for coef in result.coefficients]
        return result
    poly_instance.__mul__ = new_multiplication.__get__(poly_instance, Polynomial)

# Mutation 4: Modify Exponent in Evaluation
def modify_evaluation(poly_instance):
    original_evaluate = poly_instance.evaluate
    def new_evaluation(self, x):
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** (len(self.coefficients) - i)) 
        return result
    poly_instance.evaluate = new_evaluation.__get__(poly_instance, Polynomial)

# Function to apply all mutations
def apply_all_mutations(poly_instance):
    modify_coefficients(poly_instance)
    adjust_addition(poly_instance)
    introduce_redundancy(poly_instance)
    modify_evaluation(poly_instance)

source_module = importlib.import_module("Polynomial")
original_polynomial_class = getattr(source_module, "Polynomial")

# Create a wrapper class inheriting from the original Polynomial class
class Wrapper(original_polynomial_class):
    def __init__(self, coefficients):
        super().__init__(coefficients)
        apply_all_mutations(self)

mutated_poly_wrapper = Wrapper([1, 2, 3])
print(mutated_poly_wrapper)

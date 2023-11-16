from copy import deepcopy
import random

class MutationOperators:
    def mutate_coefficient(coefficient, index=0):
        mutation_type = random.choice(["replace", "scale", "add"])
        
        if mutation_type == "replace":
            mutated_coefficient = random.uniform(-10, 10)
        elif mutation_type == "scale":
            mutation_factor = random.uniform(0.5, 1.5)
            mutated_coefficient = coefficient * mutation_factor
        else: 
            mutation_value = random.uniform(-5, 5)
            mutated_coefficient = coefficient + mutation_value

        return mutated_coefficient

    def mutate_arithmetic_operation(poly, operation):
        mutated_poly = deepcopy(poly)
        mutated_poly.coefficients = [operation(coef) for coef in mutated_poly.coefficients]
        return mutated_poly

    def mutate_to_zero_coefficient(poly, index):
        mutated_poly = deepcopy(poly)
        mutated_poly.coefficients[index] = 0
        return mutated_poly

    def introduce_redundant_code(coefficients):
        return [coef * 1 for coef in coefficients]

    def mutate_degree(poly):
        mutated_poly = deepcopy(poly)
        mutated_poly.coefficients.insert(1, 1)
        return mutated_poly

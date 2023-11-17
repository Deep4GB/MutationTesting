from copy import deepcopy

import random


class MutationOperators:

  def mutate_coeff(c, i=0):
    mutation_type = random.choice(["replace", "scale", "add"])
    if mutation_type == "replace":
      mutated_c = random.uniform(-10, 10)

    elif mutation_type == "scale":
      mutation_factor = random.uniform(0.5, 1.5)
      mutated_c = c * mutation_factor

    else:
      mutation_value = random.uniform(-5, 5)
      mutated_c = c + mutation_value

    return mutated_c

  def mutate_arith_op(p, op):
    mutated_p = deepcopy(p)
    mutated_p.coefficients = [op(coef) for coef in mutated_p.coefficients]
    return mutated_p

  def mutate_to_zero_coeff(p, i):
    mutated_p = deepcopy(p)
    mutated_p.coefficients[i] = 0
    return mutated_p

  def introduce_redundant_code(coefs):
    return [coef * 1 for coef in coefs]

  def mutate_degree(p):
    mutated_p = deepcopy(p)
    mutated_p.coefficients.insert(1, 1)
    return mutated_p

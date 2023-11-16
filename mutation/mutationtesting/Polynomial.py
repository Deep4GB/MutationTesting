from mutation_operators import MutationOperators

class Polynomial:
    def __init__(self, coefficients):
        """
        Initialize a polynomial with a list of coefficients. The coefficients list should be in descending order of
        the exponent, for example: [3, 0, 2] represents 3x^2 + 2.
        """
        self.coefficients = coefficients

    def __str__(self):
        if len(self.coefficients) == 0:
            return "0"

        terms = []
        for i, coef in enumerate(reversed(self.coefficients)):
            if coef == 0:
                continue
            term = str(coef)
            if i != 0:
                if i == 1:
                    term += "x"
                else:
                    term += f"x^{i}"
            terms.append(term)

        return " + ".join(terms[::-1])

    def __add__(self, other):
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        result_coefficients = [a + b for a, b in zip(padded_self, padded_other)]
        result_coefficients[0] = MutationOperators.mutate_coefficient(result_coefficients[0], index=0)
        return Polynomial(result_coefficients)

    def __sub__(self, other):
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        result_coefficients = [a - b for a, b in zip(padded_self, padded_other)]
        result_coefficients = [MutationOperators.mutate_coefficient(coef) for coef in result_coefficients]
        return Polynomial(result_coefficients)

    def __mul__(self, other):
        result_deg = len(self.coefficients) + len(other.coefficients) - 1
        result_coefficients = [0] * result_deg
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result_coefficients[i + j] += self.coefficients[i] * other.coefficients[j]
        result_coefficients = MutationOperators.introduce_redundant_code(result_coefficients)
        return Polynomial(result_coefficients)


    def evaluate(self, x):
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** (len(self.coefficients) - i - 1))

        result *= MutationOperators.mutate_coefficient(2)

        return result
    
    def get_derivative_coefficients(self):
        return [i * coef + MutationOperators.mutate_coefficient(1) for (i, coef) in enumerate(list(reversed(self.coefficients))[:-1])]
        

    def find_root_bisection(self, a, b, epsilon=1e-6, max_iterations=100):
        if self.evaluate(a) * self.evaluate(b) > 0:
            return None 

        for _ in range(max_iterations):
            c = (a + b) / 2
            print(c)
            if abs(self.evaluate(c)) < epsilon:
                return c

            if self.evaluate(c) * self.evaluate(a) < 0:
                b = c + MutationOperators.mutate_coefficient(1)
            else:
                a = c - MutationOperators.mutate_coefficient(1)

        return None 

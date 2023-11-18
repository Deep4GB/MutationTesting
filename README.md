# Polynomial Mutation Testing Report

## Introduction
The Polynomial class serves as a fundamental component for manipulating polynomials, allowing various arithmetic operations and evaluations. This report presents an in-depth analysis of mutation testing performed on the Polynomial class and its associated test suite. Mutation testing is a critical technique used to evaluate the quality and effectiveness of the test suite by introducing controlled modifications (mutations) to the source code and assessing how well the test suite can detect these changes.

# 

## Command to run:
``` bash
mut.py --target Polynomial --unit-test PolyTest --runner pytest
```

#

## Defined Mutation Operators
1. **Modify Coefficients**: Adjust coefficients by random values within a specific range.
2. **Adjust Addition Process**: Alter the behavior of the addition operation.
3. **Introduce Redundancy in Multiplication**: Add redundant calculations within the multiplication process.
4. **Modify Exponent in Evaluation**: Change the exponent calculation in the evaluation method.

# 

## Applied Mutations and Impact
The provided `mutation_operators.py` script applies these mutations to the `Polynomial` class. The mutations aim to alter polynomial operations to produce different outcomes or errors.


### Examples of Mutations
- **Mutation 2 (Adjust Addition Process)**: Changes the addition behavior, making it inverse.
- **Mutation 3 (Introduce Redundancy in Multiplication)**: Introduces redundant arithmetic within the multiplication operation.
- **Mutation 4 (Modify Exponent in Evaluation)**: Adjusts the exponent calculation in polynomial evaluation.

# 

## Summary of Mutant Survival and Killing
The mutation testing revealed the following results after executing the test suite against various mutations:

### Output
```bash
Start mutation process:
   - targets: Polynomial
   - tests: PolyTest
2x^2 + 3x + 3
[*] 25 tests passed:
   - PolyTest [0.13258 s]
[*] Start mutants generation and execution:
   - [#   1] AOD Polynomial: [0.12198 s] survived
   - [#   2] AOR Polynomial: [0.11879 s] killed by PolyTest.py::test_str
   - [#   3] AOR Polynomial: [0.11148 s] killed by PolyTest.py::test_str
   - [#   4] AOR Polynomial: [0.12586 s] incompetent
   - [#   5] AOR Polynomial: [0.15237 s] survived
   - [#   6] AOR Polynomial: [0.12836 s] killed by PolyTest.py::test_str
   - [#   7] AOR Polynomial: [0.11551 s] incompetent
   - [#   8] AOR Polynomial: [0.10558 s] incompetent
   - [#   9] AOR Polynomial: [0.12220 s] incompetent
   - [#  10] AOR Polynomial: [0.13239 s] killed by PolyTest.py::test_add
   - [#  11] AOR Polynomial: [0.12298 s] incompetent
   - [#  12] AOR Polynomial: [0.12449 s] incompetent
   - [#  13] AOR Polynomial: [0.12976 s] incompetent
   - [#  14] AOR Polynomial: [0.13139 s] incompetent
   - [#  15] AOR Polynomial: [0.13903 s] killed by PolyTest.py::test_add
   - [#  16] AOR Polynomial: [0.12845 s] incompetent
   - [#  17] AOR Polynomial: [0.12275 s] killed by PolyTest.py::test_add
   - [#  18] AOR Polynomial: [0.14311 s] incompetent
   - [#  19] AOR Polynomial: [0.13358 s] incompetent
   - [#  20] AOR Polynomial: [0.13466 s] incompetent
   - [#  21] AOR Polynomial: [0.13268 s] killed by PolyTest.py::test_sub
   - [#  22] AOR Polynomial: [0.12763 s] incompetent
   - [#  23] AOR Polynomial: [0.13197 s] incompetent
   - [#  24] AOR Polynomial: [0.13362 s] incompetent
   - [#  25] AOR Polynomial: [0.13320 s] incompetent
   - [#  26] AOR Polynomial: [0.13287 s] killed by PolyTest.py::test_sub
   - [#  27] AOR Polynomial: [0.13442 s] incompetent
   - [#  28] AOR Polynomial: [0.13049 s] killed by PolyTest.py::test_sub
   - [#  29] AOR Polynomial: [0.13206 s] killed by PolyTest.py::test_mul
   - [#  30] AOR Polynomial: [0.13220 s] killed by PolyTest.py::test_mul
   - [#  31] AOR Polynomial: [0.12927 s] incompetent
   - [#  32] AOR Polynomial: [0.13610 s] incompetent
   - [#  33] AOR Polynomial: [0.13410 s] incompetent
   - [#  34] AOR Polynomial: [0.13678 s] killed by PolyTest.py::test_mul
   - [#  35] AOR Polynomial: [0.15023 s] killed by PolyTest.py::test_multiplication_by_zero
   - [#  36] AOR Polynomial: [0.14884 s] killed by PolyTest.py::test_wrapper_mutated_string_representation
   - [#  37] AOR Polynomial: [0.14093 s] killed by PolyTest.py::test_mul
   - [#  38] AOR Polynomial: [0.14814 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  39] AOR Polynomial: [0.13697 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  40] AOR Polynomial: [0.13515 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  41] AOR Polynomial: [0.13324 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  42] AOR Polynomial: [0.13200 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  43] AOR Polynomial: [0.14181 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  44] AOR Polynomial: [0.13918 s] survived
   - [#  45] AOR Polynomial: [0.13653 s] survived
   - [#  46] AOR Polynomial: [0.13700 s] survived
   - [#  47] AOR Polynomial: [0.13458 s] survived
   - [#  48] AOR Polynomial: [0.13747 s] survived
   - [#  49] AOR Polynomial: [0.15117 s] killed by PolyTest.py::test_wrapper_mutated_string_representation
   - [#  50] AOR Polynomial: [0.14822 s] killed by PolyTest.py::test_second_degree_polynomial
   - [#  51] AOR Polynomial: [0.13956 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  52] AOR Polynomial: [0.13968 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  53] AOR Polynomial: [0.16877 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  54] AOR Polynomial: [0.12928 s] survived
   - [#  55] AOR Polynomial: [0.12653 s] survived
   - [#  56] AOR Polynomial: [0.13551 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  57] ASR Polynomial: [0.13220 s] incompetent
   - [#  58] ASR Polynomial: [0.12622 s] incompetent
   - [#  59] ASR Polynomial: [0.14069 s] killed by PolyTest.py::test_mul
   - [#  60] ASR Polynomial: [0.15708 s] killed by PolyTest.py::test_evaluation_at_zero
   - [#  61] BCR Polynomial: [0.13438 s] killed by PolyTest.py::test_str
   - [#  62] COI Polynomial: [0.12359 s] killed by PolyTest.py::test_str
   - [#  63] COI Polynomial: [0.12980 s] killed by PolyTest.py::test_str
   - [#  64] COI Polynomial: [0.13510 s] killed by PolyTest.py::test_str
   - [#  65] COI Polynomial: [0.13005 s] killed by PolyTest.py::test_str
   - [#  66] COI Polynomial: [0.14256 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  67] COI Polynomial: [0.13600 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  68] COI Polynomial: [0.13273 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  69] ROR Polynomial: [0.12637 s] killed by PolyTest.py::test_str
   - [#  70] ROR Polynomial: [0.13024 s] killed by PolyTest.py::test_str
   - [#  71] ROR Polynomial: [0.12351 s] killed by PolyTest.py::test_str
   - [#  72] ROR Polynomial: [0.11221 s] killed by PolyTest.py::test_str
   - [#  73] ROR Polynomial: [0.12767 s] killed by PolyTest.py::test_str
   - [#  74] ROR Polynomial: [0.14180 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  75] ROR Polynomial: [0.14574 s] survived
   - [#  76] ROR Polynomial: [0.14290 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  77] ROR Polynomial: [0.14451 s] survived
   - [#  78] ROR Polynomial: [0.14080 s] killed by PolyTest.py::test_first_degree_polynomial
   - [#  79] ROR Polynomial: [0.14106 s] survived
   - [#  80] SIR Polynomial: [0.17988 s] killed by PolyTest.py::test_mutated_wrapper_add_aor
```
```bash
Mutation score [11.28410 s]: 79.3%
   - all: 80
   - killed: 46 (57.5%)
   - survived: 12 (15.0%)
   - incompetent: 22 (27.5%)
   - timeout: 0 (0.0%)
```

# 

## Analysis of Test Suite's Effectiveness
While the test suite killed a significant number of mutants, some survived or were deemed incompetent. This indicates potential weaknesses in test coverage or mutation operator robustness.

# 

## Recommendations for Test Suite Improvement
1. Enhance test coverage for specific edge cases or exceptional scenarios.
2. Refine mutation operators to ensure more rigorous changes.
3. Include tests specifically targeting mutated behaviors identified in survived mutants.
4. Increase the variety and complexity of test scenarios.

# 

## Conclusion
The mutation testing conducted on the Polynomial class and its associated test suite revealed valuable insights into the effectiveness of the testing approach. While the test suite demonstrated its capability to detect and eliminate a substantial portion of the generated mutants, the survival of certain mutants and the identification of incompetent ones suggest potential areas for enhancing test coverage. The results emphasize the importance of refining the test suite by addressing the identified gaps, augmenting test scenarios, and improving mutation operators. This iterative process is pivotal in fortifying code quality, ensuring the reliability of polynomial-related operations, and enhancing the overall robustness of the Polynomial class implementation.


---

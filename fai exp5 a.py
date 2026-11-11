from itertools import product


def evaluate_statement(p, q, r):
    """
    Evaluates the propositional logic statement:
    (p OR q) AND (NOT r)
    """
    return (p or q) and (not r)


def generate_truth_table():
    print("Truth Table for Propositional Logic Statement: (p ∨ q) ∧ ¬r")
    print("-" * 60)
    print(f"{'p':<10}{'q':<10}{'r':<10}{'Result':<10}")
    print("-" * 60)

    # Generate all possible True/False combinations
    # for 3 variables (2^3 = 8 rows)
    for p, q, r in product([True, False], repeat=3):
        result = evaluate_statement(p, q, r)
        print(f"{str(p):<10}{str(q):<10}{str(r):<10}{str(result):<10}")


# Run the truth table generator
generate_truth_table()

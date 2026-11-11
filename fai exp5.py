class CSPMapColoring:
    def __init__(self, variables, domains, neighbors):
        self.variables = variables
        self.domains = domains  # Dictionary tracking possible colors for each region
        self.neighbors = neighbors  # Dictionary tracking adjacent regions

    def revise(self, xi, xj):
        """
        Removes values from domains[xi] if they conflict with
        all values in domains[xj].
        """
        revised = False

        # Create a copy of the list so we can safely modify
        # the original domain during iteration
        for x in list(self.domains[xi]):

            # If there is NO value y in xj's domain that satisfies x != y,
            # remove x
            if not any(x != y for y in self.domains[xj]):
                self.domains[xi].remove(x)
                revised = True

        return revised

    def ac3(self):
        """
        AC-3 Algorithm implementation.
        """

        # Step 1: Initialize queue with all directed arcs
        # (pairs of neighbors)
        queue = [
            (xi, xj)
            for xi in self.variables
            for xj in self.neighbors[xi]
        ]

        while queue:
            xi, xj = queue.pop(0)

            # Step 2: If the domain of xi was trimmed,
            # we need to check consistency
            if self.revise(xi, xj):

                # If a domain becomes completely empty,
                # no solution exists
                if not self.domains[xi]:
                    return False

                # Step 3: Add affected neighbors back to the queue
                # for re-evaluation
                for xk in self.neighbors[xi]:
                    if xk != xj:
                        queue.append((xk, xi))

        return True


# --- Example Setup ---

# Imagine 3 regions (A, B, C) where every region borders
# the other two.
variables = ['A', 'B', 'C']

domains = {
    'A': ['Red', 'Green'],
    'B': ['Red', 'Green'],
    'C': ['Red', 'Green']
}

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

csp = CSPMapColoring(variables, domains, neighbors)

if csp.ac3():
    print("AC-3 successfully pruned the domains:")

    for region, color_options in csp.domains.items():
        print(f"Region {region}: {color_options}")
else:
    print("No solution possible for this configuration.")

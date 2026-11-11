class node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children or []

    def is_terminal(self):
        return len(self.children) == 0

    def get_value(self):
        return self.value

    def get_children(self):
        return self.children


def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.get_value()

    if maximizing_player:
        max_eval = float('-inf')

        for child in node.get_children():
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)

            if beta <= alpha:
                break

        return max_eval

    else:
        min_eval = float('inf')

        for child in node.get_children():
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)

            if alpha >= beta:
                break

        return min_eval


leaf1 = node(value=9)
leaf2 = node(value=8)
leaf3 = node(value=7)
leaf4 = node(value=6)

child1 = node(children=[leaf1, leaf2])
child2 = node(children=[leaf3, leaf4])

root = node(children=[child1, child2])

optimal_value = alpha_beta(
    root,
    depth=2,
    alpha=float('-inf'),
    beta=float('inf'),
    maximizing_player=True
)

print(f"The optimal value is: {optimal_value}")

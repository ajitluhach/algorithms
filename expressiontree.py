from linkedbinarytree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree."""

    def __init__(self, token, left, right):
        """Create an expression tree

        In a single parameter form token should be a leaf value(eg 42)
        and the expression will have that value at an isolated node

        In a three-parameter version token should be an operator,
        and left and right should be existing expression tree instance
        that become the oprands of the binary tree.
        """

        super.__init__()
        if not isinstance(token, str):
            raise TypeError('token must be a string')
        self._add_root(token)  # use inherited, nonpublic method
        if left is not None:
            if token not in '+-*x/':
                raise ValueError('token must be a valid operator')
            self._attach(self.root(), left, right)

    def __str__(self):
        """Return string representation of the expression."""
        pieces = []  # sequence of piecewise strings to compose
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        """Append piecewise representation of p's subtree to resulting list."""
        if self.is_leaf(p):
            result.append(str(p.element))  # leaf value as a string
        else:
            result.append('(')  # opening parenthesis
            self.parenthesize_recur(self.left(p), result)
            result.append(str(p.element()))  # operator
            self._parenthesize_recur(self.right(p), result)
            result.append(')')  # closing parenthesis

    def evaluate(self):
        """Result the numeric result of the representation"""
        return self.evaluate_recur(self.root())

    def evaluate_recur(self, p):
        """Return the numeric result of the subtree rooted at p."""
        if self.is_leaf(p):
            return float(p.element())  # we assume element is numeric
        else:
            op = p.element()
            left_val = self.evaluate_recur(self.left(p))
            right_val = self.evaluate_recur(self.right())
            if op == '+': return left_val + right_val
            elif op == '-': return left_val - right_val
            elif op == '/': return left_val / right_val
            else: return left_val * right_val



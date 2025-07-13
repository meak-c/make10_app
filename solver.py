import itertools
import math
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
op_symbols = list(ops.keys())


class ExprNode:
    def __init__(self, val, left=None, right=None, op=None):
        self.val = val
        self.left = left
        self.right = right
        self.op = op

    def eval(self):
        if self.op is None:
            return self.val
        try:
            return ops[self.op](self.left.eval(), self.right.eval())
        except ZeroDivisionError:
            return None

    def to_str(self):
        if self.op is None:
            return str(self.val)
        left = self.left.to_str()
        right = self.right.to_str()
        return f'({left} {self.op} {right})'

    def canonical(self):
        if self.op is None:
            return ('num', self.val)
        left_c = self.left.canonical()
        right_c = self.right.canonical()
        if self.op in ['+', '*']:
            ordered = tuple(sorted([left_c, right_c]))
            return (self.op, ordered)
        else:
            return (self.op, left_c, right_c)


def generate_all_expressions(nums):
    if len(nums) == 1:
        yield ExprNode(nums[0])
        return
    for i in range(1, len(nums)):
        left_parts = nums[:i]
        right_parts = nums[i:]
        for l in generate_all_expressions(left_parts):
            for r in generate_all_expressions(right_parts):
                for op in op_symbols:
                    if op == '/' and r.eval() == 0:
                        continue
                    yield ExprNode(None, l, r, op)


def solve(goal, numbers, max_results=10):
    solutions = []
    canonical_set = set()
    for perm in itertools.permutations(numbers):
        for expr in generate_all_expressions(list(perm)):
            val = expr.eval()
            if val is not None and math.isclose(val, goal, rel_tol=1e-9):
                canon = expr.canonical()
                if canon not in canonical_set:
                    canonical_set.add(canon)
                    expr_str = expr.to_str()
                    if expr_str.startswith('(') and expr_str.endswith(')'):
                        expr_str = expr_str[1:-1]
                    expr_str = expr_str.replace('*', '×').replace('/', '÷')
                    goal_str = str(int(goal)) if math.isclose(
                        goal, int(goal)) else str(goal)
                    solutions.append(f"{expr_str} = {goal_str}")
                    if len(solutions) >= max_results:
                        return solutions
    return solutions

from sympy import symbols, Eq, solve
import re

def solve_math(query: str) -> str:
    try:
        expr = query.lower().replace("^", "**")
        match = re.match(r"solve (.*)", expr)
        if match:
            expr = match.group(1)
        x = symbols("x")
        if "=" in expr:
            left, right = expr.split("=")
            eq = Eq(eval(left.strip()), eval(right.strip()))
            sol = solve(eq, x)
        else:
            sol = eval(expr)
        return f"Solution: {sol}"
    except Exception as e:
        return f"Math error: {str(e)}"

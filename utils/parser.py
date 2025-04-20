import sympy as sp

def parse_function(expr_str):
    x = sp.symbols('x')
    expr = sp.sympify(expr_str)
    f_lambda = sp.lambdify(x, expr, "numpy")
    df_expr = sp.diff(expr, x)
    df_lambda = sp.lambdify(x, df_expr, "numpy")
    return f_lambda, df_lambda

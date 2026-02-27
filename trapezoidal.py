import sympy as sp

def trapezoidal_rule(f_str, a, b, n):
    x = sp.symbols('x')
    f = sp.sympify(f_str)
    h = (b - a) / n
    
    result = 0.5 * (f.subs(x, a) + f.subs(x, b))
    
    for i in range(1, n):
        result += f.subs(x, a + i*h)
    
    return float(result * h)

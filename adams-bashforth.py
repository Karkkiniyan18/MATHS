import sympy as sp

def adams_bashforth(f_str, x0, y0, h, steps):
    x = sp.symbols('x')
    y = sp.symbols('y')
    f = sp.sympify(f_str)

    def f_eval(x_val, y_val):
        return float(f.subs({x: x_val, y: y_val}))

    results = [(x0, y0)]

    x_prev = x0
    y_prev = y0
    f_prev = f_eval(x_prev, y_prev)

    for _ in range(steps):
        x_pred = x_prev + h
        y_pred = y_prev + h * f_prev

        f_pred = f_eval(x_pred, y_pred)

        y_corr = y_prev + (h/2) * (f_prev + f_pred)

        results.append((x_pred, y_corr))

        x_prev, y_prev, f_prev = x_pred, y_corr, f_eval(x_pred, y_corr)

    return results

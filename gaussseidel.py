import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter=1000):
    A = np.array(A, float)
    b = np.array(b, float)
    x = np.array(x0, float)
    n = len(b)
    it = 0

    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x_old[j] for j in range(i+1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]

        it += 1
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return {"solution": x.tolist(), "iterations": it}

    return {"error": "Did not converge", "iterations": it}

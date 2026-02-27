from fastapi import FastAPI
from methods.gauss_seidel import gauss_seidel
from methods.trapezoidal import trapezoidal_rule
from methods.adams_bashforth import adams_bashforth
from pydantic import BaseModel

app = FastAPI()

# ----------------- Gauss Seidel ------------------
class GSInput(BaseModel):
    A: list
    b: list
    x0: list
    tol: float

@app.post("/gauss-seidel")
def gs_api(data: GSInput):
    return gauss_seidel(data.A, data.b, data.x0, data.tol)

# ----------------- Trapezoidal Rule --------------
class TrapInput(BaseModel):
    f: str
    a: float
    b: float
    n: int

@app.post("/trapezoidal")
def trap_api(data: TrapInput):
    result = trapezoidal_rule(data.f, data.a, data.b, data.n)
    return {"result": result}

# ----------- Adams-Bashforth Predictor Corrector -----------------
class ABInput(BaseModel):
    f: str
    x0: float
    y0: float
    h: float
    steps: int

@app.post("/adams-bashforth")
def ab_api(data: ABInput):
    return {"result": adams_bashforth(data.f, data.x0, data.y0, data.h, data.steps)}

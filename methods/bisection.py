def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >=0:
        raise ValueError("La funcion debe tener signos opuestos en a y b.")
    
    errors = []
    for i in range(max_iter):
        c = (a + b) / 2.0
        error = abs( b -a) / 2.0
        errors.append(error)

        if abs(f(c)) < tol or error < tol:
            return {"root": c, "iterations": i + 1, "errors": errors}
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return {"root": c, "iterations": max_iter, "errors": errors}
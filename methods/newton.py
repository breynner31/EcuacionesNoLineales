def newton_raphson_method(f, df, x0, tol=1e-6, max_iter=100):
    errors = []
    x = x0

    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ZeroDivisionError("La derivada se hizo cero. No se puede continuar.")

        x_new = x - fx / dfx
        error = abs(x_new - x)
        errors.append(error)

        if error < tol:
            return {"root": x_new, "iterations": i + 1, "errors": errors}

        x = x_new

    return {"root": x, "iterations": max_iter, "errors": errors}

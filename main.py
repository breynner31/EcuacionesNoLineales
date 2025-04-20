from methods.bisection import bisection_method
from methods.newton import newton_raphson_method
from utils.parser import parse_function
from utils.metrics import measure_performance
from utils.plot import plot_comparison
from colorama import init, Fore, Style

init(autoreset=True)

def main():
    print(Fore.CYAN + "=== RESOLVER ECUACIONES NO LINEALES ===")
    equation_str = input(Fore.YELLOW + "Ingrese la ecuación f(x): ")

    try:
        func, deriv = parse_function(equation_str)
    except Exception as e:
        print(Fore.RED + f"Error al interpretar la función: {e}")
        return

    try:
        a = float(input("Ingrese el valor inicial a (para Bisección): "))
        b = float(input("Ingrese el valor final b (para Bisección): "))
        x0 = float(input("Ingrese el valor inicial x0 (para Newton-Raphson): "))
        tol = float(input("Ingrese la tolerancia (ej: 1e-6): "))
        max_iter = int(input("Ingrese el número máximo de iteraciones: "))
    except Exception:
        print(Fore.RED + "Entrada inválida. Por favor ingrese valores numéricos.")
        return

    print(Fore.MAGENTA + "\n--- MÉTODO DE BISECCIÓN ---")
    if func(a) * func(b) >= 0:
        print(Fore.RED + "\n[ERROR] El intervalo [a, b] no cumple la condición f(a) * f(b) < 0")
        print(Fore.YELLOW + "Por favor ingrese valores de a y b donde la función cambie de signo.\n")
        return

    bisect_result = measure_performance(bisection_method, func, a, b, tol, max_iter)


    print(Fore.BLUE + "\n--- MÉTODO DE NEWTON-RAPHSON ---")
    newton_result = measure_performance(newton_raphson_method, func, deriv, x0, tol, max_iter)

    print(Fore.GREEN + "\n--- COMPARACIÓN ---")
    print(f"Iteraciones: Bisección = {bisect_result['iterations']} | Newton-Raphson = {newton_result['iterations']}")
    print(f"Tiempo (s): Bisección = {bisect_result['time']:.6f} | Newton-Raphson = {newton_result['time']:.6f}")
    print(f"Memoria (KB): Bisección = {bisect_result['memory']} | Newton-Raphson = {newton_result['memory']}")

    plot_comparison(bisect_result, newton_result)

if __name__ == "__main__":
    main()

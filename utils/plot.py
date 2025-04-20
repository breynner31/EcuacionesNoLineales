import matplotlib.pyplot as plt

def plot_comparison(bisect, newton):
    plt.figure(figsize=(10, 5))

    plt.plot(bisect["errors"], label="Bisección", marker='o')
    plt.plot(newton["errors"], label="Newton-Raphson", marker='x')
    plt.yscale("log")
    plt.xlabel("Iteración")
    plt.ylabel("Error (log)")
    plt.title("Comparación de errores por iteración")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

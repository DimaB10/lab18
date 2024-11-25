import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-0.5, 12, 500)
y = 2 * np.sqrt(x) + 3 * np.sqrt(x + 1.1)
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='blue', linestyle='-', label=r'$y = 2\sqrt{x} + 3\sqrt{x+1.1}$')
plt.title("Графік функції")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.savefig("grafik.png")
plt.show()

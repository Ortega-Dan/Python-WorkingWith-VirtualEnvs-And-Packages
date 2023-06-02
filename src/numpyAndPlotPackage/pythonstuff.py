# pyright: basic
import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)

# use dark theme plot
plt.style.use("dark_background")


def plotthing():
    x = [x for x in range(len(ys))]

    plt.plot(x, ys, "-")
    plt.fill_between(x, ys, 195, where=(ys > 195), facecolor="g", alpha=0.6)  # type: ignore

    plt.title("Sample Visualization")
    plt.show()

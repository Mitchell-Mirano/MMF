import numpy as np
from typing import List
import matplotlib.pyplot as plt
from potencial.potential_in_xy import potencial_charges_xy


def lineas_equipotenciales():
    cargas: list = []
    posicion_cargas: list = []
    n_charges: int = int(input("Ingrese el numero de cargas que utilizara: "))
    for i in range(1, n_charges + 1):
        q: float = eval(input(f"El valor de la carga {i}: "))
        cargas.append(q)
        p: str = input(f"Ingresar la posicion (x,y) de la carga {i}: ")
        p: list = p.replace("(", "").replace(")", "").split(",")
        posicion_cargas.append((eval(p[0]), eval(p[1])))

    while True:
        v_values: str = input("Ingrese el valor de los potenciales: ")
        if v_values == "q":
            break
        v_values: List[str] = v_values.replace("[", "").replace("]", "").split(",")
        v_values_float: list = [eval(value) for value in v_values]

        x = np.linspace(-5, 5, 100)
        y = x.copy()
        X, Y = np.meshgrid(x, y)

        Z = potencial_charges_xy(cargas, posicion_cargas, X, Y)
        plt.figure(figsize=(12, 10))
        cs = plt.contour(X, Y, Z, levels=v_values_float)

        fmt = {}
        strs = [f"${value}V$" for value in v_values]
        for l, s in zip(cs.levels, strs):
            fmt[l] = s
        plt.clabel(cs, cs.levels, inline=True, fmt=fmt, fontsize=15)
        plt.title("Lineas Equipotenciales", fontsize=20)
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.axhline(y=0)
        plt.axvline(x=0)
        plt.show()

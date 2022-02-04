import numpy as np
from typing import List


def potencial_charges_xy(charges: list, position_charges: list, x, y):
    k = 9 * 10 ** 9
    potencialxy = 0
    for charge, position in zip(charges, position_charges):
        potencialxy = potencialxy + k * charge / np.sqrt((x - position[0]) ** 2 + (y - position[1]) ** 2)

    return potencialxy


def potencial_xy(carga: float, posicion_carga: tuple, xy: tuple):
    k = 1 / (4 * np.pi * (8.85 * 10 ** -12))
    r = np.linalg.norm([xy[0] - posicion_carga[0], xy[1] - posicion_carga[1]])
    return k * carga / r


def potencial_en_xy():
    cargas: list = []
    posicion_cargas: list = []

    for i in range(1, 3):
        q: float = eval(input(f"El valor de la carga {i}: "))
        cargas.append(q)
        p: str = input(f"Ingresar la posicion (x,y) de la carga {i}: ")
        p: list = p.replace("(", "").replace(")", "").split(",")
        posicion_cargas.append((float(p[0]), float(p[1])))

    while True:
        u_xy: str = input("Ingresar una posicion (x,y) donde calcular el potencial: ")
        if u_xy == "q":
            break
        u_xy: List[str] = u_xy.replace("(", "").replace(")", "").split(",")
        u_x: float = eval(u_xy[0])
        u_y: float = eval(u_xy[1])
        xy = (u_x, u_y)
        potencial: float = 0
        for charge, position_charge in zip(cargas, posicion_cargas):
            potencial = potencial + potencial_xy(charge, position_charge, xy)

        print(f"El potencial en ({u_x},{u_y}) es: {potencial}")

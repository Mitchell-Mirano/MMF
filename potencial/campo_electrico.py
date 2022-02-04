import numpy as np
import matplotlib.pyplot as plt
from potencial.potential_in_xy import potencial_charges_xy


def campo_in_xy(cargas, position_charges, x, y):
    k = 9 * 10 ** 9
    campo_in_x = 0
    campo_in_y = 0
    for charge, position in zip(cargas, position_charges):
        r = np.linalg.norm([x - position[0], y - position[1]])
        campo_in_x = campo_in_x + k * charge * (x - position[0]) / (r ** 3)
        campo_in_y = campo_in_y + k * charge * (y - position[1]) / (r ** 3)
    E = np.linalg.norm([campo_in_x, campo_in_y])

    return E


def campo_electrico_from_equipotential_lines():
    cargas = [-1.2 * 10 ** -9, 2.5 * 10 ** -9]
    posiciones = [(0, 0), (0, 0.5)]
    x = np.linspace(0, 5, int(5 / 0.005))
    y = np.linspace(-1, 1, int(2 / 0.25))

    V: float = eval(input("Ingrese V: "))
    dv: float = eval(input("Ingrese dv: "))
    posible_xy_dict = {}

    for y_val in y:
        posible_xy = []
        for x_val in x:
            z = potencial_charges_xy(cargas, posiciones, x_val, y_val)
            if V - dv / 2 - 0.01 < z < V - dv / 2 + 0.01:
                posible_xy.append((x_val, y_val))

            if V + dv / 2 - 0.01 < z < V + dv / 2 + 0.01:
                posible_xy.append((x_val, y_val))
        posible_xy_dict[str(y_val)] = posible_xy

    potencial_campos = []
    for key, values in posible_xy_dict.items():
        if len(values) == 2:
            x_values = [val[0] for val in values]
            y_values = [val[1] for val in values]
            ds = np.linalg.norm([x_values[0] - x_values[1], y_values[0] - y_values[1]])
            dv1 = potencial_charges_xy(cargas, posiciones, x_values[0], y_values[0])
            dv2 = potencial_charges_xy(cargas, posiciones, x_values[1], y_values[1])
            potencial_campos.append(np.abs((dv1 - dv2) / ds))

    campos = []
    for key, values in posible_xy_dict.items():
        if len(values) == 2:
            x_values = [val[0] for val in values]
            y_values = [val[1] for val in values]
            E = campo_in_xy(cargas, posiciones, np.mean(x_values), np.mean(y_values))
            campos.append(E)

    print(f"Campos calulados como dv/ds: ", potencial_campos)
    print(f"Campos calculados como kq/r^2: ", campos)

    X, Y = np.meshgrid(x, y)
    Z = potencial_charges_xy(charges=cargas,
                             position_charges=posiciones,
                             x=X,
                             y=Y)

    plt.figure(figsize=(12, 12))
    plt.contour(X, Y, Z, levels=[V - dv / 2, V, V + dv / 2])
    for key, values in posible_xy_dict.items():
        if len(values) == 2:
            x_values = [val[0] for val in values]
            y_values = [val[1] for val in values]
            plt.plot(x_values, y_values, lw=3)
    plt.axhline(y=0)
    plt.axvline(x=0)
    plt.show()

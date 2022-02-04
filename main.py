import os
from potencial.potential_in_xy import potencial_en_xy
from potencial.equipotential_lines import lineas_equipotenciales
from potencial.campo_electrico import campo_electrico_from_equipotential_lines
from potencial.rutherford_experiment import Rutherford_Experiment

functions = {
    "1": potencial_en_xy,
    "2": lineas_equipotenciales,
    "3": campo_electrico_from_equipotential_lines,
    "4": Rutherford_Experiment
}


def display_options():
    with open("data/options.txt", mode="r", encoding="utf-8") as options:
        options = options.read()

    while True:
        print(options)
        option = input("Opcion: ")
        if option == "q":
            break
        current_function = functions[option]
        current_function()
        os.system("clear")


if __name__ == "__main__":
    display_options()

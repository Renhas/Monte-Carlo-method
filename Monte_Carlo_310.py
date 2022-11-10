from random import randint

# Преобразование строки в число
# Если преобразование невозможно, возвращает 0
def strToInt(str):
    try:
        int(str)
    except ValueError:
        return 0
    return int(str)

# Преобразование целого числа в его двоичную форму
def intToBinary(number, lenght = 2):
    return f"{f'{number:0b}'.zfill(lenght)}"


# Алгоритм Монте-Карло
def Monte_Carlo(steps, lenght, values):
    max, maxS = 0, "Пустая кодировка"

    print("\nНачинаем работу...\n")
    for x in range(steps):
        s = randint(0, 2 ** (lenght - 1))

        print(f"Шаг {x+1}\nТекущая лучшая кодировка: {maxS} с приспособленностью {max:,}")
        print(f"Выбранная кодировка на этом шаге: {intToBinary(s, lenght)} с приспособленностью {values[s]:,}")

        if values[s] > max:
            max = values[s]
            maxS = intToBinary(s, lenght)
            print(f"Выбрана новая лучшая кодировка {maxS} с приспособленностью {max:,}")
        print()

    print(f"Алгоритм завершил работу. Искомое решение: {maxS}, его приспособленность {max:,}")


def main():
    L = strToInt(input("Введите длину кодировки L: "))
    if L < 0:
        print("Некорректное значение, будет установлено значение по умолчанию L = 15")
        L = 15

    N = strToInt(input("Введите количество шагов N: "))
    if N < 2:
        print("Некорректное значение, будет установлено значение по умолчанию N = 10")
        N = 10

    # Вычисление приспособленностей в виде квадратичных функций
    U = []
    for x in range(2 ** L):
        U.append((x - 2 ** (L-1)) ** 2)

    # Вывод списка кодировок и их приспособленностей
    count = 5
    if count > L:
        count = L
    print("\nСписок кодировок и приспособленностей (первые 32):")
    for element in range(2 ** count):
        print(f"Кодировка {intToBinary(element, L)} | Приспособленность {U[element]:,}")

    # Запуск алгоритма
    Monte_Carlo(steps=N, lenght=L, values=U)


main()
input()


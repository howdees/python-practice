from calculator import add, sub, mul, div


def run_calculator():
    """Запускает калькулятор в интерактивном режиме."""

    print("________ КАЛЬКУЛЯТОР ________")
    print("Доступные операции: +, -, *, /")
    print("Для выхода введите exit")

    while True:
        first_input = input("\nПервое число: ").strip()

        if first_input.lower() == "exit":
            print("Работа калькулятора завершена.")
            break

        try:
            a = float(first_input)
            operation = input("Операция: ").strip()

            if operation == "exit":
                print("Работа калькулятора завершена.")
                break

            if operation not in ["+", "-", "*", "/"]:
                print("Ошибка: неизвестная операция.")
                continue

            second_input = input("Второе число: ").strip()

            if second_input.lower() == "exit":
                print("Работа калькулятора завершена.")
                break

            b = float(second_input)

            if operation == "+":
                result = add(a, b)

            elif operation == "-":
                result = sub(a, b)

            elif operation == "*":
                result = mul(a, b)

            else:
                result = div(a, b)

            print(f"Результат: {result:g}")

        except ValueError:
            print("Ошибка: необходимо ввести число.")

        except ZeroDivisionError as error:
            print(f"Ошибка: {error}")


def is_prime(n):
    """Проверяет, является ли число простым."""

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def print_primes():
    """Выводит все простые числа от 1 до 200."""

    primes = []

    for number in range(1, 201):
        if is_prime(number):
            primes.append(number)

    print("Простые числа от 1 до 200:")
    print(*primes, sep=", ")

def validate_age(value):
    """Проверяет корректность возраста от 0 до 120."""

    try:
        age = int(value)

    except (ValueError, TypeError):
        return False

    return 0 <= age <= 120


def main():
    """Главная функция программы."""

    while True:
        print("\n========== МЕНЮ ==========")
        print("1. Калькулятор")
        print("2. Простые числа от 1 до 200")
        print("3. Проверка возраста")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            run_calculator()

        elif choice == "2":
            print_primes()

        elif choice == "3":
            age = input("Введите возраст: ")

            if validate_age(age):
                print("Возраст введён корректно.")
            else:
                print("Ошибка: возраст должен быть целым числом от 0 до 120.")

        elif choice == "0":
            print("Программа завершена.")
            break

        else:
            print("Ошибка: выберите существующий пункт меню.")


if __name__ == "__main__":
    main()

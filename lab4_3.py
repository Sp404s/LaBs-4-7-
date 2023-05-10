def div_by_3(number: int):
    return True if number % 3 == 0 else False


def div_100_by(number):
    res = None
    try:
        res = 100 / float(number)
    except ValueError:
        print("В эту функцию нужно передать число")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    except Exception as e:
        print("Ошибка: ", e)
    return res


def magic_date_check(date: str):
    try:
        date = date.split(".")
        if int(date[0]) * int(date[1]) == int(date[2][2:]):
            return True
        else:
            return False
    except:
        print("Функция принимает строку с датой в формате dd.mm.yyyy")


def lucky_ticket(ticket: str):
    sum1 = sum([int(i) for i in ticket[:int(len(ticket) / 2)]])
    sum2 = sum([int(i) for i in ticket[int(len(ticket) / 2):]])
    if sum1 == sum2:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Проверка функции деления на три")
    print(div_by_3(56))
    print(div_by_3(27))

    print("\nПроверка функции деления 100 на число")
    print(div_100_by(10))
    print(div_100_by(0))
    print(div_100_by("s"))

    print("\nПроверка функции магической даты")
    print(magic_date_check("22.01.2022"))
    print(magic_date_check("21.01.2022"))

    print("\nПроверка функции счастливого билета")
    print(lucky_ticket("385916"))
    print(lucky_ticket("231002"))

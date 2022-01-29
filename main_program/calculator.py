def calculator(expression):
    print("Проверка")
    allowed = "+-/*"
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Выражение должно содержать хотя бы один знак ({allowed})')
    for sign in allowed:
        if sign in expression:
            try:
                left, rigth = expression.split(sign)
                left, rigth = int(left), int(rigth)
                if sign == "+":
                    return left + rigth
                elif sign == "-":
                    return left - rigth
                elif sign == "*":
                    return left * rigth
                elif sign == "/":
                    return left / rigth
            except (ValueError, TypeError):
                raise ValueError(f'Выражение должно содержать 2 целых числа и 1 знак')


if __name__ == '__main__':
    print(calculator("3/2"))

from decimal import *


def usual(data, mark):
    try:
        getcontext().prec = 10
        if mark == "+":
            c = Decimal(str(data["a"])) + Decimal(str(data["b"]))
        elif mark == "-":
            c = Decimal(str(data["a"])) - Decimal(str(data["b"]))
        elif mark == "*":
            c = Decimal(str(data["a"])) * Decimal(str(data["b"]))
        elif mark == "/":
            c = Decimal(str(data["a"])) / Decimal(str(data["b"]))

        else:
            c = None
        assert c == Decimal(str(data["expect"]))
        print(f"驗證{data['a']}{mark}{data['b']}運算結果：pass")
    except Exception as e:
        print(f"驗證{data['a']}{mark}{data['b']}運算結果：false", e)
        raise e

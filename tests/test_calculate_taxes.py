from main import calculate_taxes, calculate_tax
import pytest


@pytest.mark.parametrize(
    "list_of_goods, tax_rate, expected", [([10, 20, 40, 60], 10, [11, 22, 44, 66]), ([50, 100], 40, [70, 140])]
)
def test_calculate_taxes(list_of_goods, tax_rate, expected):
    assert calculate_taxes(list_of_goods, tax_rate) == expected


def test_calculate_taxes_tax_rate_zero(numbers_list):
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes(numbers_list, -1)

    assert str(exc_info.value) == "Неверный налоговый процент"


def test_calculate_taxes_price_zero():
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([0], 2)

    assert str(exc_info.value) == "Неверная цена"


# Тестирование функции calculate_tax(price: float, tax_rate: float) -> float


@pytest.mark.parametrize("price, tax_rate, expected", [(10, 10, 11), (50, 40, 70), (1, 50, 1.5)])
def test_calculate_tax_normal_values(price, tax_rate, expected):
    assert calculate_tax(price, tax_rate) == expected


@pytest.mark.parametrize(
    "price, tax_rate, expected",
    [
        (0, 10, "Неверная цена"),
        (-1, 40, "Неверная цена"),
        (-5000000000000, 50, "Неверная цена"),
        (1, 100, "Неверный налоговый процент"),
        (7, -0.1, "Неверный налоговый процент"),
        (1, 1200, "Неверный налоговый процент"),
    ],
)
def test_calculate_tax_wrong_parameters(price, tax_rate, expected):
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(price, tax_rate)

    assert str(exc_info.value) == expected


@pytest.mark.parametrize("price, tax_rate, discount, expected", [(10, 10, 50, 5.5), (50, 40, 0, 70), (1, 50, 100, 0)])
def test_calculate_tax_with_discount(price, tax_rate, discount, expected):
    assert calculate_tax(price, tax_rate, discount=discount) == expected


@pytest.mark.parametrize(
    "price, tax_rate, is_rounded, expected", [(10, 2.2, True, 10.22), (50, 2.11, False, 51.055), (1, 5.111, True, 1.05)]
)
def test_calculate_tax_with_discount(price, tax_rate, is_rounded, expected):
    assert calculate_tax(price, tax_rate, is_round=is_rounded) == expected


@pytest.mark.parametrize(
    "price, tax_rate, expected",
    [
        (10, "Дофига", "Используйте числа!"),
        ("Дофига", 40, "Используйте числа!"),
        ("Дофига", "Дофига", "Используйте числа!"),
        (True, 10, "Используйте числа!"),
    ],
)
def test_calculate_tax_not_int_or_float(price, tax_rate, expected):
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(price, tax_rate)

    assert str(exc_info.value) == expected

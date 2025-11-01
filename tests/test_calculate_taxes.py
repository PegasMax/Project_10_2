from main import calculate_taxes
import pytest

@pytest.mark.parametrize("list_of_goods, tax_rate, expected", [
    ([10,20,40,60], 10, [11, 22, 44, 66]),
    ([50,100], 40, [70, 140])
])
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


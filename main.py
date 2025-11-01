def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError("Неверный налоговый процент")

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError("Неверная цена")
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices


def calculate_tax(price, tax_rate, *, discount: float = 0, is_round: bool = False) -> float:
    """Получает цену товара и налоговую ставку, а возвращает стоимость товара с учетом налога."""

    if not ((type(price) in (int, float)) and (type(tax_rate) in (int, float))):
        raise ValueError("Используйте числа!")

    if (tax_rate < 0) or (tax_rate >= 100):
        raise ValueError("Неверный налоговый процент")

    if price <= 0:
        raise ValueError("Неверная цена")

    if is_round:
        last_price = round((price + price * tax_rate / 100) * (100 - discount) / 100, 2)
    else:
        last_price = (price + price * tax_rate / 100) * (100 - discount) / 100

    return last_price

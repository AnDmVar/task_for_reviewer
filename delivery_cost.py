def calculate_delivery_cost(
    distance: float, size: str, fragile: bool, load: str
) -> float or str:
    if distance < 0:
        raise ValueError("Некорректное расстояние")
    if size not in ["big", "small"]:
        raise ValueError("Некорректный размер груза")
    if load not in ["very high", "high", "medium", "low"]:
        raise ValueError("Некорректная загруженность службы")

    delivery_cost = 0

    if distance > 30:
        if fragile:
            return "Хрупкие грузы нельзя возить на расстояние более 30 км."
        delivery_cost += 300
    elif distance > 10:
        delivery_cost += 200
    elif distance > 2:
        delivery_cost += 100
    else:
        delivery_cost += 50

    if size == "big":
        delivery_cost += 200
    elif size == "small":
        delivery_cost += 100

    if fragile:
        delivery_cost += 300

    if load == "very high":
        delivery_cost *= 1.6
    elif load == "high":
        delivery_cost *= 1.4
    elif load == "medium":
        delivery_cost *= 1.2

    if delivery_cost < 400:
        delivery_cost = 400

    return delivery_cost

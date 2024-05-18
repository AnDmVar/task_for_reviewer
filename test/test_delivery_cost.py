import pytest
from delivery_cost import calculate_delivery_cost


@pytest.mark.positive
@pytest.mark.parametrize(
    ("distance", "size", "fragile", "load", "expected"),
    [
        (35, "big", False, "high", 700.0),
        (5, "small", True, "very high", 800.0),
        (1, "small", False, "low", 400.0),
        (25, "big", False, "medium", 480.0),
        (2, "big", True, "high", 770.0),
        (0.5, "small", False, "low", 400.0),
        (20, "big", True, "very high", 1120.0),
        (1.5, "big", True, "low", 550.0),
        (30, "big", False, "medium", 480.0),
        (10, "small", False, "low", 400.0),
        (30, "small", True, "high", 840.0),
        (
            35,
            "big",
            True,
            "high",
            "Хрупкие грузы нельзя возить на расстояние более 30 км.",
        ),
    ],
)
def test_calculate_delivery_cost_positive(distance, size, fragile, load, expected):
    assert calculate_delivery_cost(distance, size, fragile, load) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    ("distance", "size", "fragile", "load", "expected"),
    [
        (-1, "big", False, "low", "Некорректное расстояние"),
        (10, "medium", False, "low", "Некорректный размер груза"),
        (10, "small", False, "extreme", "Некорректная загруженность службы"),
        (
            35,
            "big",
            True,
            "high",
            "Хрупкие грузы нельзя возить на расстояние более 30 км.",
        ),
    ],
)
def test_calculate_delivery_cost_negative(distance, size, fragile, load, expected):
    with pytest.raises(ValueError, match=expected):
        calculate_delivery_cost(distance, size, fragile, load)

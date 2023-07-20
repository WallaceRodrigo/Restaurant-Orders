from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    dish_meat = Dish("carne", 10.0)
    meat = Ingredient("carne")
    # invalid_ingredient = Ingredient("xablau")

    assert dish_meat.name == "carne"
    assert dish_meat.price == 10.0
    assert repr(dish_meat) == "Dish('carne', R$10.00)"
    assert hash(dish_meat) == hash("Dish('carne', R$10.00)")
    assert dish_meat == dish_meat

    dish_meat.add_ingredient_dependency(meat, 1)
    assert dish_meat.recipe == {meat: 1}

    assert dish_meat.get_ingredients() == {meat}
    assert dish_meat.get_restrictions() == meat.restrictions

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("salmão", "xablau")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("salmão", 0)

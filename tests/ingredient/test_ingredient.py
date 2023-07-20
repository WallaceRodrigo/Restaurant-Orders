from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    meat = Ingredient("carne")
    invalid_ingredient = Ingredient("xablau")
    salmon = Ingredient("salmão")

    assert meat.name == "carne"
    assert repr(meat) == "Ingredient('carne')"
    assert hash(meat) == hash("carne")
    assert invalid_ingredient.restrictions == set()
    assert meat != salmon
    assert meat == meat

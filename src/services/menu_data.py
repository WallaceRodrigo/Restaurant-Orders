# Req 3
import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path):
        self.source_path = source_path
        self.dishes = set()
        self._read_csv()

    def _read_csv(self):
        with open(self.source_path, newline="") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                (
                    dish_name,
                    dish_price,
                    ingredient_name,
                    ingredient_quantity,
                ) = row
                self._add_dish(
                    dish_name,
                    float(dish_price),
                    ingredient_name,
                    int(ingredient_quantity),
                )

    def _add_dish(
        self, dish_name, dish_price, ingredient_name, ingredient_quantity
    ):
        dish = self._get_dish_by_name(dish_name)
        if not dish:
            dish = Dish(dish_name, dish_price)
            self.dishes.add(dish)

        ingredient = Ingredient(ingredient_name)
        dish.add_ingredient_dependency(ingredient, ingredient_quantity)

    def _get_dish_by_name(self, dish_name):
        for dish in self.dishes:
            if dish.name == dish_name:
                return dish
        return None

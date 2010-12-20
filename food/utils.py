from models import Ingredient
import re
from food.models import IngredientAmount

def add_many_ingredients_to_section(section):
    while True:
        name = raw_input('name :')
        if name == "": break
        unit = raw_input('unit :')
        i = Ingredient(name=name, unit=unit, is_food=True, section=section)
        print i.name, i.unit, 'added to', i.section
        i.save()


def get_ingredient_amount_from_string(line):
    for word in line.split():
        if word.isalpha():
            try:
                ingredient = Ingredient.objects.get(name=word)
                break
            except Ingredient.DoesNotExist:
                pass
    else:
        return 'No ingredient found in line : ' + line

    if not ingredient.unit in line:
        return 'Unit not found "' + ingredient.unit + '" in line ' + line

    match = re.search('\d+[,.]?\d*', line)
    if not match:
        return 'Amount not found in line : ' + line

    amount = float(match.group().replace(',', '.'))

    return IngredientAmount(ingredient=ingredient, amount=amount)

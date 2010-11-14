from models import Ingredient

def add_many_ingredients_to_section(section):
    while True:
        name = raw_input('name :')
        if name == "": break
        unit = raw_input('unit :')
        i = Ingredient(name=name, unit=unit, is_food=True, section=section)
        print i.name, i.unit, 'added to', i.section
        i.save()

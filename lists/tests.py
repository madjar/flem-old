from django.test import TestCase
import datetime
from models import ShoppingList

class ShoppingListTest(TestCase):
    def test_empty_range_creation(self):
        fro = datetime.date(2010, 9, 1)
        to = datetime.date(2010, 9, 30)
        l = ShoppingList.create_for_range(fro, to)
        meals = l.meals.all()
        self.assertEqual(meals.count(), 60)
        for meal in meals:
            meal.full_clean()
        l.full_clean()

    def test_empty_range_creation_with_no_lunch_on_first_day(self):
        date = datetime.date(2010, 9, 1)
        l = ShoppingList.create_for_range(date, date, moment_from='D')
        meal = l.meals.get()
        self.assertEqual(meal.date, date)
        self.assertEqual(meal.time_of_day, 'D')

    def test_empty_range_creation_with_no_dinner_on_last_day(self):
        date = datetime.date(2010, 9, 1)
        l = ShoppingList.create_for_range(date, date, moment_to='L')
        meal = l.meals.get()
        self.assertEqual(meal.date, date)
        self.assertEqual(meal.time_of_day, 'L')

    def test_non_empty_range_creation_without_override(self):
        from planning.models import Meal
        fro = datetime.date(2010, 9, 1)
        to = datetime.date(2010, 9, 3)

        preexistent_meal = Meal.objects.create(date=datetime.date(2010, 9, 2), time_of_day='L', persons=1)

        self.assertRaises(ShoppingList.RangeNotEmptyException,
                          ShoppingList.create_for_range,
                          fro, to)

    def test_non_empty_range_creation_with_override(self):
        from planning.models import Meal
        fro = datetime.date(2010, 9, 1)
        to = datetime.date(2010, 9, 3)

        preexistent_meal = Meal.objects.create(date=datetime.date(2010, 9, 2), time_of_day='L', persons=1)

        l = ShoppingList.create_for_range(fro, to, override=True)
        meals = l.meals.all()
        self.assertEqual(meals.count(), 6)
        preexistent_meal = Meal.objects.get(pk= preexistent_meal.pk) # Update cache
        self.assertEqual(preexistent_meal.shopping_list, l)

        for meal in meals:
            meal.full_clean()
        l.full_clean()

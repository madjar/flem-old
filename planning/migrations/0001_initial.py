# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Meal'
        db.create_table('planning_meal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('time_of_day', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('persons', self.gf('django.db.models.fields.IntegerField')()),
            ('shopping_list', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='meals', null=True, to=orm['lists.ShoppingList'])),
        ))
        db.send_create_signal('planning', ['Meal'])

        # Adding M2M table for field recipes on 'Meal'
        db.create_table('planning_meal_recipes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('meal', models.ForeignKey(orm['planning.meal'], null=False)),
            ('recipe', models.ForeignKey(orm['food.recipe'], null=False))
        ))
        db.create_unique('planning_meal_recipes', ['meal_id', 'recipe_id'])


    def backwards(self, orm):
        
        # Deleting model 'Meal'
        db.delete_table('planning_meal')

        # Removing M2M table for field recipes on 'Meal'
        db.delete_table('planning_meal_recipes')


    models = {
        'food.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'food.containment': {
            'Meta': {'object_name': 'Containment'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['food.Ingredient']"}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['food.Recipe']"})
        },
        'food.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_food': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['food.Section']"}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'})
        },
        'food.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['food.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['food.Ingredient']", 'through': "orm['food.Containment']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'food.section': {
            'Meta': {'object_name': 'Section'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'position': ('django.db.models.fields.IntegerField', [], {})
        },
        'lists.extraingredient': {
            'Meta': {'object_name': 'ExtraIngredient'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['food.Ingredient']"}),
            'shopping_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lists.ShoppingList']"})
        },
        'lists.notneededingredient': {
            'Meta': {'object_name': 'NotNeededIngredient'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['food.Ingredient']"}),
            'shopping_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lists.ShoppingList']"})
        },
        'lists.shoppinglist': {
            'Meta': {'object_name': 'ShoppingList'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'extra_ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'extra_in_lists'", 'symmetrical': 'False', 'through': "orm['lists.ExtraIngredient']", 'to': "orm['food.Ingredient']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'not_needed_ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'not_needed_in_lists'", 'symmetrical': 'False', 'through': "orm['lists.NotNeededIngredient']", 'to': "orm['food.Ingredient']"})
        },
        'planning.meal': {
            'Meta': {'object_name': 'Meal'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persons': ('django.db.models.fields.IntegerField', [], {}),
            'recipes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['food.Recipe']", 'symmetrical': 'False', 'blank': 'True'}),
            'shopping_list': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'meals'", 'null': 'True', 'to': "orm['lists.ShoppingList']"}),
            'time_of_day': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['planning']

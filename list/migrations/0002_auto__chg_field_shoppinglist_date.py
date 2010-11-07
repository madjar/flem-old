# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'ShoppingList.date'
        db.alter_column('list_shoppinglist', 'date', self.gf('django.db.models.fields.DateField')())
    
    
    def backwards(self, orm):
        
        # Changing field 'ShoppingList.date'
        db.alter_column('list_shoppinglist', 'date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True))
    
    
    models = {
        'food.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_food': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['food.Section']"}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'})
        },
        'food.section': {
            'Meta': {'object_name': 'Section'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'position': ('django.db.models.fields.IntegerField', [], {})
        },
        'list.extraingredient': {
            'Meta': {'object_name': 'ExtraIngredient'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['food.Ingredient']"}),
            'shopping_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['list.ShoppingList']"})
        },
        'list.notneededingredient': {
            'Meta': {'object_name': 'NotNeededIngredient'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['food.Ingredient']"}),
            'shopping_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['list.ShoppingList']"})
        },
        'list.shoppinglist': {
            'Meta': {'object_name': 'ShoppingList'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'extra_ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'extra_in_lists'", 'symmetrical': 'False', 'through': "orm['list.ExtraIngredient']", 'to': "orm['food.Ingredient']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'not_needed_ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'not_needed_in_lists'", 'symmetrical': 'False', 'through': "orm['list.NotNeededIngredient']", 'to': "orm['food.Ingredient']"})
        }
    }
    
    complete_apps = ['list']

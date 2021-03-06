# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ShoppingList'
        db.create_table('lists_shoppinglist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('lists', ['ShoppingList'])

        # Adding model 'ExtraIngredient'
        db.create_table('lists_extraingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['food.Ingredient'])),
            ('shopping_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lists.ShoppingList'])),
        ))
        db.send_create_signal('lists', ['ExtraIngredient'])

        # Adding model 'NotNeededIngredient'
        db.create_table('lists_notneededingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['food.Ingredient'])),
            ('shopping_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lists.ShoppingList'])),
        ))
        db.send_create_signal('lists', ['NotNeededIngredient'])


    def backwards(self, orm):
        
        # Deleting model 'ShoppingList'
        db.delete_table('lists_shoppinglist')

        # Deleting model 'ExtraIngredient'
        db.delete_table('lists_extraingredient')

        # Deleting model 'NotNeededIngredient'
        db.delete_table('lists_notneededingredient')


    models = {
        'food.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_food': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        }
    }

    complete_apps = ['lists']

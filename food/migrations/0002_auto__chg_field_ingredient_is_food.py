# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'Ingredient.is_food'
        db.alter_column('food_ingredient', 'is_food', self.gf('django.db.models.fields.BooleanField')(blank=True))
    
    
    def backwards(self, orm):
        
        # Changing field 'Ingredient.is_food'
        db.alter_column('food_ingredient', 'is_food', self.gf('django.db.models.fields.BooleanField')())
    
    
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
            'is_food': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['food.Section']"}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '64'})
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
        }
    }
    
    complete_apps = ['food']
